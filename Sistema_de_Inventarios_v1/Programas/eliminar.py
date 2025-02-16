import csv
from Funciones import *

# Función para eliminar un registro
def eliminarRegistro(carpeta : str, archivo : str, seleccion : str, indice : int, regresar : bool, concordancias : list, campo : str, almacen : int = 0) -> None:
    opcion = -1
    objetoAEliminar = 0
    # longitudArchivo = longitud(carpeta, archivo)
    regresarOpcion = 0
    while (opcion != regresarOpcion):
        # if objetoAEliminar != 0:
        #    longitudArchivo = longitud(carpeta, archivo)
        opcion, objetoAEliminar, regresarOpcion = opciones(carpeta, archivo, seleccion, indice, regresar, almacen)
        if opcion != regresarOpcion:
            print(objetoAEliminar)
            nuevoArchivo, eliminado = registrosTrasEliminar(archivo, concordancias, campo, objetoAEliminar)
            if eliminado == True: 
                #print([titulos("DB", "Articulo.csv")] + nuevoArchivo)
                guardarModificaciones(archivo, nuevoArchivo)
                aumentarSecuencia(archivo, -1)
                print("\nEl artículo ha sido eliminado con éxito. \n")
                regresarOpcion -= 1
            else: 
                print("El artículo no se puede eliminar porque tiene información asociada. ")

# Función para obtener el nuevo archivo, el cual ya no contiene el registro eliminado
def registrosTrasEliminar(archivo : str, concordancias : list, campo : str, eliminacion : str) -> list:
    nuevoArchivo = []
    eliminar = False
    with open(f'DB\{archivo}', "r", encoding = 'utf8') as documento:
        lector = csv.reader(documento)
        for fila, linea in enumerate(lector):
            if fila != 0:
                if linea[0] == eliminacion:
                    for concordancia in concordancias:
                        if find(concordancia, campo, eliminacion):
                            # print(find(concordancia, campo, eliminacion))
                            return [], False
                else:
                    nuevoArchivo.append(linea)
    return nuevoArchivo, True