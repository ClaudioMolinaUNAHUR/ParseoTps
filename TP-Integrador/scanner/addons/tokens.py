# Palabras reservadas
reserved = {
    "str": "STR",
    "num": "NUM",
    "bool": "BOOL",
    "func": "FUNC",
    "return": "RETURN",
    "if": "IF",
    "else": "ELSE",
    "loop": "LOOP",
    "in": "IN",
    "range": "RANGE",
    "console": "CONSOLE",
    "true": "TRUE",
    "false": "FALSE",
    "#start": "START",
    "#end": "END",
}

# Tokens generales + reservados
tokens = [
    # Identificadores y literales
    "ID", "NUMBER", "STRING",

    # Operadores
    "PLUS", "MINUS", "TIMES", "DIVIDE", "MOD",
    "AND", "OR", "NOT",
    "LT", "GT", "LE", "GE", "EQ", "NE",
    "ASSIGN",

    # Delimitadores
    "LPAREN", "RPAREN", "LBRACE", "RBRACE",
    "COMMA", "LBRACKET", "RBRACKET",
] + list(reserved.values())