from antlr4 import *
from src.parsers.parser.NdfGrammarListener import NdfGrammarListener
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser

from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *

import logging

# 此文件实际充当了语义指导的功能，以堆栈的形式实现了规约和递进时的语义逻辑
DISABLE_CALCULATING = False

# Stack类模拟语法栈
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, elem):
        self._stack.append(elem)

    def pop(self):
        return self._stack.pop()

    # 不弹出顶端部件
    def top(self):
        if len(self._stack) > 0:
            return self._stack[len(self._stack) - 1]
        else:
            return None

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        ''.join(map(str, self._stack))


# put on the Stack to mark end of a Stack frame
class StackMarker:
    pass


class Generator(NdfGrammarListener):

    def __init__(self, parser: NdfGrammarParser):
        super().__init__()
        self.rule_names = parser.ruleNames

        self.assignments = []
        self.stack = Stack()
        # Track depth of rules to be ignored
        self.ignore = 0

    def enterNormal_assignment(self, ctx: NdfGrammarParser.Normal_assignmentContext):
        if self.ignore > 0:
            return
        # push new assignment to stack
        self.stack.push(Assignment())
    def exitNormal_assignment(self, ctx: NdfGrammarParser.Normal_assignmentContext):
        if self.ignore > 0:
            return
        # pop value off stack and assign to assignment
        value = self.stack.pop()
        self.stack.top().value = value
        # pop assignment off stack if it's top level
        if len(self.stack) == 1:
            assignment = self.stack.pop()
            self.assignments.append(assignment)

    def enterExport_prefix(self, ctx: NdfGrammarParser.Export_prefixContext):
        if self.ignore > 0:
            return
        # assign "export" to top item on stack
        self.stack.top().export = True

    def enterPrivate_prefix(self, ctx: NdfGrammarParser.Private_prefixContext):
        if self.ignore > 0:
            return
        # assign "private" to top item on stack
        self.stack.top().private = True

    def enterId(self, ctx: NdfGrammarParser.IdContext):
        if self.ignore > 0:
            return
        # assign ID to top item on stack
        self.stack.top().id = ctx.getText()
    
    def enterNil_value(self, ctx: NdfGrammarParser.Nil_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.datatype = Datatype.Nil
        entity.value = None
        self.stack.push(entity)

    def enterBool_value(self, ctx: NdfGrammarParser.Bool_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.datatype = Datatype.Boolean
        if ctx.getText().lower() == "false":
            entity.value = False
        else:
            entity.value = True
        self.stack.push(entity)

    def enterInt_value(self, ctx: NdfGrammarParser.Int_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.datatype = Datatype.Integer
        entity.value = int(ctx.getText())
        self.stack.push(entity)

    def enterString_value(self, ctx: NdfGrammarParser.String_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        value = ctx.getText()
        if value[0] == "\'":
            entity.datatype = Datatype.String_single
        else:
            entity.datatype = Datatype.String_double
        entity.value = value[1:-1]
        self.stack.push(entity)

    def enterHex_value(self, ctx: NdfGrammarParser.Hex_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.datatype = Datatype.HexInteger
        entity.value = ctx.getText()
        self.stack.push(entity)

    def enterFloat_value(self, ctx: NdfGrammarParser.Float_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.datatype = Datatype.Float
        entity.value = float(ctx.getText())
        self.stack.push(entity)

    def enterGuid_value(self, ctx: NdfGrammarParser.Guid_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.datatype = Datatype.GUID
        entity.value = ctx.getText()
        self.stack.push(entity)

    def enterRgba_value(self, ctx: NdfGrammarParser.Rgba_valueContext):
        if self.ignore > 0:
            return
        entity = Base()
        entity.datatype = Datatype.RGBA

        text = ctx.getText()
        text = text.replace(" ", "")
        text = text.removeprefix("RGBA[")
        text = text.removesuffix("]")

        nums = text.split(",")
        entity.value = [int(x) for x in nums]
        self.stack.push(entity)

    def enterObj_reference_value(self, ctx: NdfGrammarParser.Obj_reference_valueContext):
        self.ignore += 1
        if self.ignore > 1:
            return
        # assign reference datatype and value to top item on stack
        entity = Base()
        entity.datatype = Datatype.Reference
        entity.value = ctx.getText()
        self.stack.push(entity)

    def exitObj_reference_value(self, ctx: NdfGrammarParser.Obj_reference_valueContext):
        if self.ignore > 0:
            self.ignore -= 1

    def enterPair_value(self, ctx: NdfGrammarParser.Pair_valueContext):
        if self.ignore > 0:
            return
        self.stack.push(Pair())
        self.stack.push(StackMarker())

    def exitPair_value(self, ctx: NdfGrammarParser.Pair_valueContext):
        if self.ignore > 0:
            return
        pair_values = []
        while type(self.stack.top()) != StackMarker:
            pair_values.append(self.stack.pop())
        pair_values.reverse()
        # remove stack marker
        self.stack.pop()
        for value in pair_values:
            self.stack.top().append(value)

    def enterVector_value(self, ctx: NdfGrammarParser.Vector_valueContext):
        if self.ignore > 0:
            return
        self.stack.push(Vector())
        self.stack.push(StackMarker())

    def exitVector_value(self, ctx: NdfGrammarParser.Vector_valueContext):
        if self.ignore > 0:
            return
        vector_values = []
        while type(self.stack.top()) != StackMarker:
            vector_values.append(self.stack.pop())
        vector_values.reverse()
        # remove stack marker
        self.stack.pop()
        for value in vector_values:
            self.stack.top().append(value)

    def enterMap_value(self, ctx: NdfGrammarParser.Map_valueContext):
        if self.ignore > 0:
            return
        self.stack.push(Map())
        self.stack.push(StackMarker())

    def exitMap_value(self, ctx: NdfGrammarParser.Map_valueContext):
        if self.ignore > 0:
            return
        map_values = []
        while type(self.stack.top()) != StackMarker:
            map_values.append(self.stack.pop())
        map_values.reverse()
        # remove stack marker
        self.stack.pop()
        for value in map_values:
            self.stack.top().append(value)

    def enterArithmetic(self, ctx: NdfGrammarParser.ArithmeticContext):
        # don't treat single elements as arithmetic if we aren't already inside another arithmetic
        if DISABLE_CALCULATING == True:
            if len(ctx.children) <= 1 and self.ignore <= 0:
                return
            # ignore everything until we exit arithmetic
            self.ignore += 1
            if self.ignore > 1:
                return
            arithmetic = Base()
            arithmetic.datatype = Datatype.Arithmetic
            # add spaces to text
            text = ctx.getText()
            text = text.replace("+", " + ")
            text = text.replace("-", " - ")
            text = text.replace("*", " * ")
            # TODO: this might be dangerous if ID contains "div"
            text = text.replace("div", " div ")
            text = text.replace("DIV", " DIV ")
            arithmetic.value = text

            self.stack.push(arithmetic)
            return
    

        if len(ctx.children) <= 1 and self.ignore <= 0:
            return
        # # ignore everything until we exit arithmetic
        # self.ignore += 1
        if self.ignore > 0:
            return
        arithmetic = Base()
        arithmetic.datatype = Datatype.Arithmetic
        # add spaces to text
        text = ctx.getText()
        text = text.replace("+", " + ")
        text = text.replace("-", " - ")
        text = text.replace("*", " * ")
        # TODO: this might be dangerous if ID contains "div"
        text = text.replace("div", " div ")
        text = text.replace("DIV", " DIV ")

        self.stack.push(arithmetic)

    def exitArithmetic(self, ctx: NdfGrammarParser.ArithmeticContext):
        if DISABLE_CALCULATING == True:
            if self.ignore > 0:
                self.ignore -= 1
            return
        if self.ignore > 0:
            return
        if ctx.getChildCount() == 1:
            return 
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "-":
            op1 = self.stack.pop()
            self.stack.top().value = -op1.value
            return 
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(" and ctx.getChild(2).getText() == ")":
            op1 = self.stack.pop()
            self.stack.top().value = op1.value
            return 
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "+" :
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            self.stack.top().value = op1.value + op2.value
            return
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "-" :
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            self.stack.top().value = op1.value - op2.value
            return
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "*" :
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            self.stack.top().value = op1.value * op2.value
            return
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "div" :
            op2 = self.stack.pop()
            op1 = self.stack.pop()
            self.stack.top().value = op1.value / op2.value
            return
        

    def enterOp(self, ctx: NdfGrammarParser.Object_typeContext):
        # TODO: edit text, add spaces around op
        pass


    def enterObject_type(self, ctx: NdfGrammarParser.Object_typeContext):
        if self.ignore > 0:
            return
        obj = Object()
        obj.object_type = ctx.getText()
        self.stack.push(obj)
        self.stack.push(StackMarker())

    def exitObject(self, ctx: NdfGrammarParser.ObjectContext):
        if self.ignore > 0:
            return
        members = []
        while type(self.stack.top()) != StackMarker:
            members.append(self.stack.pop())
        members.reverse()
        # remove stack marker
        self.stack.pop()
        for value in members:
            self.stack.top().append(value)

    def enterMember_assignment(self, ctx: NdfGrammarParser.Member_assignmentContext):
        if self.ignore > 0:
            return
        assignment = Assignment()
        assignment.member = True
        # push new assignment to stack
        self.stack.push(assignment)

    def exitMember_assignment(self, ctx: NdfGrammarParser.Member_assignmentContext):
        if self.ignore > 0:
            return
        # pop value off stack and assign to assignment
        value = self.stack.pop()
        self.stack.top().value = value
    
    def enterUnnamed_assignment(self, ctx: NdfGrammarParser.Unnamed_assignmentContext):
        if self.ignore > 0:
            return
        assignment = Assignment()
        assignment.unnamed = True
        # push new assignment to stack
        self.stack.push(assignment)

    def exitUnnamed_assignment(self, ctx: NdfGrammarParser.Unnamed_assignmentContext):
        if self.ignore > 0:
            return
        # pop value off stack and assign to assignment
        value = self.stack.pop()

        self.stack.top().value = value
        self.stack.top().id = "Unnamed-"+ str(hash(str(value)))
        # pop assignment off stack if it's top level
        if len(self.stack) == 1:
            assignment = self.stack.pop()
            self.assignments.append(assignment)        

