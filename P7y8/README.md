**Pregunta 1:**  
**¿Qué condiciones deben cumplirse para que se pueda crear correctamente una instancia de la clase `Libro` y cómo se gestionan los errores si alguna condición no se cumple?**

> *Deben introducirse un título y un autor no vacíos, un año entero positivo y un género no vacío. Si alguna condición no se cumple, se lanza una excepción `ErrorBiblioteca` con un mensaje adecuado.*  

**Pregunta 2:**  
**¿Qué ventaja ofrece el uso del método `descripcion()` redefinido en las clases `Libro` y `Revista` al momento de mostrar las publicaciones?**

> *Permite aplicar polimorfismo: se puede recorrer una lista de publicaciones y llamar a `descripcion()` sin importar si el objeto es un libro o una revista, obteniendo siempre la información detallada correspondiente.*  

**Pregunta 3:**  
**¿Cómo funciona el proceso de guardar las publicaciones en un archivo y qué formato se utiliza para ello?**

> *Se recorre la lista de objetos `Libro` y `Revista`, extrayendo sus atributos en diccionarios que incluyen el tipo de publicación. Luego, se guarda toda la lista como un archivo JSON mediante `json.dump()`.*  

**Pregunta 4:**  
**¿Qué pasos realiza el sistema al cargar un archivo de publicaciones y cómo determina si crear un `Libro` o una `Revista`?**

> *Lee el archivo con `json.load()`, recorre cada diccionario y, según el valor del campo `"tipo"`, instancia un objeto de la clase correspondiente (`Libro` o `Revista`). Todos los atributos necesarios se recuperan del diccionario.*  

**Pregunta 5:**  
**¿Qué diferencia hay entre las excepciones `ErrorBiblioteca` y `ErrorArchivo`, y cómo se usan en el programa?**

> *`ErrorBiblioteca` es una excepción base para errores generales del sistema. `ErrorArchivo` hereda de ella y se usa específicamente para problemas relacionados con lectura o escritura de ficheros, como archivos inexistentes o malformateados.*  

**Pregunta 6:**  
**¿Qué ocurre si el usuario introduce un año no numérico o un número negativo al registrar una publicación, y cómo se maneja en el código?**

> *El valor no pasará la validación de `leer_entero()`, que exige un número entero positivo. Si aún así llega a la clase, el constructor lanzará una excepción `ErrorBiblioteca`, y se informará al usuario sin que el programa se detenga.*  
