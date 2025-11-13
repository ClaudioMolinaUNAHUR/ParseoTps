import ply.yacc as yacc
from scanner.addons.tokens import tokens
from ast_nodes import (
    RootNode,
    VarNode,
    AssignNode,
    BinaryOpNode,
    UnaryOpNode,
    PrimitiveNode,
    IdNode,
    ListNode,
    ConsoleNode,
    FunctionNode,
    FunctionReturnNode,
    ParamNode,
    CallFuncNode,
    ConditionalNode,
    LoopNode,
    RangeNode,
    ReadListItemNode,
    ListAssignNode,
    AddListItemNode,
    RemoveListItemNode,
    LenListItemNode,
    HasListItemNode,
)

precedence = (
    ("right", "ELSE"),
    ("left", "OR"),
    ("left", "AND"),
    ("right", "NOT"),
    ("nonassoc", "EQ", "NE", "LT", "LE", "GT", "GE"),
    ("left", "PLUS", "MINUS"),
    ("left", "MULTIPLY", "DIVIDE"),
)


# <prog> ::= #start <content> #end
def p_program(p):
    """program : START content END"""
    p[0] = RootNode(p[2])


# <content> ::= <statement_list>
def p_content(p):
    """content : statement_list"""
    p[0] = p[1]


# <statement_list> ::= <statement> <statement_list>
#                   | <empty>
def p_statement_list(p):
    """statement_list : statement_list statement
    | empty"""
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]


# <statement> ::= <content_no_return> | <exp>
def p_statement(p):
    """statement : content_no_return
    | exp"""
    p[0] = p[1]


# <content_no_return> ::= <function>
#                       | <loop>
#                       | <conditional>
#                       | <var>
#                       | <assign>
#                       | <list_assign>
#                       | <comment>
#                       | <add_list_item>
#                       | <console>
def p_content_no_return(p):
    """content_no_return : function
    | function_return
    | loop
    | conditional
    | var
    | assign
    | list_assign
    | add_list_item
    | console"""
    p[0] = p[1]


# <console> ::= console(<args>)
def p_console(p):
    """console : CONSOLE LPAREN args RPAREN"""
    p[0] = ConsoleNode(p[3])


# <error> ::= error(<string>)
def p_error(p):
    if p:
        message = f"Error de sintaxis en el token '{p.value}' (tipo: {p.type}) en la línea {p.lineno}"
        print(message)
    else:
        message = "Error de sintaxis al final del archivo (EOF)"
        print(message)
    raise SyntaxError(message)


# <function> ::= func <id> ( <opt_param_list> ) { <content> }
def p_function(p):
    """function : FUNC ID LPAREN opt_param_list RPAREN LBRACE content RBRACE"""
    p[0] = FunctionNode(name=p[2], params=p[4], body=p[7])


# <function_return> ::= func <id> ( <opt_param_list> ) : <type> { <content> return <exp> }
def p_function_return(p):
    """function_return : FUNC ID LPAREN opt_param_list RPAREN COLON type LBRACE content RETURN exp RBRACE"""
    p[0] = FunctionReturnNode(
        name=p[2], params=p[4], return_type=p[7], body=p[9], return_expr=p[11]
    )


# <opt_param_list> ::= <param_list>
#                   | <empty>
def p_opt_param_list(p):
    """opt_param_list : param_list
    | empty"""
    p[0] = p[1] or []


