import os
import re
import json

from antlr4 import *
import antlr4
from antlr4.tree.Trees import Trees

from src.parsers.parser.NdfGrammarLexer import NdfGrammarLexer
from src.parsers.parser.NdfGrammarParser import NdfGrammarParser

from src.parsers.syntax_tree.actions import semantic_actions_generator
from src.parsers.syntax_tree.nodes.syntax_node_assignment import *
from src.parsers.syntax_tree.nodes.syntax_node_collection import *
from src.parsers.util import ndf_converter

from src.scanner import *

def generate_(file_name: str) -> [Assignment]:  # type: ignore
    input = antlr4.InputStream(macro(FileStream(file_name, encoding="utf8")))
    lexer = NdfGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = NdfGrammarParser(stream)
    tree = parser.ndf_file()
    listener = semantic_actions_generator.Generator(parser)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return File(listener.assignments)


def main():
    target_ndf_file = "./Ammunition.ndf"
    output_file_name = target_ndf_file.split("/")[-1].split(".")[0]
    _file = value_from_(generate_(target_ndf_file))
    filter_key = "ammunition"
    collection = collect(_file)
    export_csv(collection, output_file_name, filter_key)
    export_json(_file,output_file_name)

main()
