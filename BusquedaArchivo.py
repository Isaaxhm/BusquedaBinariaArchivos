import os

def buscar_archivo():
    # Obtener la lista de archivos en la carpeta 'archivos' y ordenarla
    archivos = sorted(os.listdir('archivos'))

    # Preguntar al usuario por el nombre del archivo a buscar
    nombre_archivo = input("Ingrese el nombre del archivo a buscar: ")

    # Implementar la búsqueda binaria
    izquierda = 0
    derecha = len(archivos) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if archivos[medio].startswith(nombre_archivo):
            print(f"Archivo '{nombre_archivo}.txt' encontrado en la posición {medio+1}")
            print(f"archivos '{archivos}")
            return
        elif archivos[medio] < nombre_archivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    print(f"Archivo '{nombre_archivo}.txt' no encontrado")