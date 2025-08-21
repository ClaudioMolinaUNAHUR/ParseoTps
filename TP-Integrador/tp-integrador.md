## Beta

## Objetivo
Se presenta el Lenguaje "Beta"
Es un lenguaje de programacion esoterico con tipado fuerte, de tipo estructurado,
maneja expresiones, loops, condicionales y funciones

## Alcance
Solo maneja numeros enteros, booleanos y cadenas de textos, 
Puede hacer operacioones logicas, arimeticas y de comparacion
los condicionales manejan : if, else if, else
funciones propias y funciones personalizadas
puede ser recursivo


## Especificaciones Léxicas

- **Identificadores**  
  - Solo letras `[a-zA-Z]+`  
  - Case sensitive (`Name` ≠ `name`)  

- **Palabras reservadas**  
str, num, bool, func, return, if, else, loop, in, range, console,
true, false, #start, #end

- **Números**  
- Enteros con o sin signo: `10`, `-5`, `+3`  
- No se permiten decimales  

- **Cadenas (string)**  
- `"..."` o `'...'`  
- Admiten letras y espacios  
- Ejemplo: `"Hola mundo"`  

- **Operadores**  
- Aritméticos: `+ - * / %`  
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
`f(10, 20)`
```
---

# BNF

```bnf
<prog>::= #start <content> #end
<content>::= <content_no_return> | <content_return> | <content_no_return> <content> | <content_return> <content> | λ
<content_no_return>::= <function> |  <loop> | <conditional> | <var> | <assign> | <call_func>
<content_return>::= <function_return> | <console>  | <exp> | <call_func> | <primitive> | <id>
<console>::= console(<args>)
 
<function>::= func <id> (<param>) { <content> }
<function_return>::= func <id> (<param>) : <type> { <content> return <content_return> }
<param>::= <type> <id>,  <param> | <var>, <param> | <type> <id> | <var>

<call_func>::= <id>(<args>) | <id>()

<conditional>::= if ( <content_return> ) { <content> } | if ( <content_return> ) { <content> } else { <content> } | if ( <content_return> ) { <content> } else <conditional>

<loop>::= loop ( <id> in <range>) { <content> }
<range>:: = range(<number>, <number>) | range(<number>)

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

<string>::= "<str_content>" | '<str_content>'
<str_content>::= <letter> <str_content> | <letter> | ` ` <str_content> | ` ` | λ 

<primitive> ::= <number> | <boolean> | <string>
<operator> ::= <op_arit> | <op_bool_bin> | <op_comp>
<number> ::= <number_content> | +<number_content> | -<number_content>
<number_content> ::= <int> <number_content> | <int>
<type> ::= str | number | boolean
<op_arit> ::= + | - | * | / | %
<op_bool_bin>::= & | `|`
<op_bool_un>::= !
<op_comp>::= < | > | <= | >= | == | !=
<boolean>::= true | false
<letter>::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z 
<int>::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```


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
   - `num` → enteros  
   - `str` → cadenas  
   - `bool` → `true` o `false`   

4. **Control de flujo**
 - `if` evalúa expresiones y ejecuta bloques.  
 - `loop` itera sobre un rango ascendente o descendente.  

5. **Funciones**
 - Parámetros con valores por defecto opcionales.  
 - Pasaje de parámetros por valor.  
 - Si la función declara tipo de retorno, debe terminar con `return <expr>`.  

6. **Ámbito**
 - Variables son locales al bloque `{}`.  
 - Funciones crean su propio ámbito.  

7. **Ejecución**
 - Modelo secuencial, determinista.  
 - No hay concurrencia ni manejo de errores.  

