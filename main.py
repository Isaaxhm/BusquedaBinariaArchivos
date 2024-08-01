# Importar Librerias
import os

import CreadorArchivos as CArchivos
import BorrarArchivos as BArchivos
import BusquedaArchivo as BBArchivo

def limpiarPantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Crear Menu de Opciones 
menu = {
    '1': 'Crear Archivos',
    '2': 'Borrar Archivo',
    '3': 'Buscar Archivo',
    '4': 'Salir'
}

while True:
    # Mostrar el menu de opciones
    print("\nMenú de Opciones:")
    for opciones, descripcion in menu.items():
        print(f"{opciones}. {descripcion}")

    # Leer la opción elegida por el usuario
    opcion = input("\nElija una opción: ")

    # Ejecutar la opción elegida
    if opcion == '1':
        # Ir a la funcion de Creador de archivos
        CArchivos.crear_archivo()
    elif opcion == '2':
        # Ir a la función de Borrar Archivo
        BArchivos.borrar_archivo()
    elif opcion == '3':
        # Ir a la función de Buscar Archivo
        BBArchivo.buscar_archivo()
    elif opcion == '4':
        limpiarPantalla()
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

