from funciones import leer_archivo, calcular_promedio

# Cargar los números
numeros = leer_archivo("datos/numeros.txt")
print(f"Números: {numeros}\n")

# Probar todos los casos
casos = [
    (1, 3, "Caso 1: Normal"),
    (3, 1, "Caso 2: fin < inicio"),
    (10, 12, "Caso 3: inicio > longitud"),
    (2, 10, "Caso 4: fin > longitud")
]

for inicio, fin, descripcion in casos:
    resultado = calcular_promedio(numeros, inicio, fin)
    print(f"{descripcion}: {resultado:.2f}")