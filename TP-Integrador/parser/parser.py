
import ply.yacc as yacc
from scanner.addons.tokens import tokens

precedence = (
    ('right', 'ELSE'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('nonassoc', 'EQ', 'NE', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)
#p[0] es el axioma de la gramatica
#p[1] - p[n] son los simbolos, terminales y no terminales, que componen la produccion
#las que estan en MAYUS, son terminales (tokens)
#las que estan en minus, son no terminales (producciones)
#<prog>::= #start <content> #end
#ID puede ser confuso pero es un token, terminal que esta compuesto por letras, ya reconocidas por el lexer
def p_program(p):
    '''program : START content END'''
    p[0] = ('program', p[2])
    
#<content> ::= <statement_list>
def p_content(p):
    '''content : statement_list'''
    p[0] = p[1]
    
#<statement_list> ::= <statement> <statement_list> | <empty>
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    if len(p) == 2: # empty
        p[0] = []
    else: # statement_list statement
        p[0] = p[1] + [p[2]]
        
#<statement> ::= <content_no_return> | <exp>
def p_statement(p):
    '''statement : content_no_return
                 | exp'''
    p[0] = p[1]
    
#<content_no_return> ::= <function> 
#                       | <loop> 
#                       | <conditional> 
#                       | <var> 
#                       | <assign> 
#                       | <list_assign> 
#                       | <comment> 
#                       | <add_list_item> 
#                       | <console>
def p_content_no_return(p):
    '''content_no_return : function
                         | function_return
                         | loop
                         | conditional
                         | var
                         | assign
                         | list_assign
                         | add_list_item
                         | console'''
    p[0] = p[1]
    
#<console>::= console(<args>)
def p_console(p):
    '''console : CONSOLE LPAREN args RPAREN'''
    p[0] = ('console', p[3])

def p_error(p):
    """Special rule for syntax errors. Tries to print context."""
    if p:
        message = f"Error de sintaxis en el token '{p.value}' (tipo: {p.type}) en la línea {p.lineno}"
        print(message)
    else:
        message = "Error de sintaxis al final del archivo (EOF)"
        print(message)
    # Para evitar que el parser se cuelgue con errores de sintaxis, es mejor detener la ejecución.
    # Lanzar una excepción es una forma simple y efectiva de lograrlo.
    raise SyntaxError(message)
#<function>::= func <id>(<param>) {<content>} | func <id>() {<content>}
def p_function(p):
    '''function : FUNC ID LPAREN opt_param_list RPAREN LBRACE content RBRACE'''
    p[0] = ('function', p[2], p[4], p[7])

#<function_return>::= func <id> (<param>) : <type> { <content> return <content_return> } 
#                   | func <id> () : <type> { <content> return <content_return> }
def p_function_return(p):
    '''function_return : FUNC ID LPAREN opt_param_list RPAREN COLON type LBRACE content RETURN exp RBRACE'''
    p[0] = ('function_return', p[2], p[4], p[7], p[9], p[11])
#<opt_param_list> ::= <param_list> | <empty>     
def p_opt_param_list(p):
    '''opt_param_list : param_list
                      | empty'''
    p[0] = p[1] or []

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_param(p):
    '''param : type ID opt_default'''
    p[0] = ('param', p[1], p[2], p[3])
        
def p_opt_default(p):
    '''opt_default : COLON exp
                   | empty'''
    p[0] = p[2] if len(p) == 3 else None
    
#<call_func>::= <id>(<args>) | <id>()
def p_call_func(p):
    '''call_func : ID LPAREN args RPAREN
                 | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = ('call_func', p[1], p[3])
    else:
        p[0] = ('call_func', p[1], [])

#<conditional>::= if ( <content_return> ) { <content> } 
#               | if ( <content_return> ) { <content> } else { <content> } 
#               | if ( <content_return> ) { <content> } else <conditional>
def p_conditional(p):
    '''conditional : IF LPAREN exp RPAREN LBRACE content RBRACE
                   | IF LPAREN exp RPAREN LBRACE content RBRACE ELSE LBRACE content RBRACE
                   | IF LPAREN exp RPAREN LBRACE content RBRACE ELSE conditional'''
    if len(p) == 8: # if without else
        p[0] = ('conditional', p[3], p[6])
    elif len(p) == 12: # if ... else { ... }
        p[0] = ('conditional', p[3], p[6], p[10])
    elif len(p) == 10: # if ... else if ...
        p[0] = ('conditional', p[3], p[6], p[8])

#<loop>::= loop ( <id> in <range>) { <content> }
def p_loop(p):
    '''loop : LOOP LPAREN ID IN range RPAREN LBRACE content RBRACE'''
    p[0] = ('loop', p[3], p[5], p[8])


#<range>:: = range(<number>, <number>) 
#          | range(<number>) 
#          | range(<number>, <number>, <number>)
def p_range(p):
    '''range : RANGE LPAREN exp COMMA exp RPAREN
             | RANGE LPAREN exp RPAREN
             | RANGE LPAREN exp COMMA exp COMMA exp RPAREN'''
    if len(p) == 5:
        p[0] = ('range', p[3])
    elif len(p) == 7:
        p[0] = ('range', p[3], p[5])
    else:
        p[0] = ('range', p[3], p[5], p[7])
        
#<exp> ::= <exp> <operator> <exp>
#        | <op_bool_un> <exp>
#        | <primary_exp>
def p_exp(p):
    '''exp : exp operator exp
           | op_bool_un exp
           | primary_exp'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = ('unary_op', p[1], p[2])
    else:
        p[0] = ('binary_op', p[1], p[2], p[3])
#<primary_exp> ::= <function_return>
#                | <error>
#                | <call_func>
#                | <primitive>
#                | <id>
#                | <len_list_item>
#                | <remove_list_item>
#                | <read_list_item>
#                | <has_list_item>
#                | <list>
#                | ( <exp> )
def p_primary_exp(p):
    '''primary_exp : call_func
                   | primitive
                   | id
                   | len_list_item
                   | remove_list_item
                   | read_list_item
                   | has_list_item
                   | list
                   | LPAREN exp RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else: # Parentheses
        p[0] = p[2]

#<var>::= <type> <id>: <content_return>
def p_var(p):
    '''var : type ID COLON exp'''
    p[0] = ('var', p[1], p[2], p[4])
    
#<assign>::= <id>: <content_return>
def p_assign(p):
    '''assign : ID COLON exp'''
    p[0] = ('assign', p[1], p[3])

#<args>::= <content_return>,<args> | <content_return>
def p_args(p):
    '''args : args COMMA exp
            | exp'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

#<id>::= <letter> <id> | <letter>
def p_id(p):
    '''id : ID'''
    p[0] = ('id', p[1])

#<operator> ::= <op_arit> | <op_bool_bin> | <op_comp>
#<op_arit> ::= + | - | * | /
#<op_bool_bin>::= & | `|`
#<op_comp>::= < | > | <= | >= | == | !=
def p_operator(p):
    '''operator : PLUS
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
                | NE'''
    p[0] = p[1]

#<op_bool_un>::= !
def p_op_bool_un(p):
    '''op_bool_un : NOT'''
    p[0] = p[1]
    
#<type> ::= str | number | boolean | list<<list_type>>
def p_type(p):
    '''type : STR
            | NUM
            | BOOL
            | LIST LT type GT'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('list_type', p[3])

# ACCIONES DE LISTAS
#<list>::= [<list_content>] | []
def p_list(p):
    '''list : LBRACKET list_content RBRACKET
            | LBRACKET RBRACKET'''
    if len(p) == 4:
        p[0] = ('list', p[2])
    else:
        p[0] = ('list', [])
#<list_content>::= <content_return>,<list_content> | <content_return>
def p_list_content(p):
    '''list_content : list_content COMMA exp
                    | exp'''
    if len(p) == 2: # exp
        p[0] = [p[1]]
    else: # list_content COMMA exp
        p[0] = p[1] + [p[3]]
#<add_list_item>::= add(<id>, <primitive>) | add(<list>, <primitive>)
def p_add_list_item(p):
    '''add_list_item : ADD LPAREN exp COMMA exp RPAREN'''
    p[0] = ('add', p[3], p[5])
#<len_list_item>::= size(<id>) | size(<list>)
def p_len_list_item(p):
    '''len_list_item : SIZE LPAREN exp RPAREN'''
    p[0] = ('len_list_item', p[3])
    
#<read_list_item>::= <id>[<number>] | <list>[<number>]  
def p_read_list_item(p):
    '''read_list_item : id LBRACKET exp RBRACKET'''
    p[0] = ('read_list_item', p[1], p[3])
#<remove_list_item>::= remove(<id>) | remove(<list>)
def p_remove_list_item(p):
    '''remove_list_item : REMOVE LPAREN exp RPAREN'''
    p[0] = ('remove_list_item', p[3])
#<has_list_item>::= has(<id>, <primitive>) | has(<list>, <primitive>)
def p_has_list_item(p):
    '''has_list_item : HAS LPAREN exp COMMA primitive RPAREN'''
    p[0] = ('has_list_item', p[3], p[5])
#<list_assign>::= <id>[<number>] : <exp>
def p_list_assign(p):
    '''list_assign : id LBRACKET exp RBRACKET COLON exp'''
    p[0] = ('list_assign', p[1], p[3], p[6])
    
#<primitive> ::= <number> | <boolean> | <string>
def p_primitive(p):
    '''primitive : NUMBER
                 | STRING
                 | TRUE
                 | FALSE'''
    token_type = p.slice[1].type
    if token_type in ('TRUE', 'FALSE'):
        p[0] = ('boolean', p[1] == 'true')
    else: # NUMBER, STRING
        p[0] = ('primitive', p[1])
    
#<empty>::= λ
def p_empty(p):
    '''empty :'''
    pass




# Construir el parser
parser = yacc.yacc(debug=True)