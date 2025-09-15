import os
import sys
from scanner.scanner import lexer
from parser.parser import parser
from interpreter import Interpreter
# from utils.helpers import parse_json # Unused import

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def run_test(name, code):
    print(f"--- Running test: {name} ---")

    full_code = f"#start\n{code}\n#end"

    lexer.input(full_code)
    result = parser.parse(full_code, lexer=lexer)
    print("AST:", result)

    interpreter = Interpreter()
    interpreter.execute(result)

    print(f"--- Finished test: {name} ---\n")


def test_main_program():
    """Tests the main example program."""
    code = """
    list<str> productos: []
    list<num> precios: []
    list<bool> comprado: []

    // funcion de agregar un producto al carrito con precio determinado -/
    func agregar(str nombre, num precio) {
        add(productos, nombre)
        add(precios, precio)
        add(comprado, false)
    }

    // Se agregan 2 productos al carrito -/
    agregar("Pan", 120)
    agregar("Leche", 250)

    // funcion para realizar la compra de 1 producto -/
    func comprar(num indice) {
        comprado[indice]: true
    }

    comprar(0)   // Marca Pan como comprado -/

    func total(): num {
        num suma: 0
        loop(i in range(0, size(precios))) {
            suma: suma + precios[i]
        }
        return suma
    }

    console(total()) // Mostrar precio Total -/

    // comprar todos los productos -/
    loop(i in range(0, size(precios))) {
        comprar(i)
        console("comprando item" + i)
    }
    """
    run_test("Main Program", code)


def test_loop():
    code = """
    loop(i in range(0, 2, 1)) { 
        console("x" + i) 
    }
    """
    run_test("Loop", code)


def test_var_primitive():
    code = """
    num x: 1
    str y: "hola"
    bool z: true
    
    x: x + 1
    y: y + " mundo"
    z: false     
    console(x, y, z)
    """
    run_test("Variables and Primitives", code)


def test_list():
    code = """    
    list<num> listaA: [1, 2, 3, 4, 5]
    list<str> listaB: ["a", "b", "c", "d", "e"]
    list<bool> listaC: [true, true, false, true, false]
    
    listaA[0]: 10
    listaB[1]: "z"
    listaC[2]: false
    console(listaA, listaB, listaC)
    """
    run_test("List", code)


def test_list_actions():
    code = """    
    list<num> lista: [1, 2, 3, 4, 5]
    
    add(lista, 6)
    remove(lista)
    console(size(lista), lista)
    """
    run_test("List Actions", code)


def test_if_else():
    code = """
    num x: 10
    str result: ""
    if (x > 0) { result: "true" } else { result: "falso" }
    console(result)
    if (x == 0) { result: "verdadero" } else {result:  "falso" }
    console(result)
    console(!true)
    """
    run_test("If/Else", code)


def main():
    # You can run all tests
    test_main_program()
    test_loop()
    test_var_primitive()
    test_list()
    test_list_actions()
    test_if_else()

    # Or comment out the above and run a specific test for more focused debugging
    # print("--- Running a single test ---")
    # test_loop()


if __name__ == "__main__":
    main()
