import logging

from pathlib import Path

from src.parsers.syntax_tree.nodes.syntax_node_base import *
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *

 # Collection是一种中间形式，用于描述出去Assigment后的所有基本结构的基类
 # 如 [v1,v2,v3] Map[(k1,v1),(k2,v2)] (p1,p2)等等
 # lookup是一个快速查阅检索的字典，主要用于查询Assigment的字段内容 
class Collection(Base):
    def __init__(self):
        super().__init__()
        self.value = []
        self.lookup = {}

    def append(self, data: Base):
        self.value.append(data)
        if isinstance(data, Assignment):
            self.lookup[data.id] = len(self.value) - 1
        elif isinstance(data, Object):
            self.lookup[data.object_type] = len(self.value) - 1

    def get__value(self, path: str, default=None):
        # get current ID
        current = path.split("\\")[0]
        # build remaining path
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        # if nothing remains, return own value
        if current == "":
            return self.value
        # otherwise, call function on own value
        elif self.lookup.__contains__(current):
            return self.value[self.lookup[current]].get__value(remaining, default)
        else:
            print("Could not find value for " + str(path) + " on " + str(self))
            return default

    def set__value(self, path: str, value):
        # get current ID
        current = path.split("\\")[0]
        # build remaining path
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        # if nothing remains, return own value
        if current == "":
            self.value = value
        # otherwise, call function on own value
        elif self.lookup.__contains__(current):
            self.value[self.lookup[current]].set__value(remaining, value)
        else:
            print("could not find " + path + "\nremaining: " + remaining)

    def set_raw_value(self, path: str, value, dtypes: [Datatype]): # type: ignore
        entity = node_from_value(value, dtypes)
        self.set__value(path, entity)

    def get_raw_value(self, path: str, default=None):
        result = self.get__value(path, default)
        return value_from_node(result)

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        if not len(self.value) == len(other.value):
            return False
        for i in range(len(self.value)):
            if not self.value[i] == other.value[i]:
                return False
        return True

    def __len__(self):
        return len(self.value)

    def contains(self, item):
        return self.value.__contains__(item)

# File是对文件的基本描述，即一个Ndf文件本身，它将文件视为Assignments的集合
# 即 [A1,A2,A3] 
class File(Collection):
    def __init__(self, assignments=[]):
        super().__init__()
        self.datatype = Datatype.STRUCTURAL
        for assignment in assignments:
            self.append(assignment)

    def __str__(self):
        return "{type: file, value: " + ''.join(map(str, self.value)) + "}"

# Object是对对象的描述，类似面向对象语言的实例化即 ClassA(Member = Value)
# 因此Value是对象列表
class Object(Collection):
    def __init__(self):
        super().__init__()
        self.value = []
        self.object_type = ""
        self.datatype = Datatype.Object

    def __str__(self):
        return "{type: object, value: " + ''.join(map(str, self.value)) + "}"

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        if self.object_type != other.object_type or self.value != other.value:
            return False
        return super().__eq__(other)

# Object是对对的描述，是NDF中特有的数据类型，即(P1,P2)
# 因此Value是两个数据值
class Pair(Collection):
    def __init__(self):
        super().__init__()
        self.value = []
        self.datatype = Datatype.Pair

    def append(self, data: Base):
        super().append(data)
        if len(self.value) > 2:
            logging.warning("Tried to append " + str(data) + " to a full Pair. Discarded")
            del self.value[2]

    def __str__(self):
        return "{type: pair, value: " + ''.join(map(str, self.value)) + "}"

# Vector是对数组的描述，即[V1,V2,V3]
# 因此Value是列表中的数据值
class Vector(Collection):
    def __init__(self):
        super().__init__()
        self.value = []
        self.datatype = Datatype.Vector

    def __str__(self):
        return "{type: vector, value: " + ''.join(map(str, self.value)) + "}"

# Map是对字典的描述，即Map[(k1,v1),(k2,v2)]
# 因此Value是字典的pair value表 而map是键值对
class Map(Collection):
    def __init__(self):
        super().__init__()
        self.value = []
        self.map = {}
        self.datatype = Datatype.Map

    def append(self, data: Pair):
        super().append(data)
        self.map[str(data.value[0].value)] = data.value[1]
        self.lookup[str(data.value[0].value)] = len(self.value) - 1

    def get__value(self, path: str, default=None):
        # get current ID
        current = path.split("\\")[0]
        # build remaining path
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        # if nothing remains, return own value
        if current == "":
            return self.value
        # if value is in map, return it
        elif self.lookup.__contains__(current) and remaining == "":
            return self.map[current]
        # otherwise, call function on own value
        elif self.lookup.__contains__(current):
            return self.map[current].get__value(remaining, default)
        else:
            print("Could not find value for " + str(path) + " on " + str(self))
            return default

    def set__value(self, path: str, value):
        # get current ID
        current = path.split("\\")[0]
        # build remaining path
        remaining = path.removeprefix(current)
        remaining = remaining.removeprefix("\\")
        # if nothing remains, return own value
        if current == "":
            self.value = value
        # if no more path, insert in current map
        elif self.lookup.__contains__(current) and remaining == "":
            self.value[self.lookup[current]].value[1] = value
        # otherwise, call function on own value
        elif self.lookup.__contains__(current):
            self.map[current].set__value(remaining, value)
        else:
            print("could not find " + path + "\nremaining: " + remaining)

    def __str__(self):
        return "{type: map, value: " + ''.join(map(str, self.value)) + "}"

