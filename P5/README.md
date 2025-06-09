1. ¿Cuál es el propósito del decorador operation_logger en el programa?

El decorador operation_logger se utiliza para registrar (loggear) el nombre de la operación ejecutada, los argumentos de entrada y el resultado. Si ocurre un error, también lo captura y lo muestra. Esto permite depurar o auditar fácilmente qué operaciones se realizan sin modificar la lógica principal de la función.

2. ¿Por qué se utiliza *args en math_operation y en las funciones lambda?

Se usa *args para permitir que las operaciones acepten un número variable de argumentos. Esto es útil, por ejemplo, en la suma o la multiplicación, donde se pueden procesar 2 o más números sin definir una cantidad fija de parámetros.

3. ¿Cómo se maneja el error de división por cero en la función divide y por qué es importante?

La función divide lanza explícitamente un ZeroDivisionError si el divisor es cero. Este error es capturado por el decorador operation_logger, que imprime un mensaje de error en lugar de permitir que el programa se detenga. Esto es crucial para asegurar que el sistema sea robusto y no se bloquee ante entradas inválidas.

4. ¿Por qué en la clase Empleado se usa super().__init__() en el constructor?

Porque Empleado hereda de Ficha, y super().__init__() permite inicializar los atributos heredados (nombre, edad, nacio) sin tener que reescribir ese código. Así se garantiza una correcta inicialización y se evita duplicación.


5. ¿Qué ventaja ofrece usar @property para los atributos como nombre o dni?

Permite acceder a los atributos como si fueran públicos (ej. persona.nombre) pero manteniendo el encapsulamiento. Si más adelante se quiere modificar el comportamiento del acceso (por ejemplo, añadir validaciones), se puede hacer sin cambiar el resto del código.


6. ¿Qué sucede si se llama a registro.visualizar_registro() y hay tanto empleados como clientes?

El método recorre la lista de personas y llama a visualizar() en cada una. Gracias al polimorfismo, se ejecuta el método específico de la subclase (Empleado o Cliente), mostrando los datos de forma adecuada según el tipo real de cada objeto.


