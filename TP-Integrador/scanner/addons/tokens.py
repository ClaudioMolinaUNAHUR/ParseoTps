# tokens que reconoce el lexer, luego el parser los usara como terminales (tokens)
# algunos tokens son palabras reservadas (reserved), que tienen un significado especial en el
# "COMO_SE_ESCRIBE_EN_CODIGO" : "NOMBRE_DEL_TOKEN"
reserved = {
    "str": "STR",
    "num": "NUM",
    "bool": "BOOL",
    "list": "LIST",
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
     # TODO: implementar 
    "size": "SIZE",
    "add": "ADD",
    "remove": "REMOVE", 
    "has": "HAS",
}

#son todos los tokens, incluidos los reserved
#10, "hola", seran 1 token cada uno
#10 , "hola", seran token NUMBER, STRING
tokens = [
    "ID",
    "NUMBER",
    "STRING",
    # operadores
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "DIVIDE",
    "NOT",
    "AND",
    "OR",    
    "LT",
    "GT",
    "LE",
    "GE",
    "EQ",
    "NE",
    # delimitadores
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "COMMA",
    "LBRACKET",
    "RBRACKET",
    "COLON",
    #otros
    "COMMENT",
] + list(reserved.values())
