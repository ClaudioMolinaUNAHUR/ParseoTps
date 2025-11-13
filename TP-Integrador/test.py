def test_simple():
    code = """
    num x: 10
    2 + x
    console(x)
    """
    return ("simple", code)


def test_main_program():
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
    return ("Programa Principal", code)


def test_loop():
    code = """
    loop(i in range(0, 5, 2)) { 
        console("x" + i) 
    }
    """
    return ("Bucle", code)


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
    return ("Variables y Primitivas", code)


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
    return ("Lista", code)


def test_list_actions():
    code = """    
    list<num> lista: [1, 2, 3, 4, 5]
    
    add(lista, 6)
    remove(lista)
    console(size(lista), lista)
    """
    return ("Acciones de Lista", code)


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
    return ("If/Else", code)


def test_sintaxis_error():
    codes = {
        "Mala declaracion": "[num x: 10]",
        "error de asignacion": "str x: <=",
        "error de for": 'for (x > 0) { result: "true" } else { result: "falso" }',
        "error en parentesis console": "console)()",
        "error en expresion": "+ 10",
        "error en id": "if",
    }
    err_tests = []
    for i, code in codes.items():
        err_tests.append((i, code))
    return err_tests
