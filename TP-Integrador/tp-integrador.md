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

# TP3

## Análisis Sintáctico Descendente (ASD) por izquierda

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
| #start loop ( id in range ) { content } #end                | id -> letter                             |
| #start loop ( letter in range ) { content } #end            | letter -> i                              |
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

## Análisis Sintáctico Ascendente (ASA) por derecha

Ejemplo al derivar la cadena

```
#start
  loop ( i in range(3) ) {
   console(i)
  }
#end
```

Derivacion por derecha

| cadena de derivacion                                            | proxima produccion                       |
| --------------------------------------------------------------- | ---------------------------------------- |
| prog                                                            | prog -> #start content #end              |
| #start content #end                                             | content -> statement_list                |
| #start statement_list #end                                      | statement_list -> statement              |
| #start statement #end                                           | statement -> content_no_return           |
| #start content_no_return #end                                   | content_no_return -> loop                |
| #start loop #end                                                | loop -> loop ( id in range ) { content } |
| #start loop ( id in range ) { content } #end                    | content -> statement_list                |
| #start loop ( id in range ) { statement_list } #end             | statement_list -> statement              |
| #start loop ( id in range ) { statement } #end                  | statement -> content_no_return           |
| #start loop ( id in range ) { content_no_return } #end          | content_no_return -> console             |
| #start loop ( id in range ) { console } #end                    | console -> console(args)                 |
| #start loop ( id in range ) { console(args) } #end              | args -> exp                              |
| #start loop ( id in range ) { console(exp) } #end               | exp -> primary_exp                       |
| #start loop ( id in range ) { console(primary_exp) } #end       | primary_exp -> id                        |
| #start loop ( id in range ) { console(id) } #end                | id -> i                                  |
| #start loop ( id in range ) { console(i) } #end                 | range -> range(exp)                      |
| #start loop ( id in range(exp) ) { console(i) } #end            | exp -> primary_exp                       |
| #start loop ( id in range(primary_exp) ) { console(i) } #end    | primary_exp -> primitive                 |
| #start loop ( id in range(primitive) ) { console(i) } #end      | primitive -> number                      |
| #start loop ( id in range(number) ) { console(i) } #end         | number -> number_content                 |
| #start loop ( id in range(number_content) ) { console(i) } #end | number_content -> int                    |
| #start loop ( id in range(int) ) { console(i) } #end            | int -> 3                                 |
| #start loop ( id in range(3) ) { console(i) } #end              | id -> letter                             |
| #start loop ( letter in range(3) ) { console(i) } #end          | letter -> i                              |
| #start loop ( i in range(3) ) { console(i) } #end               | accept                                   |

Orden Inverso a la derivación por derecha

| cadena de derivacion                                            | proxima produccion                       |
| --------------------------------------------------------------- | ---------------------------------------- |
| #start loop ( i in range(3) ) { console(i) } #end               | letter -> i                              |
| #start loop ( letter in range(3) ) { console(i) } #end          | id -> letter                             |
| #start loop ( id in range(3) ) { console(i) } #end              | int -> 3                                 |
| #start loop ( id in range(int) ) { console(i) } #end            | number_content -> int                    |
| #start loop ( id in range(number_content) ) { console(i) } #end | number -> number_content                 |
| #start loop ( id in range(number) ) { console(i) } #end         | primitive -> number                      |
| #start loop ( id in range(primitive) ) { console(i) } #end      | primary_exp -> primitive                 |
| #start loop ( id in range(primary_exp) ) { console(i) } #end    | exp -> primary_exp                       |
| #start loop ( id in range(exp) ) { console(i) } #end            | range -> range(exp)                      |
| #start loop ( id in range ) { console(i) } #end                 | id -> i                                  |
| #start loop ( id in range ) { console(id) } #end                | primary_exp -> id                        |
| #start loop ( id in range ) { console(primary_exp) } #end       | exp -> primary_exp                       |
| #start loop ( id in range ) { console(exp) } #end               | args -> exp                              |
| #start loop ( id in range ) { console(args) } #end              | console -> console(args)                 |
| #start loop ( id in range ) { console } #end                    | content_no_return -> console             |
| #start loop ( id in range ) { content_no_return } #end          | statement -> content_no_return           |
| #start loop ( id in range ) { statement } #end                  | statement_list -> statement              |
| #start loop ( id in range ) { statement_list } #end             | content -> statement_list                |
| #start loop ( id in range ) { content } #end                    | loop -> loop ( id in range ) { content } |
| #start loop #end                                                | content_no_return -> loop                |
| #start content_no_return #end                                   | statement -> content_no_return           |
| #start statement #end                                           | statement_list -> statement              |
| #start statement_list #end                                      | content -> statement_list                |
| #start content #end                                             | prog -> #start content #end              |
| prog                                                            | accept                                   |