# <param_list> ::= <param>
#               | <param_list> , <param>
def p_param_list(p):
    """param_list : param_list COMMA param
    | param"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


# <param> ::= <type> <id> <opt_default>
def p_param(p):
    """param : type ID opt_default"""
    p[0] = ParamNode(param_type=p[1], name=p[2], default_value=p[3])


# <opt_default> ::= : <exp>
#                   | <empty>
def p_opt_default(p):
    """opt_default : COLON exp
    | empty"""
    p[0] = p[2] if len(p) == 3 else None


# <call_func> ::= <id>(<args>) | <id>()
def p_call_func(p):
    """call_func : ID LPAREN args RPAREN
    | ID LPAREN RPAREN"""
    if len(p) == 5:
        p[0] = CallFuncNode(name=p[1], args=p[3])
    else:
        p[0] = CallFuncNode(name=p[1], args=[])


# <conditional> ::= if ( <exp> ) { <content> }
#                | if ( <exp> ) { <content> } else { <content> }
#                | if ( <exp> ) { <content> } else <conditional>
def p_conditional(p):
    """conditional : IF LPAREN exp RPAREN LBRACE content RBRACE
    | IF LPAREN exp RPAREN LBRACE content RBRACE ELSE LBRACE content RBRACE
    | IF LPAREN exp RPAREN LBRACE content RBRACE ELSE conditional"""
    if len(p) == 8:
        p[0] = ConditionalNode(condition=p[3], if_block=RootNode(p[6]))
    else:
        # Handle both `else { ... }` and `else if ...`
        else_block = RootNode(p[10]) if len(p) == 12 else p[8]
        p[0] = ConditionalNode(
            condition=p[3], if_block=RootNode(p[6]), else_block=else_block
        )


# <loop> ::= loop ( <id> in <range> ) { <content> }
def p_loop(p):
    """loop : LOOP LPAREN ID IN range RPAREN LBRACE content RBRACE"""
    p[0] = LoopNode(var_name=p[3], range_node=p[5], body=RootNode(p[8]))


# <range> ::= range(<exp>) | range(<exp>, <exp>) | range(<exp>, <exp>, <exp>)
def p_range(p):
    """range : RANGE LPAREN exp COMMA exp RPAREN
    | RANGE LPAREN exp RPAREN
    | RANGE LPAREN exp COMMA exp COMMA exp RPAREN"""
    if len(p) == 5:
        p[0] = RangeNode(p[3])
    elif len(p) == 7:
        p[0] = RangeNode(p[3], p[5])
    else:
        p[0] = RangeNode(p[3], p[5], p[7])


# <exp> ::= <exp> <operator> <exp>
#        | <op_bool_un> <exp>
#        | <primary_exp>
def p_exp(p):
    """exp : exp operator exp
    | op_bool_un exp
    | primary_exp"""
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = UnaryOpNode(op=p[1], expr=p[2])
    else:
        p[0] = BinaryOpNode(left=p[1], op=p[2], right=p[3])


# <primary_exp> ::= <function_return>
#                 | <error>
#                 | <call_func>
#                 | <primitive>
#                 | <id>
#                 | <len_list_item>
#                 | <remove_list_item>
#                 | <read_list_item>
#                 | <has_list_item>
#                 | <list>
#                 | ( <exp> )
def p_primary_exp(p):
    """primary_exp : call_func
    | primitive
    | id
    | len_list_item
    | remove_list_item
    | read_list_item
    | has_list_item
    | list
    | LPAREN exp RPAREN"""
    if len(p) == 2:
        p[0] = p[1]
    else:  # Parentheses
        p[0] = p[2]


# <var> ::= <type> <id>: <exp>
def p_var(p):
    """var : type ID COLON exp"""
    p[0] = VarNode(var_type=p[1], name=p[2], value_expr=p[4])


# <assign> ::= <id>: <exp>
def p_assign(p):
    """assign : ID COLON exp"""
    p[0] = AssignNode(name=p[1], value_expr=p[3])


# <args> ::= <exp>
#           | <exp> , <args>
def p_args(p):
    """args : args COMMA exp
    | exp"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


# <id> ::= <letter> <id> | <letter>
def p_id(p):
    """id : ID"""
    p[0] = IdNode(p[1])


# <operator> ::= <op_arit>
#              | <op_bool_bin>
#              | <op_comp>
def p_operator(p):
    """operator : PLUS
    | MINUS
    | MULTIPLY
    | DIVIDE
    | AND
    | OR
    | LT
    | GT
    | LE
    | GE
    | EQ
    | NE"""
    p[0] = p[1]


# <op_bool_un>::= !
def p_op_bool_un(p):
    """op_bool_un : NOT"""
    p[0] = p[1]


# <type> ::= str
#           | num
#           | bool
#           | list< <type> >
def p_type(p):
    """type : STR
    | NUM
    | BOOL
    | LIST LT type GT"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ("list_type", p[3])  # This can remain a tuple or become a simple class


# <list> ::= [ <list_content> ]
#           | []
def p_list(p):
    """list : LBRACKET list_content RBRACKET
    | LBRACKET RBRACKET"""
    if len(p) == 4:
        p[0] = ListNode(p[2])
    else:
        p[0] = ListNode([])


# <list_content> ::= <exp>
#                   | <exp> , <list_content>
def p_list_content(p):
    """list_content : list_content COMMA exp
    | exp"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


# <add_list_item> ::= add( <id> | <list> , <exp> )
def p_add_list_item(p):
    """add_list_item : ADD LPAREN exp COMMA exp RPAREN"""
    p[0] = AddListItemNode(list_expr=p[3], value_expr=p[5])


# <len_list_item> ::= size( <id> | <list> )
def p_len_list_item(p):
    """len_list_item : SIZE LPAREN exp RPAREN"""
    p[0] = LenListItemNode(p[3])


# <read_list_item> ::=  <id>[ <exp> ] | <list>[ <exp> ]
def p_read_list_item(p):
    """read_list_item : id LBRACKET exp RBRACKET"""
    p[0] = ReadListItemNode(list_node=p[1], index_expr=p[3])


# <remove_list_item> ::= remove( <id> | <list> )
def p_remove_list_item(p):
    """remove_list_item : REMOVE LPAREN exp RPAREN"""
    p[0] = RemoveListItemNode(p[3])


# <has_list_item> ::= has( <id> | <list> , <primitive> )
def p_has_list_item(p):
    """has_list_item : HAS LPAREN exp COMMA primitive RPAREN"""
    p[0] = HasListItemNode(list_expr=p[3], value_expr=p[5])


# <list_assign> ::= <id>[ <exp> ] : <exp> | <list>[ <exp> ] : <exp>
def p_list_assign(p):
    """list_assign : id LBRACKET exp RBRACKET COLON exp"""
    p[0] = ListAssignNode(list_node=p[1], index_expr=p[3], value_expr=p[6])


# <primitive> ::= <number>
#               | <boolean>
#               | <string>
def p_primitive(p):
    """primitive : NUMBER
    | STRING
    | TRUE
    | FALSE"""
    token_type = p.slice[1].type
    if token_type in ("TRUE", "FALSE"):
        p[0] = PrimitiveNode(p[1] == "true")
    else:
        p[0] = PrimitiveNode(p[1])


# <empty>::= λ
def p_empty(p):
    """empty :"""
    pass


# Build the parser
parser = yacc.yacc(debug=True)
