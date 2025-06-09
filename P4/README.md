**1. ¿Cuál es el propósito de la clase CMatFloat en este programa?**  
> *La clase CMatFloat representa matrices 1D y 2D utilizando la librería numpy. Permite la creación, modificación y realización de operaciones básicas (como suma y resta) entre matrices.*  

**2. ¿Para qué sirven los métodos CrearMatriz1D y CrearMatriz2D?**  
> *CrearMatriz1D crea una matriz unidimensional con una sola fila, mientras que CrearMatriz2D crea una matriz bidimensional con un número específico de filas y columnas, ambas inicializadas en cero.*  

**3. ¿Qué hace el método Introducir en la clase CMatFloat?**  
> *Introducir permite al usuario ingresar manualmente los valores para cada elemento de la matriz. Los datos se almacenan en la matriz existente, siempre que haya sido creada.*  

**4. ¿Cómo asegura el programa que ambas matrices tengan las mismas dimensiones para sumar o restar?**  
> *Antes de realizar la suma o resta, el programa verifica que las dimensiones de ambas matrices coincidan. Si no coinciden, el programa indica que no es posible realizar la operación.*  

**5. ¿Qué función tiene el método Existe?**  
> *Existe verifica si la matriz ha sido creada y no está vacía. Retorna True si la matriz existe y contiene datos; de lo contrario, retorna False.*  

**6. ¿Cuál es la función de leer_int y leer_float?**  
> *Estas funciones ayudan a garantizar que el usuario introduzca un número entero o decimal válido, respectivamente, mostrando un mensaje de error y pidiendo reintento en caso de entrada no válida.*  

**7. ¿Cómo está estructurado el menú principal y el submenú de operaciones?**  
> *El menú principal permite al usuario crear una matriz, introducir valores, mostrar la matriz y realizar operaciones con otra matriz (suma y resta). Al elegir "Operaciones con matrices," se abre un submenú donde el usuario selecciona entre sumar, restar o volver al menú principal.*
