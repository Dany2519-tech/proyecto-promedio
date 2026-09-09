def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            numeros = []
            for linea in archivo:
                valor = linea.strip()
                if valor:
                    try:
                        numeros.append(int(valor))
                    except ValueError:
                        print(f"Advertencia: '{valor}' no es un número entero válido. Se omite.")
            return numeros
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return []
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return []

def calcular_promedio(lista_numeros, inicio, fin):
    # Validación de parámetros
    if not isinstance(inicio, int) or not isinstance(fin, int):
        raise TypeError("Los índices deben ser números enteros")
    
    if inicio < 0 or fin < 0:
        raise ValueError("Los índices deben ser mayores o iguales a 0")
    
    # Caso 1: si el segundo entero es menor que el primero
    if fin < inicio:
        return 0.0
    
    # Caso 2: si el primer entero es mayor que la longitud de la lista
    if inicio >= len(lista_numeros):
        return 0.0
    
    # Caso 3: si el segundo entero es mayor que la longitud
    if fin >= len(lista_numeros):
        fin = len(lista_numeros) - 1
    
    # Calcular promedio
    try:
        sublista = lista_numeros[inicio:fin+1]
        if not sublista:
            return 0.0
        return sum(sublista) / len(sublista)
    except ZeroDivisionError:
        return 0.0