**Pregunta 1:** <br>
**¿Por qué se utiliza el método __add__ en la clase RegistroDiario, y qué efecto tiene sobre los objetos?**

> *Se utiliza para sobrecargar el operador +, permitiendo combinar dos objetos RegistroDiario. Al usar registro1 + registro2, se crea un nuevo registro que contiene a todas las personas de ambos. Internamente, agrega las personas de ambos registros a una nueva instancia.*<br>

**Pregunta 2:** <br>
**¿Cómo se asegura el método agregar_persona() de que solo se añaden objetos válidos al registro?**

> *El método utiliza isinstance() para verificar que la persona sea instancia de Empleado o Cliente antes de añadirla. Esto evita que se agreguen objetos de otro tipo (como strings o enteros), garantizando consistencia en la lista.*<br>

**Pregunta 3:** <br>
**¿Qué diferencia hay entre los métodos visualizar_registro() y visualizar_empleados()?**

> *visualizar_registro() muestra todos los objetos en la lista, sin importar si son empleados o clientes, llamando al método visualizar() de cada uno. En cambio, visualizar_empleados() filtra y muestra solo los que son instancias de Empleado.*<br>

**Pregunta 4:** <br>
**. ¿Cómo permite el método __getitem__ acceder a los elementos del registro, y qué ventaja aporta?**

> *Sobrecarga el operador de indexación ([]), permitiendo usar registro[i] para acceder a una persona en el índice i. Esto hace el acceso más intuitivo, como si el objeto fuera una lista, sin necesidad de exponer directamente el atributo interno.*<br>

**Pregunta 5:** <br>
**¿Qué ocurre si el usuario introduce una hora de nacimiento con un formato incorrecto, como "25:99:00"?**

> *El método strptime() del módulo time lanzará un ValueError porque el formato no es válido (las horas no pueden ser 25 ni los minutos 99). Actualmente no se gestiona este error, por lo que habría que validarlo o capturarlo para mejorar robustez.*<br>

**Pregunta 6:** <br>
**¿Por qué se usa super() en los constructores de Empleado y Cliente?**

> *Porque Empleado y Cliente heredan de Ficha, y super() permite llamar al constructor de la clase base para inicializar los atributos comunes (nombre, edad, nacio). Así se evita duplicar código y se respeta el principio DRY (Don't Repeat Yourself).*<br>