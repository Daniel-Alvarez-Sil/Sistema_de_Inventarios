import csv
from Funciones import *

# Función que se encarga de modificar un registro
def modificarRegistro(archivo : str, campoID : str, campos : list, indice : list, titulo : str, seleccion : str, almacen : int = 0) -> None: 
    print(f'Modificar {titulo}: \n')
    opcion = -1
    objetoAModificar = 0
    # longitudArchivo = longitud("DB", archivo)
    regresarOpcion = 0
    while (opcion != regresarOpcion):
        opcion, objetoAModificar, regresarOpcion = opciones("DB", archivo, seleccion, indice, True, almacen)
        if opcion != regresarOpcion:
            infoActual = find(archivo, campoID, objetoAModificar)
            infoNueva = [0 for i in campos]
            # print(infoActual)
            contador = 0
            for campo in campos: 
                if type(campo) == list:
                    if len(campo) == 4: 
                        print(f"{campo[0]} ({find(campo[1], campo[3], str(infoActual[contador]))[campo[2]]})")
                        opcion, indiceDeOpcion, desechable = opciones("DB", campo[1], campo[0], [campo[2]], False, )
                        infoNueva[contador] = indiceDeOpcion
                        if campo[1] == 'Utilidad.csv':
                            # print("Pruebas")
                            infoNueva[6] = float(infoActual[3]) * (1 +  (int(find(campo[1], campo[3], indiceDeOpcion)[1]) / 100))
                            # print(int(infoActual[3]) * int(find(campo[1], campo[3], indiceDeOpcion)[1]))
                            
                    elif len(campo) > 0: 
                        # print("Pruebas")
                        if campo[1] == 'float':    
                            # print("Pruebas")
                            modificacion = 0
                            while modificacion == 0:
                                try:
                                    modificacion = float(input(f'{campo[0]} ({infoActual[contador]}): '))
                                    if modificacion == 0:
                                        print("Por favor ingresa una valor que no sea cero. ")
                                except:
                                    print("Por favor ingresa un valor númerico. ")  
                            infoNueva[contador] = modificacion
                        elif campo[1] == 'int':
                            modificacion = 0
                            while modificacion == 0:
                                try:
                                    modificacion = int(input(f'{campo[0]} ({infoActual[contador]}): '))
                                    if modificacion == 0:
                                        print("Por favor ingresa una valor que no sea cero. ")
                                except:
                                    print("Por favor ingresa un valor númerico. ")  
                            infoNueva[contador] = modificacion

                    else:
                        if infoNueva[contador] == 0:
                            infoNueva[contador] = infoActual[contador]
                else:  
                    modificacion = input(f'{campo} ({infoActual[contador]}): ')
                    while modificacion == "" or modificacion == " " or modificacion.strip() == "":
                        print("Por favor ingresa información en el campo. ")
                        modificacion = input(f'{campo} ({infoActual[contador]}): ')
                    infoNueva[contador] = modificacion.replace('"', "").replace("'", "").replace(",","")
                contador = contador + 1
            # print(f'{infoNueva}')
            nuevoArchivo, modificar = registrosTrasModificar(archivo, campoID, objetoAModificar, infoNueva)
            if modificar == True: 
                guardarModificaciones(archivo, nuevoArchivo)
                print(f'Los cambios se han guardado con éxito. ')
            else: 
                print(f'Los cambios no han sido guardados con éxito. Por favor intenta nuevamente.')

# Función para obtener el nuevo archivo, el cual ya contiene el registro modificado
def registrosTrasModificar(archivo : str, campo : str, indiceDeModificacion : str, modificaciones : list) -> list:
    modificar = False
    nuevoArchivo = []
    with open(f"DB\{archivo}", "r", encoding = 'utf8') as documento: 
        lector = csv.reader(documento)
        for fila, linea in enumerate(lector):
            if fila != 0: 
                if linea[0] == indiceDeModificacion:
                    nuevoArchivo.append([str(i) for i in modificaciones])
                    modificar = True
                else: 
                    nuevoArchivo.append([str(i) for i in linea])
    return nuevoArchivo, modificar
    # for nuevo in nuevoArchivo:
    #    print(nuevo)    

if __name__ == '__main__':
    modificarRegistro('Socio de Negocios.csv', 'ID_socio', camposSocioDeNegocio(), 2, 'Socio de Negocios', 'socio de negocios')
    # modificarRegistro('Articulo.csv', 'ID_articulo', camposArticulo(), 2, 'Artículo', 'artículo')
