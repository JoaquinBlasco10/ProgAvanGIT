## PREGUNTAS Y RESPUESTAS

# Ejercicio 1:<br>

**Pregunta 1:** <br>
  **-En este codigo, ¿que rango de números coge la variable range?<br>**
  > *En el código, la función range(1, 6) genera los números del 1 al 5, tanto para la   variable i como para la variable j. El número 6 no está incluido.*<br>

  **Pregunta 2: <br>
  -¿De qué sire el bucle "if" en el que la condición es i % 2 == 0?<br>**
  > *El bucle if i % 2 == 0 se utiliza para verificar si el número i es par. Si lo es, la instrucción continue hace que se salte esa iteración, omitiendo la impresión de multiplicaciones para números pares.*<br>

  **Pregunta 3: <br>
  -¿Qué hace la llamada a la función "tabla_multiplicar( )"? <br>**
  >*La llamada a la función tabla_multiplicar() ejecuta el código dentro de la función, generando e imprimiendo las tablas de multiplicar del 1 al 5 con las condiciones especificadas (omitir números pares, detener si el producto supera 20).*<br>

 # Ejercicio 2:<br>
**Pregunta 1: <br>
-¿Para qué sirven las funciones "text = text.lower( )" y "text = text.strip( )"?<br>**
> *text.lower() convierte el texto a minúsculas, y text.strip() elimina los espacios en blanco al inicio y al final del texto. Ambas funciones ayudan a normalizar el texto antes de procesarlo.*<br>

**Pregunta 2: <br>
-¿Por qué el contador de palabras "replaced_count" se inicializa a 0?** <br>
> *El contador de palabras replaced_count se inicializa a 0 para llevar un registro de cuántas palabras de la lista han sido reemplazadas en la cadena de texto. Al comenzar en 0, el contador puede incrementarse en 1 cada vez que se realiza un reemplazo, lo que permite devolver el número total de palabras reemplazadas al final de la función.*<br>

 # Ejercicio 3:<br>
**Pregunta 1: <br>
-¿Cómo clasifica el programa a un numero para determinar si es primo o palíndromo? <br>**
> *Un número es primo si es mayor que 1 y no tiene divisores distintos de 1 y de sí mismo (verificado en is_prime(n)), en cambio un número es un palíndromo si se lee igual de adelante hacia atrás (verificado en check_palindrome(primes)).*<br>

**Pregunta 2: <br>
-¿Por qué el "for" que está dentro del "if n <= 1" coge esos parámetros?<br>**
> *El for dentro de is_prime(n) no se ejecuta si \(n\) es menor o igual a 1 porque la función devuelve "False" en esa condición, indicando que \(n\) no puede ser primo. El bucle solo se ejecuta si \(n\) es mayor que 1.*<br>

 # Ejercicio 4:<br>
**Pregunta 1: <br>
-¿Cómo comprueba "len(numeros) == len(set(numeros))" que no se repite ningún numero de la lista?<br>**
> *La expresión len(numeros) == len(set(numeros)) comprueba si todos los números son únicos al comparar la longitud de la lista original con la de un conjunto, que elimina duplicados. Si las longitudes son iguales, no hay números repetidos.*<br>

 # Ejercicio 5:<br>
**Pregunta 1: <br>
-¿Cómo funciona el bucle "if" para eliminar tareas de la lista?<br>**
> *El bucle if en la función remove_task(task) verifica si la tarea a eliminar está en la lista. Si la tarea está presente, la elimina con el método remove(). Si no está, muestra un mensaje indicando que no se encontró la tarea.*<br>

**Pregunta 2: <br>
-¿Con qué finalidad se define "list_tasks( )" en el código?<br>**
> *La función list_tasks() se define para mostrar todas las tareas pendientes y enumerarlas, o informar si no hay tareas en la lista.*<br>

 # Ejercicio 6:<br>
**Pregunta 1: <br>
-¿Cómo hace el contador para enumerar cada una de las cadenas para luego después clasificarlas?<br>**
> *El contador utiliza la función `enumerate()` para asignar un número a cada cadena en la lista, comenzando desde 1. Esto permite que las cadenas se presenten de forma ordenada cuando se imprimen, clasificándolas por su posición en la lista.*<br>

