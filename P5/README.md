**Pregunta 1:** <br>
**¿Cómo se asegura el decorador operation_logger de que se registre correctamente tanto un resultado como un posible error en la operación?**

> *El decorador envuelve la función math_operation y utiliza un bloque try-except. En el try, ejecuta la operación y registra el nombre de la función, los argumentos y el resultado. Si ocurre una excepción (como una división por cero), el except la captura y muestra un mensaje de error sin detener el programa. De este modo, se mantiene el control del flujo incluso ante entradas inválidas..*<br>

**Pregunta 2:** <br>
**¿Por qué es útil usar funciones lambda para operaciones como suma, resta, multiplicación y división en este contexto?**

> *Las funciones lambda permiten definir de forma rápida y concisa operaciones simples sin tener que escribir funciones completas con def. Además, como son objetos de primera clase en Python, se pueden pasar como argumentos a otras funciones (como math_operation) para aplicarlas dinámicamente, lo cual favorece un diseño más flexible y compacto.*<br>

**Pregunta 3:** <br>
**¿Qué ventajas aporta utilizar *args en la definición de math_operation y en algunas funciones lambda como add o multiply?**

> *El uso de *args permite que las funciones puedan aceptar cualquier cantidad de argumentos posicionales. Esto es especialmente útil en operaciones como suma o multiplicación, donde puede haber más de dos operandos. Así, math_operation(add, 1, 2, 3, 4, 5) es válido sin tener que definir una función con un número fijo de parámetros. Mejora la reutilización y adaptabilidad del código.*<br>

**Pregunta 4:** <br>
**¿Para qué se utiliza el decorador @property en las clases Book y User?**

> *Se usa para permitir el acceso controlado a los atributos privados como si fueran públicos. Así se mantiene el encapsulamiento sin necesidad de usar métodos get_ o set_ explícitos, facilitando la lectura del código y permitiendo incluir validaciones futuras si fuera necesario.*<br>


**Pregunta 5:** <br>
**¿Qué función cumple la clase Library y cómo gestiona los libros?**

> *La clase Library centraliza toda la gestión de libros: puede añadir, eliminar, prestar, devolver y buscar libros. Internamente, almacena los libros en un diccionario con la clave como ISBN, lo que permite acceder y modificar libros de forma rápida y eficiente.*<br>


**Pregunta 6:** <br>
**¿Cómo se generan los IDs únicos para usuarios y libros y por qué es importante?**

> *Se utiliza la función uuid4() del módulo uuid, recortando el resultado a los primeros 8 caracteres para crear un ID corto pero único. Esto evita colisiones y permite identificar de forma segura a cada libro y usuario dentro del sistema sin tener que depender de entradas manuales.*<br>
