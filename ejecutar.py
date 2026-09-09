from funciones import leer_archivo, calcular_promedio

# Aquí defines qué prueba quieres hacer
archivo = "datos/numeros.txt"
inicio = 1
fin = 3

# Leer archivo
numeros = leer_archivo(archivo)
print(f"Números leídos: {numeros}")

# Calcular promedio
if numeros:
    resultado = calcular_promedio(numeros, inicio, fin)
    print(f"Promedio entre índices {inicio} y {fin}: {resultado:.2f}")
else:
    print("No se pudieron leer números.")