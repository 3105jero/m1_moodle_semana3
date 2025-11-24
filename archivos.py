import csv


def guardar_csv(inventarios, filename='inventario.csv'):
    """
    Guarda el inventario en un archivo CSV.
    """
    fieldnames = ['nombre', 'precio', 'cantidad']

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for producto in inventarios:
                writer.writerow({
                    'nombre': producto['nombre'],
                    'precio': producto['precio'],
                    'cantidad': producto['cantidad']
                })

        print(f"Inventario guardado correctamente en '{filename}'")

    except Exception as e:
        print(f"Error guardando archivo CSV: {e}")



def cargar_csv(filename='inventario.csv'):
    """
    Carga el inventario desde un archivo CSV.
    Si el archivo no existe, devuelve una lista vacía.
    """

    inventarios = []

    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for fila in reader:
                inventarios.append({
                    'nombre': fila['nombre'],
                    'precio': float(fila['precio']),
                    'cantidad': int(fila['cantidad'])
                })

        print(f"Inventario cargado correctamente desde '{filename}'")

    except FileNotFoundError:
        print(f"El archivo '{filename}' no existe aún. Guarda primero.")

    except Exception as e:
        print(f"Error cargando archivo CSV: {e}")

    return inventarios
