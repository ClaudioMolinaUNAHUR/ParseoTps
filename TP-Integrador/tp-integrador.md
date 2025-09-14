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
<prog>::= #start <content> #end
<content>::= <content_no_return> | <content_return> | <content_no_return> <content> | <content_return> <content> | (<content>) | (<content>) <content> | () | λ
<content_no_return>::= <function> |  <loop> | <conditional> | <var> | <assign> | <call_func> | <list> | <comment>
<content_return>::= <function_return> | <console> | <error> | <exp> | <call_func> | <primitive> | <id> | <len_list_item> | <remove_list_item> | <read_list_item> | <has_list_item> | <remove_list_item>
<console>::= console(<args>)
<error>::= error(<string>)

<function>::= func <id> (<param>) { <content> } | func <id> () { <content> }
<function_return>::= func <id> (<param>) : <type> { <content> return <content_return> } | func <id> () : <type> { <content> return <content_return> }
<param>::= <type> <id>,  <param> | <var>, <param> | <type> <id> | <var>

<call_func>::= <id>(<args>) | <id>()

<conditional>::= if ( <content_return> ) { <content> } | if ( <content_return> ) { <content> } else { <content> } | if ( <content_return> ) { <content> } else <conditional>

<loop>::= loop ( <id> in <range>) { <content> }
<range>:: = range(<number>, <number>) | range(<number>) | range(<number>, <number>, <number>)

<exp>::=
    <content_return> <operator> <content_return> |
    <content_return> <operator> <exp> |
    <content_return> |
    <op_bool_un> <content_return> <operator> <content_return> |
    <op_bool_un> <content_return> <operator> <exp> |
    <op_bool_un> <content_return>

<var>::= <type> <id>: <content_return>
<assign>::= <id>: <content_return>
<args>::= <content_return>,<args> | <content_return>
<id>::= <letter> <id> | <letter>

<comment>::= //<str_content>-/
<string>::= "<str_content>" | '<str_content>' | "" | ''
<str_content>::= <number> <str_content> | <number> | <letter> <str_content> | <letter> | ` ` <str_content> | ` `

<list_type>::= <type>[]
<list>::= [<list_content>] | []
<list_content>::= <content_return>,<list_content> | <content_return>
<add_list_item>::= add(<id>, <primitive>) | add(<list>, <primitive>)
<len_list_item>::= size(<id>) | size(<list>)
<remove_list_item>::= remove(<id>) | remove(<list>)
<has_list_item>::= has(<id>, <primitive>) | has(<list>, <primitive>)
<read_list_item>::= <id>[<number>] | <list>[<number>]

<type> ::= str | number | boolean | list<<list_type>>
<primitive> ::= <number> | <boolean> | <string>
<operator> ::= <op_arit> | <op_bool_bin> | <op_comp>
<number> ::= <number_content> | -<number_content>
<number_content> ::= <int> <number_content> | <int> | .<decimal>
<decimal> ::= <int> <decimal> | <int>
<type> ::= str | number | boolean
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

