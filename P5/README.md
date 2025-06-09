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
**¿Por qué en la clase Empleado se usa super().__init__() en el constructor?**

> *Porque Empleado hereda de Ficha, y super().__init__() permite inicializar los atributos heredados (nombre, edad, nacio) sin tener que reescribir ese código. Así se garantiza una correcta inicialización y se evita duplicación.*<br>


**Pregunta 5:** <br>
**¿Qué ventaja ofrece usar @property para los atributos como nombre o dni?**

> *Permite acceder a los atributos como si fueran públicos (ej. persona.nombre) pero manteniendo el encapsulamiento. Si más adelante se quiere modificar el comportamiento del acceso (por ejemplo, añadir validaciones), se puede hacer sin cambiar el resto del código.*<br>


**Pregunta 6:** <br>
**¿Qué sucede si se llama a registro.visualizar_registro() y hay tanto empleados como clientes?**

> *El método recorre la lista de personas y llama a visualizar() en cada una. Gracias al polimorfismo, se ejecuta el método específico de la subclase (Empleado o Cliente), mostrando los datos de forma adecuada según el tipo real de cada objeto.*<br>
