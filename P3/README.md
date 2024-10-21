1. **¿Qué hace la clase Time en el programa?**<br>
    > *La clase Time representa una hora con formato AM/PM o de 24 horas. Permite almacenar y validar una hora, y también convertir una cadena de texto con formato de hora en un objeto Time.*<br>

2. ¿Cómo se validan los valores de hora, minutos y segundos?
    Los valores de hora, minutos y segundos se validan dependiendo del formato de la hora. Para el formato de 24 horas, las horas deben estar entre 0 y 23; para los formatos AM/PM, las horas deben estar entre 1 y 12. Los minutos y segundos siempre deben estar entre 0 y 59.

3. ¿Cómo se maneja el formato de hora (AM/PM o 24 HOURS) en el programa?
    El formato de hora se maneja utilizando el método __assign_format(), que convierte el formato a mayúsculas y lo valida comparándolo con los valores permitidos: "AM", "PM" y "24 HOURS".

4. ¿Qué hace la función from_string()?
    La función from_string() es un método de clase que permite crear un objeto Time a partir de una cadena con el formato "HH:MM FORMAT". Si la cadena es válida, el objeto se crea con los valores extraídos; de lo contrario, se muestra un mensaje de error.

5. ¿Cómo se visualiza la hora configurada en el objeto Time?
    La hora se visualiza usando el método get_time(), que devuelve la hora en formato de cadena. El formato cambia dependiendo de si es 12 horas (AM/PM) o 24 horas, siguiendo las validaciones previas.

6. ¿Qué función tiene el menú en el programa?
    El menú principal permite al usuario interactuar con el programa, eligiendo entre las opciones de ingresar una nueva hora, visualizar la hora actual, crear una hora desde una cadena, o terminar el programa.

7. ¿Qué pasa si el usuario introduce una hora inválida?
    Si el usuario introduce una hora inválida (por ejemplo, con valores fuera de los rangos permitidos), el programa lo detecta y muestra un mensaje de error, sin cambiar la hora almacenada en el objeto.

8. ¿Cómo se asegura que el formato de hora esté en mayúsculas aunque el usuario lo introduzca en minúsculas?
    El formato se convierte automáticamente a mayúsculas dentro del método __assign_format() para evitar problemas de capitalización y asegurar que se compare correctamente con los formatos válidos.

