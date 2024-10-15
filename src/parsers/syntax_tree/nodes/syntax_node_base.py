# provides common functionality for any  object

class Datatype:
    UNKNOWN, STRUCTURAL,Nil ,  Boolean, Integer, HexInteger, Float, String_single, String_double, GUID, RGBA, Reference, \
    Pair, Vector, Map, Arithmetic, Object = range(17)

# 语法节点树的基类
class Base:
    def __init__(self):
        self.datatype = Datatype.UNKNOWN
        self.value = None

    def __str__(self):
        return "{type: " + str(self.datatype) + ", value: " + str(self.value) + "}"

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        return self.datatype == other.datatype and self.value == other.value

    def __hash__(self):
        return hash((self.datatype, self.value))

    def get__value(self, path: str, default=None):
        # to be implemented by subclasses
        print(self)
        print("not implemented")
        return default

    def set__value(self, path: str, value):
        # to be implemented by subclasses
        print(self)
        print("not implemented")
