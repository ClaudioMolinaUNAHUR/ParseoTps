## Beta

## Objetivo

El lenguaje Beta está diseñado con un fin didáctico: aprender las nociones fundamentales de los lenguajes de programación estructurados y fuertemente tipados, sin necesidad de enfrentarse a toda la complejidad de un lenguaje real como C, Java o Python.

Se eligió un dominio “matemático y de manejo de listas” porque es un terreno común en las primeras etapas de la enseñanza de algoritmos: trabajar con listas de datos (números, cadenas, valores lógicos) y aplicar sobre ellas operaciones de filtrado, recorridos con bucles, condiciones y funciones recursivas.

De este modo, Beta está pensado como un lenguaje de laboratorio para:

- Aprender estructuras de control (if, loop).
- Modelar datos simples (num, str, bool).
- Manipular colecciones (list<tipo>).
- Abstraer soluciones en funciones propias o personalizadas.
- Familiarizarse con los conceptos de ámbitos, retorno de funciones y recursión.

## Alcance

Solo maneja listas, numeros reales, booleanos y cadenas de textos,
Puede hacer operacioones logicas, arimeticas y de comparacion
los condicionales manejan : if, else if, else
funciones propias y funciones personalizadas
puede ser recursivo

## Especificaciones Léxicas

- **Identificadores**

  - Solo letras `(a-z | A-Z)+`
  - Case sensitive (`Name` ≠ `name`)

- **Palabras reservadas**  
  str, num, bool, func, return, if, else, loop, in, range, console,
  true, false, #start, #end

- **Números**
- Reales con o sin signo: `10.0`, `-5`, `3.558`
- No se permiten decimales

- **Listas**
- listas con tipos especificos: `[true, true, false]`, `["", "hola"]`, `[0]`

- **Cadenas (string)**
- `"..."` o `'...'`
- Admiten letras y espacios
- Ejemplo: `"Hola mundo"`

- **Operadores**
- Aritméticos: `+ - * /`
- Lógicos: `& | !`
- Comparación: `< > <= >= == !=`
- Asignación: `:`

- **Delimitadores**
- Paréntesis `()`, llaves `{}`, comas `,`

---

## Especificaciones Sintácticas

- **Programa**  
  #start
  `<content>`
  #end

- **Declaración de variable**  
  `<tipo> <id>: <exp>`

- - Ejemplo:

```
num x: 10
```

- **Asignación**  
  `<id>: <exp>`
- - Ejemplo:

```
x: 20
```

- **Expresiones**
- Pueden ser literales, identificadores, operaciones o llamadas a funciones.
- Ejemplos:

```
1 + 2
true & false
"abc" / true
```

- **Condicionales**

```
if (<expr>) { <content> }
if (<expr>) { <content> } else { <content> }
```

- - Ejemplo:

```
if(x > 0) {
  console("positivo")
} else {
  console("negativo")
}
```

- **Bucles**

```
loop(i in range(0, 5)) { console(i) }
```

- **Funciones**  
  Con o sin retorno:

```
func f(num a, num b: 5) { <content> }

func g(str x): num { return 1 }
```

- **Llamada a función**

```
f(10, 20)
```

---

# BNF