| cadena de derivacion                                              | proxima produccion                       |
| ----------------------------------------------------------------- | ---------------------------------------- |
| Programa                                                          | Programa -> #start Content #end          |
| #start Content #end                                               | Content -> Content_NoReturn              |
| #start Content_NoReturn #end                                      | ContentNoReturn -> Loop                  |
| #start Loop #end                                                  | Loop -> loop ( Id IN Range ) { Content } |
| #start loop ( Id IN Range ) { Content } #end                      | Id -> Letter                             |
| #start loop ( Letter IN Range ) { Content } #end                  | Letter -> i                              |
| #start loop ( i IN Range ) { Content } #end                       | Range -> range( Number )                 |
| #start loop ( i IN range( Number ) ) { Content } #end             | Number -> Int                            |
| #start loop ( i IN range( Int ) ) { Content } #end                | Int -> 3                                 |
| #start loop ( i IN range( 3 ) ) { Content } #end                  | Content -> ContentReturn                 |
| #start loop ( i IN range( 3 ) ) { ContentReturn } #end            | ContentReturn -> Console                 |
| #start loop ( i IN range( 3 ) ) { Console } #end                  | Console -> console( Args )               |
| #start loop ( i IN range( 3 ) ) { console( Args ) } #end          | Args -> ContentReturn                    |
| #start loop ( i IN range( 3 ) ) { console( ContentReturn ) } #end | ContentReturn -> Id                      |
| #start loop ( i IN range( 3 ) ) { console( Id ) } #end            | Id -> Letter                             |
| #start loop ( i IN range( 3 ) ) { console( Letter ) } #end        | Letter -> i                              |
| #start loop ( i IN range( 3 ) ) { console( i ) } #end             | accept                                   |

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
| cadena de derivacion                                          | proxima produccion                                     |
|---------------------------------------------------------------|--------------------------------------------------------|
| Programa                                                      | Programa -> #start Content #end                        |
| #start Content #end                                           | Content -> Content_NoReturn                            |
| #start Content_NoReturn #end                                  | ContentNoReturn -> Loop                                |
| #start Loop #end                                              | Loop -> loop ( Id IN Range ) { Content }               |
| #start loop ( Id IN Range ) { Content } #end                  | Content -> ContentReturn                               |
| #start loop ( Id IN Range ) { ContentReturn } #end            | ContentReturn -> Console                               |
| #start loop ( Id IN Range ) { Console } #end                  | Console -> console( Args )                             |
| #start loop ( Id IN Range ) { console( Args ) } #end          | Args -> ContentReturn                                  |
| #start loop ( Id IN Range ) { console( ContentReturn ) } #end | ContentReturn -> Id                                    |
| #start loop ( Id IN Range ) { console( Id ) } #end            | Id -> Letter                                           |
| #start loop ( Id IN Range ) { console( Letter ) } #end        | Letter -> i                                            |
| #start loop ( Id IN range( Number ) ) { console( i ) } #end   | Range -> range( Number )                               |
| #start loop ( Id IN range( Int ) ) { console( i ) } #end      | Number -> Int                                          |
| #start loop ( Id IN range( 3 ) ) { console( i ) } #end        | Int -> 3                                               |
| #start loop ( Id IN range( 3 ) ) { console( i ) } #end        | Id -> Letter                                           |
| #start loop ( Letter IN range( 3 ) ) { console( i ) } #end    | Letter -> i                                            |
| #start loop ( i IN range( 3 ) ) { console( i ) } #end         | accept                                                 |

Orden Inverso a la derivación por derecha

| cadena de derivacion                                          | proxima produccion                       |
| ------------------------------------------------------------- | ---------------------------------------- |
| #start loop ( i IN range( 3 ) ) { console( i ) } #end         | Letter -> i                              |
| #start loop ( Letter IN range( 3 ) ) { console( i ) } #end    | Id -> Letter                             |
| #start loop ( Id IN range( 3 ) ) { console( i ) } #end        | Int -> 3                                 |
| #start loop ( Id IN range( 3 ) ) { console( i ) } #end        | Number -> Int                            |
| #start loop ( Id IN range( Int ) ) { console( i ) } #end      | Range -> range( Number )                 |
| #start loop ( Id IN range( Number ) ) { console( i ) } #end   | Letter -> i                              |
| #start loop ( Id IN Range ) { console( Letter ) } #end        | Id -> Letter                             |
| #start loop ( Id IN Range ) { console( Id ) } #end            | ContentReturn -> Id                      |
| #start loop ( Id IN Range ) { console( ContentReturn ) } #end | Args -> ContentReturn                    |
| #start loop ( Id IN Range ) { console( Args ) } #end          | Console -> console( Args )               |
| #start loop ( Id IN Range ) { Console } #end                  | ContentReturn -> Console                 |
| #start loop ( Id IN Range ) { ContentReturn } #end            | Content -> ContentReturn                 |
| #start loop ( Id IN Range ) { Content } #end                  | Loop -> loop ( Id IN Range ) { Content } |
| #start Loop #end                                              | ContentNoReturn -> Loop                  |
| #start Content_NoReturn #end                                  | Content -> Content_NoReturn              |
| #start Content #end                                           | Programa -> #start Content #end          |
| Programa                                                      | accept                                   |
