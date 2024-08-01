import os

def crear_archivo():

    # crear carpeta de 'archivo' si no existe
    if not os.path.exists('archivos'):
        os.makedirs('archivos')
        print("Carpeta 'archivos' creada con éxito.")

    # Número de archivos a crear con su nombre
    num_archivos = int(input("Ingrese el número de archivos a crear: "))
    nombre_archivo = input("Ingrese el nombre de archivos a crear: ")

    # Recorrer los archivos y crearlos con el contenido ingresado por el usuariofor 
    for i in range(num_archivos):
        # Crear Archivos .txt dentro la carpeta 'archivo'
        nombre_archivo_txt = os.path.join('archivos', nombre_archivo + str(i+1) + ".txt")
        archivo = open(nombre_archivo_txt, "w")
        archivo.close()
        print(f"Archivo '{nombre_archivo_txt}' creado con éxito.")