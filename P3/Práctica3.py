import re

class Time:
    """
    Clase que representa una hora con formato AM/PM o 24 horas.
    """
    
    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0

    def __init__(self):
        """
        Inicializa los atributos en 0.
        """
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.format = "24 HOURS"
        Time.time_count += 1

    def __assign_format(self, pszFormat):
        """
        Asigna el formato después de verificar si es válido.
        """
        pszFormat = pszFormat.upper()
        if pszFormat in Time.TIME_FORMATS:
            self.format = pszFormat
            return True
        return False

    def __is_24hour_format(self):
        """
        Comprueba si el formato es "24 HOURS".
        """
        return self.format == "24 HOURS"

    def _is_valid_time(self):
        """
        Comprueba si la hora es válida.
        """
        if self.__is_24hour_format():
            return 0 <= self.hours <= 23 and 0 <= self.minutes <= 59 and 0 <= self.seconds <= 59
        elif self.format in ["AM", "PM"]:
            return 1 <= self.hours <= 12 and 0 <= self.minutes <= 59 and 0 <= self.seconds <= 59
        return False

    def set_time(self, nHoras, nMinutos, nSegundos, pszFormato):
        """
        Asigna una nueva hora validada.
        """
        if self.__assign_format(pszFormato):
            self.hours = nHoras
            self.minutes = nMinutos
            self.seconds = nSegundos
            if self._is_valid_time():
                return True
        return False

    def get_time(self):
        """
        Devuelve la hora actual en formato de cadena.
        """
        if self.__is_24hour_format():
            return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} 24 HOURS"
        else:
            return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.format}"

    @classmethod
    def from_string(cls, time_string):
        """
        Crea un objeto Time desde una cadena.
        """
        pattern = r"(\d{1,2}):(\d{2}):(\d{2})\s*(AM|PM|24 HOURS)"
        match = re.match(pattern, time_string, re.IGNORECASE)
        if match:
            horas, minutos, segundos, formato = match.groups()
            horas, minutos, segundos = int(horas), int(minutos), int(segundos)
            formato = formato.upper()
            new_time = cls()
            if new_time.set_time(horas, minutos, segundos, formato):
                return new_time
            else:
                print("Error: La hora no es válida según el formato.")
        else:
            print("Error: Formato de cadena de hora inválido.")
        return None

    @staticmethod
    def is_valid_format(time_format):
        """
        Verifica si el formato es válido.
        """
        return time_format.upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        """
        Devuelve el número total de objetos Time creados.
        """
        return cls.time_count

# Función fuera de la clase para mostrar la hora formateada
def mostrar_hora(time_obj):
    """
    Muestra la hora actual del objeto Time.
    """
    if time_obj:
        print(f"La hora actual es: {time_obj.get_time()}")
    else:
        print("No se ha configurado ninguna hora.")

# Función para manejar el menú principal
def main():
    """
    Función principal que ejecuta el menú del programa.
    """
    current_time = Time()  # Inicializamos con una hora por defecto (00:00:00 24 HOURS)
    
    while True:
        print("\nMenú de Gestión de Tiempo")
        print("1. Introducir una nueva hora")
        print("2. Visualizar hora")
        print("3. Crear una hora a partir de una cadena")
        print("4. Terminar")
        
        option = input("Elige una opción: ")
        
        if option == "1":
            try:
                horas = int(input("Introduce las horas: "))
                minutos = int(input("Introduce los minutos: "))
                segundos = int(input("Introduce los segundos: "))
                formato = input("Introduce el formato (AM, PM o 24 HOURS): ")
                if current_time.set_time(horas, minutos, segundos, formato):
                    print("Hora configurada correctamente.")
                else:
                    print("Error: La hora introducida no es válida.")
            except ValueError:
                print("Error: Entrada no válida. Asegúrate de introducir números para las horas, minutos y segundos.")

        elif option == "2":
            mostrar_hora(current_time)

        elif option == "3":
            cadena_hora = input("Introduce la hora en formato 'HH:MM:SS FORMATO' (por ejemplo, 02:30:45 PM): ")
            nueva_hora = Time.from_string(cadena_hora)
            if nueva_hora:
                current_time = nueva_hora
                print("Hora configurada correctamente desde la cadena.")
            else:
                print("Error: No se pudo configurar la hora desde la cadena.")

        elif option == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
