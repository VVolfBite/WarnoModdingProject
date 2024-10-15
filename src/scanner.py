from email import header
from typing import Collection
from src.extractors.translation_filter import dict_key_filter
import copy
import csv
import json

# 一个宏替换操作
def macro(file_stream):
    macro_rules = {
        "Metre": 2.92198967,
    }
    content = str(file_stream)
    for key, value in macro_rules.items():
        content = content.replace(key, str(value))
    return content

# 该函数用于收集叶子结构的键集
def collect(data, path=""):
    kv = {}
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list, tuple)):
                kv.update(collect(value, path + key + "/"))
            else:
                kv[path + str(key)] = value
    elif isinstance(data, tuple):
        if len(data) == 2:  # 处理二元组，将其视为键值对
            key, value = data
            if isinstance(value, (dict, list, tuple)):
                kv.update(collect(value, path + key + "/"))
            else:
                kv[path + str(key)] = value
    elif isinstance(data, list):
        for item in data:
            kv.update(collect(item, path))
    return kv

def export_csv(dict, file_name, filter=None):
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

def export_json(dict, file_name):
    json_output = json.dumps(dict, indent=4, ensure_ascii=False)
    with open(f"{file_name}.json", "w", encoding="utf-8") as json_file:
        json_file.write(json_output)

