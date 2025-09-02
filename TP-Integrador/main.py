import os
import sys
import json
from scanner.scanner import lexer

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def like_json(data):
    return json.dumps(data, indent=2, ensure_ascii=False)


def main():
    data = """
    #start

    list<str> productos: []
    list<num> precios: []
    list<bool> comprado: []

    // funcion de agregar un producto al carrito con precio determinado -/
    func agregar(str nombre, num precio) {
        productos.add(nombre)
        precios.add(precio)
        comprado.add(false)
    }

    // Se agregan 2 productos al carrito
    agregar("Pan", 120)
    agregar("Leche", 250)

    // funcion para realizar la compra de 1 producto -/
    func comprar(num indice) {
        comprado[indice]: true
    }

    comprar(0)   // Marca Pan como comprado -/

    func total(): num {
        num suma: 0
        loop(i in range(0, precios.size())) {
            suma: suma + precios[i]
        }
        return suma
    }

    console(total()) // Mostrar precio Total -/

    // comprar todos los productos -/
    loop(i in range(0, precios.size())) {
        comprar(i)
    }

    #end
    """

    lexer.input(data)

    for tok in lexer:
        print(tok)


if __name__ == "__main__":
    main()
