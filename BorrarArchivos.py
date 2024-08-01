import os

def borrar_archivo():
    carpeta = 'archivos'
    palabraClave = input('Ingrese la palabra clave o nombre del archivo: ')

    if os.path.exists(carpeta):
        if "." in palabraClave:
            eliminar_archivo(carpeta, palabraClave)
        else:
            eliminar_archivos(carpeta, palabraClave)
    else:
        print(f"La carpeta '{carpeta}' no existe.")

def eliminar_archivos(ruta, palabra_clave):
    for archivo in os.listdir(ruta):
        if palabra_clave in archivo:
            os.remove(os.path.join(ruta, archivo))
            print(f"Eliminado: {archivo}")

def eliminar_archivo(ruta, nombre_archivo):
    try:
        os.remove(os.path.join(ruta, nombre_archivo))
        print(f"Eliminado: {nombre_archivo}")
    except FileNotFoundError:
        print(f"No se encontró el archivo: {nombre_archivo}")
