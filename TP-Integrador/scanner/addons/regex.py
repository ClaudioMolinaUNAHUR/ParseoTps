from scanner.addons.tokens import *
from scanner.addons.regex_simple import *


def t_HASH_RESERVED(t):
    r"\#start|\#end"
    t.type = reserved.get(t.value, "ID")  # devuelve START o END reserved
    return t


def t_ID(t):
    r"[a-zA-Z]+"
    t.type = reserved.get(t.value, "ID")
    return t


def t_STRING(t):
    r"\".*?\"|'.*?'"
    t.value = t.value[1:-1]  # quita comillas
    return t


def t_NUMBER(t):
    r"-?[0-9]+(\.[0-9]+)?"  # reconoce 123 o 123.45
    if "." in t.value:
        t.value = float(t.value)  # si tiene punto -> float
    else:
        t.value = int(t.value)  # si no -> int
    return t


t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r"//(.|\n)*?-/"
    pass


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
