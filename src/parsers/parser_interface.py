from antlr4 import *
import antlr4
import copy
import csv
import json

from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser

from src.parsers.syntax_tree.actions import semantic_actions_generator
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *
from src.scanner import *

# 一个宏替换操作
def macro(file_stream):
    macro_rules = {
        "Metre": 2.92198967,
    }
    content = str(file_stream)
    for key, value in macro_rules.items():
        content = content.replace(key, str(value))
    return content


def generate_node_object(file_name: str) -> [Assignment]:  # type: ignore
    input = antlr4.InputStream(macro(FileStream(file_name, encoding="utf8")))
    lexer = NdfGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = NdfGrammarParser(stream)
    tree = parser.ndf_file()
    listener = semantic_actions_generator.Generator(parser)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return File(listener.assignments)


def value_from_node(entity: Base):
    if isinstance(entity, Map):
        py_map = {}
        for key in entity.map.keys():
            py_map[key] = value_from_node(entity.map[key])
        return py_map
     # @NOTE 目前不清楚Pair要处理为list还是map，由于pair不对值做内建限制，如果处理为map可能会导致键出问题
    elif isinstance(entity, Pair):
        py_tuple = (value_from_node(entity.value[0]), value_from_node(entity.value[1]))
        return py_tuple
    elif isinstance(entity, Vector):
        py_ls = []
        for val in entity.value:
            py_ls.append(value_from_node(val))
        return py_ls
    elif isinstance(entity,Assignment):
        py_dict = {entity.id : value_from_node(entity.value)}

        return py_dict
    elif isinstance(entity,File):
        py_dict = {}
        for assignment in entity.value:
            py_dict.update(value_from_node(assignment))
        return py_dict
    # @NOTE 是否要带类型描述？
    elif isinstance(entity,Object):
        py_dict = {}
        py_dict_v = {}
        vals = []
        for val in entity.value:
            py_dict_v.update(value_from_node(val))
        py_dict = {entity.object_type : py_dict_v}
        return py_dict
    elif isinstance(entity, Collection):
        vals = []
        for val in entity.value:
            vals.append(value_from_node(val))
        return vals
    # else return a simple data type
    match entity.datatype:

        case Datatype.Integer:
            return int(entity.value)
        case Datatype.Boolean:
            return bool(entity.value)
        case Datatype.Float:
            return float(entity.value)
        case Datatype.Reference:
            # return Path(str(entity.value))
            return str(entity.value)
        case Datatype.Nil:
            entity.value = None
        case _:
            return str(entity.value)

# 用于将Python转化为Base对象，效果不是特别好
# @NOTE 目前没有更改和应用
def node_from_value(value, dtypes: [Datatype]) -> Base: # type: ignore
    if isinstance(value, dict):
        _map = Map()
        for key in value.keys():
            _pair = Pair()
            _pair.append(node_from_value(key, dtypes))
            _pair.append(node_from_value(value[key], dtypes))
            _map.append(_pair)
        return _map
    elif isinstance(value, list):
        _list = Vector()
        for val in value:
            _list.append(node_from_value(val, dtypes))
        return _list
    # else construct primitive entity
    entity = Base()
    entity.datatype = dtypes.pop()
    match entity.datatype:
        case Datatype.Integer:
            entity.value = int(value)
        case Datatype.Boolean:
            entity.value = bool(value)
        case Datatype.Float:
            entity.value = float(value)
        case Datatype.Nil:
            entity.value = None
        case _:
            entity.value = str(value)
    return entity

# 该函数用于收集叶子结构的键集
def collect(node, path=""):
    kv = {}
    if isinstance(node, dict):
        for key, value in node.items():
            if isinstance(value, (dict, list, tuple)):
                kv.update(collect(value, path + key + "/"))
            else:
                kv[path + str(key)] = value
    elif isinstance(node, tuple):
        if len(node) == 2:  # 处理二元组，将其视为键值对
            key, value = node
            if isinstance(value, (dict, list, tuple)):
                kv.update(collect(value, path + key + "/"))
            else:
                kv[path + str(key)] = value
    elif isinstance(node, list):
        for item in node:
            kv.update(collect(item, path))
    return kv

def export_csv(node, file_name, filter=None):
    dict = collect(node)
    header = set()
    data = {}

    def get_header():
        for key, value in dict.items():
            attr_name = key.split("/")[-1]
            header.add(attr_name)

    def get_data():
        template_dict = {h: "" for h in header}
        for key, value in dict.items():
            item_name = key.split("/")[0]

            if item_name not in data:
                data[item_name] = copy.deepcopy(template_dict)
            attr_name = key.split("/")[-1]
            data[item_name][attr_name] = value

    def get_csv():

        csv_file = f"{file_name}.csv"
        fieldnames = ["Name"] + list(header)
        with open(csv_file, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for name, item in data.items():
                item["Name"] = name
                writer.writerow(item)

    def get_chinese_csv():
        csv_file = f"{file_name}.csv"
        fieldnames = ["名称"] + list(dict_key_filter[filter].values())
        with open(csv_file, mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for name, item in data.items():
                row = {"名称": name}
                for k, v in dict_key_filter[filter].items():
                    if k in item:
                        val = item[k]
                        if val == True:
                            val = "是"
                        if val == False:
                            val = "否"
                        if val == None or val == "":
                            val = "无"
                        row[v] = val
                    else:
                        row[v] = "无"
                writer.writerow(row)

    get_header()
    get_data()
    get_chinese_csv()

def export_json(node, file_name):
    dict = collect(node)
    json_output = json.dumps(dict, indent=4, ensure_ascii=False)
    with open(f"{file_name}.json", "w", encoding="utf-8") as json_file:
        json_file.write(json_output)