```bnf
<prog> ::= #start <content> #end

<content> ::= <statement_list>
<statement_list> ::= <statement> <statement_list> | <empty>
<statement> ::= <content_no_return> | <exp>

<content_no_return> ::= <function> | <loop> | <conditional> | <var> | <assign> | <list_assign> | <comment> | <add_list_item> | <console>

<console> ::= console(<args>)
<error> ::= error(<string>)

<function> ::= func <id> ( <opt_param_list> ) { <content> }
<function_return> ::= func <id> ( <opt_param_list> ) : <type> { <content> return <exp> }

<opt_param_list> ::= <param_list> | <empty>
<param_list> ::= <param> | <param_list> , <param>
<param> ::= <type> <id> <opt_default>
<opt_default> ::= : <exp> | <empty>

<call_func> ::= <id>(<args>) | <id>()

<conditional> ::= if ( <exp> ) { <content> }
                | if ( <exp> ) { <content> } else { <content> }
                | if ( <exp> ) { <content> } else <conditional>

<loop> ::= loop ( <id> in <range> ) { <content> }
<range> ::= range(<exp>) | range(<exp>, <exp>) | range(<exp>, <exp>, <exp>)

<exp> ::= <exp> <operator> <exp>
        | <op_bool_un> <exp>
        | <primary_exp>

<primary_exp> ::= <function_return>
                | <error>
                | <call_func>
                | <primitive>
                | <id>
                | <len_list_item>
                | <remove_list_item>
                | <read_list_item>
                | <has_list_item>
                | <list>
                | ( <exp> )
<empty>::= λ
<var> ::= <type> <id>: <exp>
<assign> ::= <id>: <exp>
<args> ::= <exp> | <exp> , <args>
<id> ::= <letter> <id> | <letter>

<comment> ::= //<str_content>-/
<string> ::= "<str_content>" | '<str_content>' | "" | ''
<str_content> ::= <number> <str_content> | <number> | <letter> <str_content> | <letter> | ` ` <str_content> | ` `

<list> ::= [ <list_content> ] | []
<list_content> ::= <exp> | <exp> , <list_content>
<add_list_item> ::= add( <id> | <list> , <exp> )
<len_list_item> ::= size( <id> | <list> )
<remove_list_item> ::= remove( <id> | <list> )
<has_list_item> ::= has( <id> | <list> , <primitive> )
<read_list_item> ::=  <id>[ <exp> ] | <list>[ <exp> ]
<list_assign> ::= <id>[ <exp> ] : <exp> | <list>[ <exp> ] : <exp>

<type> ::= str | num | bool | list< <type> >
<primitive> ::= <number> | <boolean> | <string>
<operator> ::= <op_arit> | <op_bool_bin> | <op_comp>
<number> ::= <number_content> | -<number_content>
<number_content> ::= <int> <number_content> | <int> | .<decimal>
<decimal> ::= <int> <decimal> | <int>
<op_arit> ::= + | - | * | /
<op_bool_bin>::= & | `|`
<op_bool_un>::= !
<op_comp>::= < | > | <= | >= | == | !=
<boolean>::= true | false
<letter>::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z
<int>::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

# Operaciones posibles entre expresiónes

| Operación     | Ejemplo            | Resultado                                                           | Tipo   |
| ------------- | ------------------ | ------------------------------------------------------------------- | ------ |
| `bool == num` | `true == 1`        | `true` (porque `true` ≡ 1, `false` ≡ 0)                             | `bool` |
| `str + num`   | `"hola" + 1`       | `"hola1"`                                                           | `str`  |
| `str + bool`  | `"hola" + true`    | `"holatrue"` o `"hola1"` (según si querés stringify o numeric cast) | `str`  |
| `num + str`   | `1 + "hola"`       | `"1hola"`                                                           | `str`  |
| `bool + str`  | `true + "hola"`    | `"truehola"` o `"1hola"`                                            | `str`  |
| `str * num`   | `"hi" * 3`         | `"hihihi"`                                                          | `str`  |
| `str * 0`     | `"hi" * 0`         | `""`                                                                | `str`  |
| `num * bool`  | `5 * true`         | `5`                                                                 | `num`  |
| `num * false` | `5 * false`        | `0`                                                                 | `num`  |
| `str / num`   | `"abc" / 2`        | ❌ Error (posible división dispareja)                               | -      |
| `num / bool`  | `5 / true`         | `5`                                                                 | `num`  |
| `num / false` | `5 / false`        | ❌ Error (división por cero)                                        | -      |
| `str == str`  | `"hola" == "hola"` | `true`                                                              | `bool` |
| `str == num`  | `"1" == 1`         | `false`                                                             | `bool` |

## Especificaciones Semánticas

1. **Variables**

- Deben declararse con tipo explícito.
- Siempre deben inicializarse.
- No existe inferencia de tipos.

2. **Asignación**

- La expresión debe devolver un valor compatible con el tipo de la variable.
- Ejemplo válido:
  ```
  num x: 1 + 2
  ```
- Ejemplo inválido:
  ```
  name: funcionSinReturn()
  ```

3. **Tipos**

- Tipado estático y fuerte:
  - `num` → enteros o decimales
  - `str` → cadenas
  - `bool` → `true` o `false`

4. **Control de flujo**

- `if` evalúa expresiones y ejecuta bloques.
- `loop` itera sobre un rango ascendente o descendente.

5. **Funciones**

- Parámetros con valores por defecto opcionales.
- Pasaje de parámetros por valor.
- Si la función declara tipo de retorno, debe terminar con `return <expr>`.

EJEMPLOS:
Se desea tener un sistema de gestión de compras

```

#start

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
}

#end
```

6. **Ámbito**

- Variables son locales al bloque `{}`.
- Funciones crean su propio ámbito.

7. **Ejecución**

- Modelo secuencial, determinista.
- No hay concurrencia ni manejo de errores.

# Análisis Sintáctico Descendente (ASD) por izquierda

Ejemplo al derivar la cadena

```
#start
  loop ( i in range(3) ) {
   console(i)
  }
