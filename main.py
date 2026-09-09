import sys
import argparse
from funciones import leer_archivo, calcular_promedio

def main():
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(
        description="Calcula el promedio de números en un archivo entre dos índices."
    )
    parser.add_argument(
        "archivo", 
        type=str,
        help="Ruta al archivo con números enteros (uno por línea)"
    )
    parser.add_argument(
        "inicio", 
        type=int,
        help="Índice inicial (mayor o igual a 0)"
    )
    parser.add_argument(
        "fin", 
        type=int,
        help="Índice final (mayor o igual a 0)"
    )
    
    # Parsear argumentos
    args = parser.parse_args()
    
    # Leer el archivo
    numeros = leer_archivo(args.archivo)
    
    if not numeros:
        print("No se pudieron leer datos válidos del archivo.")
        sys.exit(1)
    
    # Calcular el promedio
    try:
        promedio = calcular_promedio(numeros, args.inicio, args.fin)
        print(f"Promedio de los valores entre índices {args.inicio} y {args.fin}: {promedio:.2f}")
    except (TypeError, ValueError) as e:
        print(f"Error en los parámetros: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()