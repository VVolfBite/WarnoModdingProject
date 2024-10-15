from src.parsers.syntax_tree.nodes.syntax_node_base import *

# Assignment是一个描述文件中基本语句的节点类
# 基本结构是 export/private id is value
# 还有一种member形式 即 id = value
class Assignment(Base):
    def __init__(self):
        super().__init__()
        self.id = ""
        self.datatype = Datatype.STRUCTURAL
        self.export = False
        self.private = False
        self.unnamed = False
        self.member = False

    def __str__(self):
        return "{id: " + self.id + " type: assignment, export: " + str(self.export) + ", private: " + \
               str(self.private) + ", member: " + str(self.member) + ", value: " + str(self.value) + "}"

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        ret = self.datatype == other.datatype and self.id == other.id and self.export == other.export \
               and self.member == other.member and self.unnamed == other.unnamed and self.value == other.value
        return ret

    def get__value(self, path: str, default=None):
        # get current ID
        current = path.split("\\")[0]
        # if nothing remains, return own value
        if current == "":
            return self.value
        elif isinstance(self.value, Base):
            return self.value.get__value(path, default)
        else:
            return default

    def set__value(self, path: str, value):
        # get current ID
        current = path.split("\\")[0]
        # if nothing remains, return own value
        if current == "":
            self.value = value
        elif isinstance(self.value, Base):
            self.value.set__value(path, value)
        else:
            print("could not find " + path + "\ncurrent: " + current)

