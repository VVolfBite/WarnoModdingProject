# Generated from NdfGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,40,422,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,
        5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,
        1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,
        1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,
        1,31,1,32,1,32,1,32,1,32,5,32,258,8,32,10,32,12,32,261,9,32,1,32,
        1,32,1,32,1,32,1,32,5,32,268,8,32,10,32,12,32,271,9,32,1,32,3,32,
        274,8,32,1,33,3,33,277,8,33,1,33,4,33,280,8,33,11,33,12,33,281,1,
        34,3,34,285,8,34,1,34,4,34,288,8,34,11,34,12,34,289,1,34,1,34,5,
        34,294,8,34,10,34,12,34,297,9,34,1,34,5,34,300,8,34,10,34,12,34,
        303,9,34,1,34,1,34,4,34,307,8,34,11,34,12,34,308,3,34,311,8,34,1,
        35,1,35,1,36,1,36,1,36,4,36,318,8,36,11,36,12,36,319,1,37,1,37,1,
        37,1,37,1,37,1,37,1,37,1,37,1,37,5,37,331,8,37,10,37,12,37,334,9,
        37,1,37,1,37,1,38,4,38,339,8,38,11,38,12,38,340,1,39,4,39,344,8,
        39,11,39,12,39,345,1,39,1,39,1,40,1,40,1,40,1,40,5,40,354,8,40,10,
        40,12,40,357,9,40,1,40,1,40,5,40,361,8,40,10,40,12,40,364,9,40,1,
        40,3,40,367,8,40,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,
        44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,
        51,1,51,1,52,1,52,1,53,1,53,1,54,1,54,1,55,1,55,1,56,1,56,1,57,1,
        57,1,58,1,58,1,59,1,59,1,60,1,60,1,61,1,61,1,62,1,62,1,63,1,63,1,
        64,1,64,1,65,1,65,1,66,1,66,4,259,269,355,362,0,67,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,
        16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,
        27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,0,73,36,75,
        37,77,38,79,39,81,40,83,0,85,0,87,0,89,0,91,0,93,0,95,0,97,0,99,
        0,101,0,103,0,105,0,107,0,109,0,111,0,113,0,115,0,117,0,119,0,121,
        0,123,0,125,0,127,0,129,0,131,0,133,0,1,0,31,1,0,48,57,3,0,48,57,
        65,70,97,102,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,2,
        0,10,10,13,13,2,0,65,65,97,97,2,0,66,66,98,98,2,0,67,67,99,99,2,
        0,68,68,100,100,2,0,69,69,101,101,2,0,70,70,102,102,2,0,71,71,103,
        103,2,0,72,72,104,104,2,0,73,73,105,105,2,0,74,74,106,106,2,0,75,
        75,107,107,2,0,76,76,108,108,2,0,77,77,109,109,2,0,78,78,110,110,
        2,0,79,79,111,111,2,0,80,80,112,112,2,0,81,81,113,113,2,0,82,82,
        114,114,2,0,83,83,115,115,2,0,84,84,116,116,2,0,85,85,117,117,2,
        0,86,86,118,118,2,0,87,87,119,119,2,0,88,88,120,120,2,0,89,89,121,
        121,2,0,90,90,122,122,415,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,
        7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,
        1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,
        1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,
        1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,
        1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,
        1,0,0,0,0,69,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,
        1,0,0,0,0,81,1,0,0,0,1,135,1,0,0,0,3,137,1,0,0,0,5,139,1,0,0,0,7,
        141,1,0,0,0,9,143,1,0,0,0,11,145,1,0,0,0,13,147,1,0,0,0,15,149,1,
        0,0,0,17,151,1,0,0,0,19,153,1,0,0,0,21,155,1,0,0,0,23,157,1,0,0,
        0,25,159,1,0,0,0,27,161,1,0,0,0,29,163,1,0,0,0,31,165,1,0,0,0,33,
        167,1,0,0,0,35,172,1,0,0,0,37,178,1,0,0,0,39,182,1,0,0,0,41,185,
        1,0,0,0,43,189,1,0,0,0,45,193,1,0,0,0,47,198,1,0,0,0,49,205,1,0,
        0,0,51,209,1,0,0,0,53,215,1,0,0,0,55,220,1,0,0,0,57,225,1,0,0,0,
        59,232,1,0,0,0,61,240,1,0,0,0,63,248,1,0,0,0,65,273,1,0,0,0,67,276,
        1,0,0,0,69,284,1,0,0,0,71,312,1,0,0,0,73,314,1,0,0,0,75,321,1,0,
        0,0,77,338,1,0,0,0,79,343,1,0,0,0,81,349,1,0,0,0,83,370,1,0,0,0,
        85,372,1,0,0,0,87,374,1,0,0,0,89,376,1,0,0,0,91,378,1,0,0,0,93,380,
        1,0,0,0,95,382,1,0,0,0,97,384,1,0,0,0,99,386,1,0,0,0,101,388,1,0,
        0,0,103,390,1,0,0,0,105,392,1,0,0,0,107,394,1,0,0,0,109,396,1,0,
        0,0,111,398,1,0,0,0,113,400,1,0,0,0,115,402,1,0,0,0,117,404,1,0,
        0,0,119,406,1,0,0,0,121,408,1,0,0,0,123,410,1,0,0,0,125,412,1,0,
        0,0,127,414,1,0,0,0,129,416,1,0,0,0,131,418,1,0,0,0,133,420,1,0,
        0,0,135,136,5,61,0,0,136,2,1,0,0,0,137,138,5,40,0,0,138,4,1,0,0,
        0,139,140,5,41,0,0,140,6,1,0,0,0,141,142,5,58,0,0,142,8,1,0,0,0,
        143,144,5,45,0,0,144,10,1,0,0,0,145,146,5,43,0,0,146,12,1,0,0,0,
        147,148,5,42,0,0,148,14,1,0,0,0,149,150,5,60,0,0,150,16,1,0,0,0,
        151,152,5,44,0,0,152,18,1,0,0,0,153,154,5,62,0,0,154,20,1,0,0,0,
        155,156,5,91,0,0,156,22,1,0,0,0,157,158,5,93,0,0,158,24,1,0,0,0,
        159,160,5,36,0,0,160,26,1,0,0,0,161,162,5,126,0,0,162,28,1,0,0,0,
        163,164,5,47,0,0,164,30,1,0,0,0,165,166,5,124,0,0,166,32,1,0,0,0,
        167,168,3,121,60,0,168,169,3,117,58,0,169,170,3,123,61,0,170,171,
        3,91,45,0,171,34,1,0,0,0,172,173,3,93,46,0,173,174,3,83,41,0,174,
        175,3,105,52,0,175,176,3,119,59,0,176,177,3,91,45,0,177,36,1,0,0,
        0,178,179,3,107,53,0,179,180,3,83,41,0,180,181,3,113,56,0,181,38,
        1,0,0,0,182,183,3,99,49,0,183,184,3,119,59,0,184,40,1,0,0,0,185,
        186,3,89,44,0,186,187,3,99,49,0,187,188,3,125,62,0,188,42,1,0,0,
        0,189,190,3,109,54,0,190,191,3,99,49,0,191,192,3,105,52,0,192,44,
        1,0,0,0,193,194,3,85,42,0,194,195,3,111,55,0,195,196,3,111,55,0,
        196,197,3,105,52,0,197,46,1,0,0,0,198,199,3,119,59,0,199,200,3,121,
        60,0,200,201,3,117,58,0,201,202,3,99,49,0,202,203,3,109,54,0,203,
        204,3,95,47,0,204,48,1,0,0,0,205,206,3,99,49,0,206,207,3,109,54,
        0,207,208,3,121,60,0,208,50,1,0,0,0,209,210,3,93,46,0,210,211,3,
        105,52,0,211,212,3,111,55,0,212,213,3,83,41,0,213,214,3,121,60,0,
        214,52,1,0,0,0,215,216,3,113,56,0,216,217,3,83,41,0,217,218,3,99,
        49,0,218,219,3,117,58,0,219,54,1,0,0,0,220,221,3,105,52,0,221,222,
        3,99,49,0,222,223,3,119,59,0,223,224,3,121,60,0,224,56,1,0,0,0,225,
        226,3,91,45,0,226,227,3,129,64,0,227,228,3,113,56,0,228,229,3,111,
        55,0,229,230,3,117,58,0,230,231,3,121,60,0,231,58,1,0,0,0,232,233,
        3,113,56,0,233,234,3,117,58,0,234,235,3,99,49,0,235,236,3,125,62,
        0,236,237,3,83,41,0,237,238,3,121,60,0,238,239,3,91,45,0,239,60,
        1,0,0,0,240,241,3,123,61,0,241,242,3,109,54,0,242,243,3,109,54,0,
        243,244,3,83,41,0,244,245,3,107,53,0,245,246,3,91,45,0,246,247,3,
        89,44,0,247,62,1,0,0,0,248,249,3,117,58,0,249,250,3,95,47,0,250,
        251,3,85,42,0,251,252,3,83,41,0,252,64,1,0,0,0,253,259,5,34,0,0,
        254,255,5,92,0,0,255,258,5,34,0,0,256,258,9,0,0,0,257,254,1,0,0,
        0,257,256,1,0,0,0,258,261,1,0,0,0,259,260,1,0,0,0,259,257,1,0,0,
        0,260,262,1,0,0,0,261,259,1,0,0,0,262,274,5,34,0,0,263,269,5,39,
        0,0,264,265,5,92,0,0,265,268,5,39,0,0,266,268,9,0,0,0,267,264,1,
        0,0,0,267,266,1,0,0,0,268,271,1,0,0,0,269,270,1,0,0,0,269,267,1,
        0,0,0,270,272,1,0,0,0,271,269,1,0,0,0,272,274,5,39,0,0,273,253,1,
        0,0,0,273,263,1,0,0,0,274,66,1,0,0,0,275,277,5,45,0,0,276,275,1,
        0,0,0,276,277,1,0,0,0,277,279,1,0,0,0,278,280,7,0,0,0,279,278,1,
        0,0,0,280,281,1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,68,1,0,
        0,0,283,285,5,45,0,0,284,283,1,0,0,0,284,285,1,0,0,0,285,310,1,0,
        0,0,286,288,7,0,0,0,287,286,1,0,0,0,288,289,1,0,0,0,289,287,1,0,
        0,0,289,290,1,0,0,0,290,291,1,0,0,0,291,295,5,46,0,0,292,294,7,0,
        0,0,293,292,1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,
        0,0,296,311,1,0,0,0,297,295,1,0,0,0,298,300,7,0,0,0,299,298,1,0,
        0,0,300,303,1,0,0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,304,1,0,
        0,0,303,301,1,0,0,0,304,306,5,46,0,0,305,307,7,0,0,0,306,305,1,0,
        0,0,307,308,1,0,0,0,308,306,1,0,0,0,308,309,1,0,0,0,309,311,1,0,
        0,0,310,287,1,0,0,0,310,301,1,0,0,0,311,70,1,0,0,0,312,313,7,1,0,
        0,313,72,1,0,0,0,314,315,5,48,0,0,315,317,3,129,64,0,316,318,3,71,
        35,0,317,316,1,0,0,0,318,319,1,0,0,0,319,317,1,0,0,0,319,320,1,0,
        0,0,320,74,1,0,0,0,321,322,5,71,0,0,322,323,5,85,0,0,323,324,5,73,
        0,0,324,325,5,68,0,0,325,326,5,58,0,0,326,327,5,123,0,0,327,332,
        1,0,0,0,328,331,3,71,35,0,329,331,5,45,0,0,330,328,1,0,0,0,330,329,
        1,0,0,0,331,334,1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,335,
        1,0,0,0,334,332,1,0,0,0,335,336,5,125,0,0,336,76,1,0,0,0,337,339,
        7,2,0,0,338,337,1,0,0,0,339,340,1,0,0,0,340,338,1,0,0,0,340,341,
        1,0,0,0,341,78,1,0,0,0,342,344,7,3,0,0,343,342,1,0,0,0,344,345,1,
        0,0,0,345,343,1,0,0,0,345,346,1,0,0,0,346,347,1,0,0,0,347,348,6,
        39,0,0,348,80,1,0,0,0,349,350,5,47,0,0,350,351,5,47,0,0,351,366,
        1,0,0,0,352,354,9,0,0,0,353,352,1,0,0,0,354,357,1,0,0,0,355,356,
        1,0,0,0,355,353,1,0,0,0,356,358,1,0,0,0,357,355,1,0,0,0,358,367,
        7,4,0,0,359,361,8,4,0,0,360,359,1,0,0,0,361,364,1,0,0,0,362,363,
        1,0,0,0,362,360,1,0,0,0,363,365,1,0,0,0,364,362,1,0,0,0,365,367,
        5,0,0,1,366,355,1,0,0,0,366,362,1,0,0,0,367,368,1,0,0,0,368,369,
        6,40,0,0,369,82,1,0,0,0,370,371,7,5,0,0,371,84,1,0,0,0,372,373,7,
        6,0,0,373,86,1,0,0,0,374,375,7,7,0,0,375,88,1,0,0,0,376,377,7,8,
        0,0,377,90,1,0,0,0,378,379,7,9,0,0,379,92,1,0,0,0,380,381,7,10,0,
        0,381,94,1,0,0,0,382,383,7,11,0,0,383,96,1,0,0,0,384,385,7,12,0,
        0,385,98,1,0,0,0,386,387,7,13,0,0,387,100,1,0,0,0,388,389,7,14,0,
        0,389,102,1,0,0,0,390,391,7,15,0,0,391,104,1,0,0,0,392,393,7,16,
        0,0,393,106,1,0,0,0,394,395,7,17,0,0,395,108,1,0,0,0,396,397,7,18,
        0,0,397,110,1,0,0,0,398,399,7,19,0,0,399,112,1,0,0,0,400,401,7,20,
        0,0,401,114,1,0,0,0,402,403,7,21,0,0,403,116,1,0,0,0,404,405,7,22,
        0,0,405,118,1,0,0,0,406,407,7,23,0,0,407,120,1,0,0,0,408,409,7,24,
        0,0,409,122,1,0,0,0,410,411,7,25,0,0,411,124,1,0,0,0,412,413,7,26,
        0,0,413,126,1,0,0,0,414,415,7,27,0,0,415,128,1,0,0,0,416,417,7,28,
        0,0,417,130,1,0,0,0,418,419,7,29,0,0,419,132,1,0,0,0,420,421,7,30,
        0,0,421,134,1,0,0,0,22,0,257,259,267,269,273,276,281,284,289,295,
        301,308,310,319,330,332,340,345,355,362,366,1,6,0,0
    ]

class NdfGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    K_TRUE = 17
    K_FALSE = 18
    K_MAP = 19
    K_IS = 20
    K_DIV = 21
    K_NIL = 22
    K_BOOL = 23
    K_STRING = 24
    K_INT = 25
    K_FLOAT = 26
    K_PAIR = 27
    K_LIST = 28
    K_EXPORT = 29
    K_PRIVATE = 30
    K_UNNAMED = 31
    K_RGBA = 32
    STRING = 33
    INT = 34
    FLOAT = 35
    HEXNUMBER = 36
    GUID = 37
    ID = 38
    WS = 39
    COMMENT = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "':'", "'-'", "'+'", "'*'", "'<'", "','", 
            "'>'", "'['", "']'", "'$'", "'~'", "'/'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "K_TRUE", "K_FALSE", "K_MAP", "K_IS", "K_DIV", "K_NIL", "K_BOOL", 
            "K_STRING", "K_INT", "K_FLOAT", "K_PAIR", "K_LIST", "K_EXPORT", 
            "K_PRIVATE", "K_UNNAMED", "K_RGBA", "STRING", "INT", "FLOAT", 
            "HEXNUMBER", "GUID", "ID", "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "K_TRUE", "K_FALSE", "K_MAP", "K_IS", 
                  "K_DIV", "K_NIL", "K_BOOL", "K_STRING", "K_INT", "K_FLOAT", 
                  "K_PAIR", "K_LIST", "K_EXPORT", "K_PRIVATE", "K_UNNAMED", 
                  "K_RGBA", "STRING", "INT", "FLOAT", "HEXDIGIT", "HEXNUMBER", 
                  "GUID", "ID", "WS", "COMMENT", "A", "B", "C", "D", "E", 
                  "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

    grammarFileName = "NdfGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