#end
```

| cadena de derivacion                                        | proxima produccion                       |
| ----------------------------------------------------------- | ---------------------------------------- |
| prog                                                        | prog -> #start content #end              |
| #start content #end                                         | content -> statement_list                |
| #start statement_list #end                                  | statement_list -> statement              |
| #start statement #end                                       | statement -> content_no_return           |
| #start content_no_return #end                               | content_no_return -> loop                |
| #start loop #end                                            | loop -> loop ( id in range ) { content } |
| #start loop ( id in range ) { content } #end                | id -> i                                  |
| #start loop ( i in range ) { content } #end                 | range -> range(exp)                      |
| #start loop ( i in range(exp) ) { content } #end            | exp -> primary_exp                       |
| #start loop ( i in range(primary_exp) ) { content } #end    | primary_exp -> primitive                 |
| #start loop ( i in range(primitive) ) { content } #end      | primitive -> number                      |
| #start loop ( i in range(number) ) { content } #end         | number -> number_content                 |
| #start loop ( i in range(number_content) ) { content } #end | number_content -> int                    |
| #start loop ( i in range(int) ) { content } #end            | int -> 3                                 |
| #start loop ( i in range(3) ) { statement_list } #end       | content -> statement_list                |
| #start loop ( i in range(3) ) { statement } #end            | statement_list -> statement              |
| #start loop ( i in range(3) ) { content_no_return } #end    | statement -> content_no_return           |
| #start loop ( i in range(3) ) { console } #end              | content_no_return -> console             |
| #start loop ( i in range(3) ) { console(args) } #end        | console -> console(args)                 |
| #start loop ( i in range(3) ) { console(exp) } #end         | args -> exp                              |
| #start loop ( i in range(3) ) { console(id) } #end          | exp -> id                                |
| #start loop ( i in range(3) ) { console(i) } #end           | id -> i                                  |
| #start loop ( i in range(3) ) { console(i) } #end           | accept                                   |

# Análisis Sintáctico Ascendente (ASA) por derecha

Ejemplo al derivar la cadena

```
#start
  loop ( i in range(3) ) {
   console(i)
  }
#end
```

Derivacion por derecha

| cadena de derivacion                                         | proxima produccion                       |
| ------------------------------------------------------------ | ---------------------------------------- |
| program                                                      | program -> #start content #end           |
| #start content #end                                          | content -> statement_list                |
| #start statement_list #end                                   | statement_list -> statement              |
| #start statement #end                                        | statement -> content_no_return           |
| #start content_no_return #end                                | content_no_return -> loop                |
| #start loop #end                                             | loop -> loop ( id in range ) { content } |
| #start loop ( id in range ) { content } #end                 | content -> statement_list                |
| #start loop ( id in range ) { statement_list } #end          | statement_list -> statement              |
| #start loop ( id in range ) { statement } #end               | statement -> content_no_return           |
| #start loop ( id in range ) { content_no_return } #end       | content_no_return -> console             |
| #start loop ( id in range ) { console } #end                 | console -> console(args)                 |
| #start loop ( id in range ) { console(args) } #end           | args -> exp                              |
| #start loop ( id in range ) { console(exp) } #end            | exp -> primary_exp                       |
| #start loop ( id in range ) { console(primary_exp) } #end    | primary_exp -> id                        |
| #start loop ( id in range ) { console(id) } #end             | id -> i                                  |
| #start loop ( id in range ) { console(i) } #end              | range -> range(exp)                      |
| #start loop ( id in range(exp) ) { console(i) } #end         | exp -> primary_exp                       |
| #start loop ( id in range(primary_exp) ) { console(i) } #end | primary_exp -> primitive                 |
| #start loop ( id in range(primitive) ) { console(i) } #end   | primitive -> 3                           |
| #start loop ( id in range(3) ) { console(i) } #end           | id -> i                                  |
| #start loop ( i in range(3) ) { console(i) } #end            | accept                                   |

Orden Inverso a la derivación por derecha

| cadena de derivacion                                        | proxima produccion                       |
| ----------------------------------------------------------- | ---------------------------------------- |
| #start loop ( i in range(3) ) { console(i) } #end           | id -> i                                  |
| #start loop ( i in range(3) ) { console(id) } #end          | primary_exp -> id                        |
| #start loop ( i in range(3) ) { console(primary_exp) } #end | exp -> primary_exp                       |
| #start loop ( i in range(3) ) { console(exp) } #end         | args -> exp                              |
| #start loop ( i in range(3) ) { console(args) } #end        | console -> console(args)                 |
| #start loop ( i in range(3) ) { console } #end              | content_no_return -> console             |
| #start loop ( i in range(3) ) { content_no_return } #end    | statement -> content_no_return           |
| #start loop ( i in range(3) ) { statement } #end            | statement_list -> statement              |
| #start loop ( i in range(3) ) { statement_list } #end       | content -> statement_list                |
| #start loop ( i in range(3) ) { content } #end              | primitive -> 3                           |
| #start loop ( i in range(primitive) ) { content } #end      | primary_exp -> primitive                 |
| #start loop ( i in range(primary_exp) ) { content } #end    | exp -> primary_exp                       |
| #start loop ( i in range(exp) ) { content } #end            | range -> range(exp)                      |
| #start loop ( i in range ) { content } #end                 | id -> i                                  |
| #start loop ( id in range ) { content } #end                | loop -> loop ( id in range ) { content } |
| #start loop #end                                            | content_no_return -> loop                |
| #start content_no_return #end                               | statement -> content_no_return           |
| #start statement #end                                       | statement_list -> statement              |
| #start statement_list #end                                  | content -> statement_list                |
| #start content #end                                         | prog -> #start content #end              |
| prog                                                        | accept                                   |