## Análisis Sintáctico Ascendente (ASD) con retroceso

```
#start
  loop ( i in range(3) ) {
   console(i)
  }
#end
```

# TP4

## Automata de Pila para ejemplo

- Pila= <ΣN, ΣT, S, P>

* ΣN = {todas las palabras de este ejemplo que empiezan con Mayus}
* ΣT ={#start, #end, loop, in, range, console, i, 3, {, }, (, )}
* S = Prog
* P = {producciones del BNF}

```
  δ(q0, λ, λ) => (q1, Z)
  δ(q1, λ, λ) => (q2, Prog)

  δ(q2, λ, Prog) => (q2, #start Content #end)
  δ(q2, λ, Content) => (q2, Statement_list)
  δ(q2, λ, Statement_list) => (q2, Statement)
  δ(q2, λ, Statement) => (q2, Content_no_return)
  δ(q2, λ, Content_no_return) => (q2, Console)
  δ(q2, λ, Content_no_return) => (q2, Loop)
  δ(q2, λ, Loop) => (q2, loop ( Id in Range ) { Content })
  δ(q2, λ, Id) => (q1, Letter)
  δ(q2, λ, Letter) => (q2, i)
  δ(q2, λ, Range) => (q2, range(Exp))
  δ(q2, λ, Exp) => (q2, Primary_exp)
  δ(q2, λ, Exp) => (q2, Id)
  δ(q2, λ, Primary_exp) => (q2, Primitive)
  δ(q2, λ, Primitive) => (q2, Number)
  δ(q2, λ, Number) => (q2, Number_content)
  δ(q2, λ, Number_content) => (q2, Int)
  δ(q2, λ, Int) => (q2, 3)
  δ(q2, λ, Console) => (q2, console(Args))
  δ(q2, λ, Args) => (q2, Exp)

  δ(q2, #start, #start) => (q2, λ)
  δ(q2, #end, #end) => (q2, λ)
  δ(q2, loop, loop) => (q2, λ)
  δ(q2, in, in) => (q2, λ)
  δ(q2, console, console) => (q2, λ)
  δ(q2, range, range) => (q2, λ)
  δ(q2, i, i) => (q2, λ)
  δ(q2, 3, 3) => (q2, λ)
  δ(q2, (, () => (q2, λ)
  δ(q2, ), )) => (q2, λ)
  δ(q2, }, }) => (q2, λ)
  δ(q2, {, {) => (q2, λ)

  δ(q2, λ, Z) => (q3, λ)
```

| Pila                                   | Cadena                                           | transicion                                              |
| -------------------------------------- | ------------------------------------------------ | ------------------------------------------------------- |
| λ                                      | #start loop ( i in range(3) ) { console(i)} #end | δ(q0, λ, λ)=> (q1, Z)                                   |
| Z                                      | #start loop ( i in range(3) ) { console(i)} #end | δ(q1, λ, λ)=> (q2, Prog)                                |
| ZProg                                  | #start loop ( i in range(3) ) { console(i)} #end | δ(q2, λ, Prog)=> (q2, #start Content #end)              |
| Z#end Content #start                   | #start loop ( i in range(3) ) { console(i)} #end | δ(q2, #start , #start)=> (q2, λ)                        |
| Z#end Content                          | loop ( i in range(3) ) { console(i)} #end        | δ(q2, λ, Content)=> (q2, Statement_list)                |
| Z#end Statement_list                   | loop ( i in range(3) ) { console(i)} #end        | δ(q2, λ, Statement_list)=> (q2, Statement)              |
| Z#end Statement                        | loop ( i in range(3) ) { console(i)} #end        | δ(q2, λ, Statement)=> (q2, Content_no_return)           |
| Z#end Content_no_return                | loop ( i in range(3) ) { console(i)} #end        | δ(q2, λ, Content_no_return)=> (q2, Loop)                |
| Z#end Loop                             | loop ( i in range(3) ) { console(i)} #end        | δ(q2, λ, Loop)=> (q2, loop ( Id in Range ) { Content }) |
| Z#end } Content { ) Range in Id ( loop | loop ( i in range(3) ) { console(i)} #end        | δ(q2, loop, loop)=> (q2, λ)                             |
| Z#end } Content { ) Range in Id (      | ( i in range(3) ) { console(i)} #end             | δ(q2, (, ()=> (q2, λ)                                   |
| Z#end } Content { ) Range in Id        | i in range(3) ) { console(i)} #end               | δ(q2, λ, Id)=> (q1, Letter)                             |
| Z#end } Content { ) Range in Letter    | i in range(3) ) { console(i)} #end               | δ(q2, λ, Letter)=> (q2, i)                              |
| Z#end } Content { ) Range in i         | i in range(3) ) { console(i)} #end               | δ(q2, i, i)=> (q2, λ)                                   |
| Z#end } Content { ) Range in           | in range(3) ) { console(i)} #end                 | δ(q2, in, in)=> (q2, λ)                                 |
| Z#end } Content { ) Range              | range(3) ) { console(i)} #end                    | δ(q2, λ, Range)=> (q2, range(Exp) )                     |
| Z#end } Content { ) ) Exp ( range      | range(3) ) { console(i)} #end                    | δ(q2, range, range)=> (q2, λ)                           |
| Z#end } Content { ) ) Exp (            | (3) ) { console(i)} #end                         | δ(q2, (, ()=> (q2, λ)                                   |
| Z#end } Content { ) ) Exp              | 3) ) { console(i)} #end                          | δ(q2, λ, Exp)=> (q2, Primary_exp )                      |
| Z#end } Content { ) ) Primary_exp      | 3) ) { console(i)} #end                          | δ(q2, λ, Primary_exp)=> (q2, Primitive )                |
| Z#end } Content { ) ) Primitive        | 3) ) { console(i)} #end                          | δ(q2, λ, Primitive)=> (q2, Number )                     |
| Z#end } Content { ) ) Number           | 3) ) { console(i)} #end                          | δ(q2, λ, Number)=> (q2, Number_content )                |
| Z#end } Content { ) ) Number_content   | 3) ) { console(i)} #end                          | δ(q2, λ, Number_content)=> (q2, Int)                    |
| Z#end } Content { ) ) Int              | 3) ) { console(i)} #end                          | δ(q2, λ, Int)=> (q2, 3)                                 |
| Z#end } Content { ) ) 3                | 3) ) { console(i)} #end                          | δ(q2, 3, 3)=> (q2, λ)                                   |
| Z#end } Content { ) )                  | ) ) { console(i)} #end                           | δ(q2, ), ))=> (q2, λ)                                   |
| Z#end } Content { )                    | ) { console(i)} #end                             | δ(q2, ), ))=> (q2, λ)                                   |
| Z#end } Content {                      | { console(i)} #end                               | δ(q2, {, {)=> (q2, λ)                                   |
| Z#end } Content                        | console(i)} #end                                 | δ(q2, λ, Content)=> (q2, Statement_list)                |
| Z#end } Statement_list                 | console(i)} #end                                 | δ(q2, λ, Statement_list)=> (q2, Statement)              |
| Z#end } Statement                      | console(i)} #end                                 | δ(q2, λ, Statement)=> (q2, Content_no_return)           |
| Z#end } Content_no_return              | console(i)} #end                                 | δ(q2, λ, Content_no_return)=> (q2, Console)             |
| Z#end } Console                        | console(i)} #end                                 | δ(q2, λ, Console)=> (q2, console(Args))                 |
| Z#end } ) Args ( console               | console(i)} #end                                 | δ(q2, console, console)=> (q2, λ)                       |
| Z#end } ) Args (                       | (i)} #end                                        | δ(q2, (, ()=> (q2, λ)                                   |
| Z#end } ) Args                         | i)} #end                                         | δ(q2, λ, Args)=> (q2, Exp)                              |
| Z#end } ) Exp                          | i)} #end                                         | δ(q2, λ, Exp)=> (q2, Id )                               |
| Z#end } ) Id                           | i)} #end                                         | δ(q2, λ, Id)=> (q1, Letter)                             |
| Z#end } ) Letter                       | i)} #end                                         | δ(q2, λ, Letter)=> (q2, i)                              |
| Z#end } )                              | )} #end                                          | δ(q2, i, i)=> (q2, λ)                                   |
| Z#end } )                              | )} #end                                          | δ(q2, ), ))=> (q2, λ)                                   |
| Z#end }                                | } #end                                           | δ(q2, }, })=> (q2, λ)                                   |
| Z#end                                  | #end                                             | δ(q2, #end, #end)=> (q2, λ)                             |
| Z                                      | λ                                                | δ(q2, λ, Z)=> (q3, λ)                                   |
| λ                                      | λ                                                | accept                                                  |

# TP 5
## Analisis LL(1)
## se reduce el BNF a un GIC mas accesible para el analisis. Las derivaciones q se sacaron se simulan con Out, OutE ( expresiones ) -> 

cadena

```
#start
  loop ( i in range(3) ) {
   console(i)
  }
#end
```

```GIC (reducido)
Prog -> #start Content #end
Content -> StatementList
StatementList -> Statement StatementList | λ
Statement -> ContentNoReturn | Exp

ContentNoReturn -> Loop | Console | Out

Console -> console(Args)

Loop -> loop ( Id in Range ) { Content }
Range -> range1(Exp) | range2(Exp, Exp) | range3(Exp, Exp, Exp)

Exp -> Primary_exp | OutE

Primary_exp -> Primitive | Id | ( Exp ) | OutE

Args -> Exp ArgsRest
ArgsRest -> , Exp ArgsRest | λ

Id -> Letter RestId
RestId -> Letter RestId | λ

Primitive -> Number | OutE
Number -> NumberContent | -NumberContent
NumberContent -> Int NumRest | OutE
NumRest -> Int NumRest | λ

Letter -> a | i
Int -> 0 | 3

OutE -> outE
Out -> out
```

| PRIM                                                                   |
| ---------------------------------------------------------------------- |
| PRIM(PROG) = { #start }                                                |
| PRIM(Content) = { loop, console, out, 0, 3, -, outE, a, i, (, λ}       |
| PRIM(StatementList) = { loop, console, out, 0, 3, -, outE, a, i, (, λ} |
| PRIM(Statement) = { loop, console, out, 0, 3, -, outE, a, i, ( }       |
| PRIM(ContentNoReturn) = { loop, console, out }                         |
| PRIM(Console) = { console }                                            |
| PRIM(Loop) = { loop }                                                  |
| PRIM(Range) = { range1, range2, range3 }                               |
| PRIM(Exp) = {0, 3, -, outE, a, i, (}                                   |
| PRIM(Primary_exp) = {0, 3, outE, a, i, (}                              |
| PRIM(Args) = {0, 3, -, outE, a, i, (}                                  |
| PRIM(ArgsRest) = {",", λ}                                              |
| PRIM(Id) = { a, i}                                                     |
| PRIM(RestId) = { a, i, λ }                                             |
| PRIM(Primitive) = { 0, 3, -}                                           |
| PRIM(Number) = { 0, 3, -}                                              |
| PRIM(NumberContent) = { 0, 3}                                          |
| PRIM(NumRest) = { 0, 3, λ}                                             |
| PRIM(Letter) = { a, i}                                                 |
| PRIM(Int) = { 0, 3 }                                                   |
| PRIM(OutE) = { outE }                                                  |
| PRIM(Out) = { out }                                                    |

| SIG                                                                    |
| ---------------------------------------------------------------------- |
| SIG(PROG) = {$, loop, console, out, 0, 3, -, outE, a, i, (, #end }     |
| SIG(Content) = { #end, } }                                             |
| SIG(StatementList) = {#end, } }                                        |
| SIG(Statement) = { loop, console, out, 0, 3, -, outE, a, i, ( }        |
| SIG(ContentNoReturn) = { loop, console, out, 0, 3, -, outE, a, i, (, } |
| SIG(Console) = { loop, console, out, 0, 3, -, outE, a, i, (, }         |
| SIG(Loop) = { loop, console, out, 0, 3, -, outE, a, i, (, }            |
| SIG(Range) = { ) { }                                                   |
| SIG(Exp) = { ), ",", }                                                 |
| SIG(Primary_exp) = { ), ",", }                                         |
| SIG(Args) = { ) }                                                      |
| SIG(ArgsRest) = { ) }                                                  |
| SIG(Id) = { in, (, -, 0, 3, outE}                                      |
| SIG(RestId) = { in, (, -, 0, 3, outE}                                  |
| SIG(Primitive) = { ), ",", }                                           |
| SIG(Number) = { ), ",", }                                              |
| SIG(NumberContent) = { ), ",", }                                       |
| SIG(NumRest) = { ), ",", }                                             |
| SIG(Int) = { ), ",", }                                                 |
| SIG(Letter) = { in, (, -, 0, 3, outE}                                  |
| SIG(OutE) = { in, (, -, 0, 3, outE}                                    |
| SIG(Out) = { ), ",", }                                                 |

| PRED                                                                                            |
| ----------------------------------------------------------------------------------------------- |
| PRED(Prog -> #start Content #end) = {#start}                                                    |
| PRED(Content -> StatementList) = { loop, console, out, 0, 3, -, outE, a, i, (, #end}            |
| PRED(StatementList -> Statement StatementList) = { loop, console, out, 0, 3, -, outE, a, i, ( } |
| PRED(StatementList -> λ) = {#end, } }                                                           |
| PRED(Statement -> ContentNoReturn) = { loop, console, out }                                     |
| PRED(Statement -> Exp) = {0, 3, -, outE, a, i, (}                                               |
| PRED(ContentNoReturn -> Loop) = { loop }                                                        |
| PRED(ContentNoReturn -> Console) = { console }                                                  |
| PRED(ContentNoReturn -> Out) = { out }                                                          |
| PRED(Console -> console(Args)) = { console }                                                    |
| PRED(Loop -> loop ( Id in Range ) { Content }) = { loop }                                       |
| PRED(Range -> range1(Exp)) = { range1 }                                                         |
| PRED(Range -> range2(Exp, Exp)) = { range2 }                                                    |
| PRED(Range -> range3(Exp, Exp, Exp)) = { range3 }                                               |
| PRED(Exp -> Primary_exp) = {0, 3, outE, a, i, (}                                                |
| PRED(Exp -> OutE) = { outE }                                                                    |
| PRED(Primary_exp -> Primitive) = {0, 3, outE, a, i, (}                                          |
| PRED(Primary_exp -> Id) = { a, i, outE}                                                         |
| PRED(Primary_exp -> ( Exp )) = { ( }                                                            |
| PRED(Primary_exp -> OutE) = { outE}                                                             |
| PRED(Args -> Exp) = {0, 3, -, outE, a, i, (}                                                    |
| PRED(ArgsRest -> , Exp ArgsRest) = {","}                                                        |
| PRED(ArgsRest -> λ) = { ) }                                                                     |
| PRED(Primitive -> Number) = { 0, 3, -}                                                          |
| PRED(Primitive -> OutE) = { outE }                                                              |
| PRED(Number -> NumberContent) = { 0, 3 }                                                        |
| PRED(Number -> -NumberContent) = { - }                                                          |
| PRED(NumberContent -> Int NumRest) = { 0, 3, λ}                                                 |
| PRED(NumRest -> Int NumRest) = { 0, 3 }                                                         |
| PRED(NumRest -> λ) = { ), ",", }                                                                |
| PRED(Id -> Letter RestId ) = { a, i }                                                           |
| PRED(RestId -> Id RestId ) = { a, i }                                                           |
| PRED(RestId -> λ ) = { in, (, -, 0, 3, outE}                                                    |
| PRED(Letter -> a) = { a }                                                                       |
| PRED(Letter -> i) = { i }                                                                       |
| PRED(Int -> 0) = { 0 }                                                                          |
| PRED(Int -> 3) = { 3 }                                                                          |
| PRED(OutE -> outE) = { outE }                                                                   |
| PRED(Out -> out) = { out }                                                                      |

# Predicción de ASDP LL(1)

| Pila                                                      | Cadena                                              | Regla o Acción                           |
| --------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------- |
| $                                                         | #start loop ( i in range1(3) ) { console(i)} #end $ | Prog -> #start Content #end              |
| $ #end Content #start                                     | #start loop ( i in range1(3) ) { console(i)} #end $ | Emparejar(#start)                        |
| $ #end Content                                            | loop ( i in range1(3) ) { console(i)} #end $        | Content -> StatementList                 |
| $ #end StatementList                                      | loop ( i in range1(3) ) { console(i)} #end $        | StatementList -> Statement StatementList |
| $ #end StatementList Statement                            | loop ( i in range1(3) ) { console(i)} #end $        | Statement -> ContentNoReturn             |
| $ #end StatementList ContentNoReturn                      | loop ( i in range1(3) ) { console(i)} #end $        | ContentNoReturn -> Loop                  |
| $ #end StatementList Loop                                 | loop ( i in range1(3) ) { console(i)} #end $        | Loop -> loop ( Id in Range ) { Content } |
| $ #end StatementList } Content { ) Range in Id ( loop     | loop ( i in range1(3) ) { console(i)} #end $        | Emparejar(loop)                          |
| $ #end StatementList } Content { ) Range in Id (          | (i in range1(3) ) { console(i)} #end $              | Emparejar(()                             |
| $ #end StatementList } Content { ) Range in Id            | i in range1(3) ) { console(i)} #end $               | Id -> Letter RestId                      |
| $ #end StatementList } Content { ) Range in RestId Letter | i in range1(3) ) { console(i)} #end $               | Letter -> i                              |
| $ #end StatementList } Content { ) Range in RestId i      | i in range1(3) ) { console(i)} #end $               | Emparejar(i)                             |
| $ #end StatementList } Content { ) Range in RestId        | in range1(3) ) { console(i)} #end $                 | RestId -> λ                              |
| $ #end StatementList } Content { ) Range in               | in range1(3) ) { console(i)} #end $                 | Emparejar(in)                            |
| $ #end StatementList } Content { ) Range                  | range1(3) ) { console(i)} #end $                    | Range -> range1(Exp)                     |
| $ #end StatementList } Content { ) ) Exp ( range1         | range1(3) ) { console(i)} #end $                    | Emparejar(range1)                        |
| $ #end StatementList } Content { ) ) Exp (                | (3) ) { console(i)} #end $                          | Emparejar(()                             |
| $ #end StatementList } Content { ) ) Exp                  | 3) ) { console(i)} #end $                           | Exp -> Primary_exp                       |
| $ #end StatementList } Content { ) ) Primary_exp          | 3) ) { console(i)} #end $                           | Primary_exp -> Primitive                 |
| $ #end StatementList } Content { ) ) Primitive            | 3) ) { console(i)} #end $                           | Primitive -> Number                      |
| $ #end StatementList } Content { ) ) Number               | 3) ) { console(i)} #end $                           | Number -> NumberContent                  |
| $ #end StatementList } Content { ) ) NumberContent        | 3) ) { console(i)} #end $                           | NumberContent -> Int NumRest             |
| $ #end StatementList } Content { ) ) NumRest Int          | 3) ) { console(i)} #end $                           | Int -> 3                                 |
| $ #end StatementList } Content { ) ) NumRest 3            | 3) ) { console(i)} #end $                           | Emparejar(3)                             |
| $ #end StatementList } Content { ) ) NumRest              | ) ) { console(i)} #end $                            | NumRest -> λ                             |
| $ #end StatementList } Content { )                        | ) { console(i)} #end $                              | Emparejar())                             |
| $ #end StatementList } Content {                          | { console(i)} #end $                                | Emparejar({)                             |
| $ #end StatementList } Content                            | console(i)} #end $                                  | Content -> StatementList                 |
| $ #end StatementList } StatementList                      | console(i)} #end $                                  | StatementList -> Statement StatementList |
| $ #end StatementList } StatementList Statement            | console(i)} #end $                                  | Content -> StatementList                 |
| $ #end StatementList } StatementList StatementList        | console(i)} #end $                                  | Statement -> ContentNoReturn             |
| $ #end StatementList } StatementList ContentNoReturn      | console(i)} #end $                                  | ContentNoReturn -> Console               |
| $ #end StatementList } StatementList Console              | console(i)} #end $                                  | Console -> console(Args)                 |
| $ #end StatementList } StatementList ) Args ( console     | console(i)} #end $                                  | Emparejar(console)                       |
| $ #end StatementList } StatementList ) Args (             | (i)} #end $                                         | Emparejar(()                             |
| $ #end StatementList } StatementList ) Args               | i)} #end $                                          | Args -> Exp                              |
| $ #end StatementList } StatementList ) Exp                | i)} #end $                                          | Exp -> Primary_exp                       |
| $ #end StatementList } StatementList ) Primary_exp        | i)} #end $                                          | Primary_exp -> Id                        |
| $ #end StatementList } StatementList ) Id                 | i)} #end $                                          | Id -> Letter RestId                      |
| $ #end StatementList } StatementList ) RestId Letter      | i)} #end $                                          | Letter -> i                              |
| $ #end StatementList } StatementList ) RestId i           | i)} #end $                                          | Emparejar(i)                             |
| $ #end StatementList } StatementList ) RestId             | )} #end $                                           | RestId -> λ                              |
| $ #end StatementList } StatementList )                    | )} #end $                                           | Emparejar())                             |
| $ #end StatementList } StatementList                      | } #end $                                            | StatementList -> λ                       |
| $ #end StatementList }                                    | } #end $                                            | Emparejar(})                             |
| $ #end StatementList                                      | #end $                                              | StatementList -> λ                       |
| $ #end                                                    | #end $                                              | Emparejar(#end)                          |
| $                                                         | $                                                   | accept                                   |
