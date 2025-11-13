import os
import sys
from scanner.scanner import lexer
from parser.parser import parser
from interpreter import Interpreter
from utils.helpers import to_json
from test import *

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def run_test(name, code):
    print(f"--- Ejecutando prueba: {name} ---")

    full_code = f"#start\n{code}\n#end"

    lexer.input(full_code)
    print(f"--- Imprimir Tokens: {name} ---")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    try:
        result = parser.parse(full_code, lexer=lexer)
        print("AST generado")
        print(result)
        print(to_json(result))
        print("FIN AST")
        # Si el AST es None, la interpretación falla
        if result:
            interpreter = Interpreter()
            interpreter.execute(result)
        elif name != "ERRORS":
            print("El parsing falló y no se generó un AST.")
    except SyntaxError:
        if name == "ERRORS":
            print("Prueba exitosa: Se capturó un error de sintaxis como se esperaba.")
        else:
            print(
                f"Error: Se encontró un error de sintaxis inesperado en la prueba '{name}'."
            )
    print(f"--- Prueba finalizada: {name} ---\n")


def main():
    tests = [
        test_simple,
        test_main_program,
        test_loop,
        test_var_primitive,
        test_list,
        test_list_actions,
        test_if_else,
    ]
    for test in tests:
        tuple = test()
        if tuple is None:
            continue
        name = tuple[0]
        code = tuple[1]
        run_test(name, code)

    print(f"--- Manejo de Errores ---\n")

    err_tests = test_sintaxis_error()
    for err_test in err_tests:
        if err_test is None:
            continue
        name = err_test[0]
        code = err_test[1]
        run_test(name, code)


if __name__ == "__main__":
    main()
