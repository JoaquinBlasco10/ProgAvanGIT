# Decorador que registra la operación
def operation_logger(func):
    def wrapper(operation, *args, **kwargs):
        try:
            result = func(operation, *args, **kwargs)
            print(f"Operación: {operation.__name__}--> Entradas: {args}, Resultado: {result}")
            return result
        except Exception as e:

            print(f"[ERROR] Operación: {operation.__name__}, Entradas: {args}, Error: {e}")
            return None
    return wrapper

# Funciones lambda para operaciones básicas
suma = lambda *args: sum(args)
suma.__name__='SUMA'

resta = lambda x, y: x - y
resta.__name__='RESTA'

multiplicacion = lambda *args: __import__('functools').reduce(lambda a, b: a * b, args)
multiplicacion.__name__='MULTIPLICACIÓN'

division = lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ZeroDivisionError("División por cero"))
division.__name__='DIVISIÓN'

# Función decorada para ejecutar operaciones
@operation_logger
def math_operation(operation, *args, **kwargs):
    return operation(*args, **kwargs)

# Pruebas
math_operation(suma, 5, 3)
math_operation(resta, 10, 4)
math_operation(multiplicacion, 2, 6)
math_operation(division, 15, 3)
math_operation(division, 10, 0)  # División por cero
math_operation(suma, 1, 2, 3, 4, 5)  # Múltiples argumentos
