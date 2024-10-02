## PREGUNTAS Y RESPUESTAS

# Ejercicio 1:<br>

**PREGUNTA 1:** <br>
  **-En este codigo, ¿que rango de números coge la variable range?<br>**
  > *En el código, la función range(1, 6) genera los números del 1 al 5, tanto para la   variable i como para la variable j. El número 6 no está incluido.*<br><br>


  **PREGUNTA 2: <br>
  -¿De qué sire el bucle "if" en el que la condición es i % 2 == 0?<br>**
  > *El bucle if i % 2 == 0 se utiliza para verificar si el número i es par. Si lo es, la instrucción continue hace que se salte esa iteración, omitiendo la impresión de multiplicaciones para números pares.*<br><br>

  **PREGUNTA 3: <br>
  -¿Qué hace la llamada a la función "tabla_multiplicar( )"? <br>**
  >*La llamada a la función tabla_multiplicar() ejecuta el código dentro de la función, generando e imprimiendo las tablas de multiplicar del 1 al 5 con las condiciones especificadas (omitir números pares, detener si el producto supera 20).*<br><br>  

 # Ejercicio 2:<br>
**Pregunta 1: <br>
-¿Para qué sirven las funciones "text = text.lower( )" y "text = text.strip( )"?<br>**
> *text.lower() convierte el texto a minúsculas, y text.strip() elimina los espacios en blanco al inicio y al final del texto. Ambas funciones ayudan a normalizar el texto antes de procesarlo.*<br><br>

**Pregunta 2: <br>
-¿Por qué el contador de palabras "replaced_count" se inicializa a 0?** <br>
> *El contador de palabras replaced_count se inicializa a 0 para llevar un registro de cuántas palabras de la lista han sido reemplazadas en la cadena de texto. Al comenzar en 0, el contador puede incrementarse en 1 cada vez que se realiza un reemplazo, lo que permite devolver el número total de palabras reemplazadas al final de la función.*<br><br>

 # Ejercicio 3:<br>
**Pregunta 1: <br>
-¿Cómo clasifica el programa a un numero para determinar si es primo o palíndromo? <br>**
> *Un número es primo si es mayor que 1 y no tiene divisores distintos de 1 y de sí mismo (verificado en is_prime(n)), en cambio un número es un palíndromo si se lee igual de adelante hacia atrás (verificado en check_palindrome(primes)).*<br><br>

**Pregunta 2: <br>
-¿Por qué el "for" que está dentro del "if n <= 1" coge esos parámetros?<br>**
> *El for dentro de is_prime(n) no se ejecuta si \( n \) es menor o igual a 1 porque la función devuelve `False` en esa condición, indicando que \( n \) no puede ser primo. El bucle solo se ejecuta si \( n \) es mayor que 1.*<br><br>

