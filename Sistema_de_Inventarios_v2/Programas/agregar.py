import csv
from Funciones import *

# Función para agregar un nuevo registro
def agregarRegistro(archivo : str, campos : list, titulo : str, almacen : int = 0) -> None: 
    print(f'Agregar {titulo}: \n')
    infoNueva = [0 for i in campos]
    # print(infoActual)
    contador = 0
    for campo in campos: 
        if type(campo) == list:
            if len(campo) == 4: 
                print(f"{campo[0]}")
                opcion, indiceDeOpcion, desechable = opciones("DB", campo[1], campo[0], [campo[2]], False)
                infoNueva[contador] = indiceDeOpcion
                if campo[1] == 'Utilidad.csv':
                    # print("Pruebas")
                    infoNueva[6] = 0 * int(find(campo[1], campo[3], indiceDeOpcion)[1])
                    # print(int(infoActual[3]) * int(find(campo[1], campo[3], indiceDeOpcion)[1]))
                    
            elif len(campo) > 0: 
                # print("Pruebas")
                if campo[1] == 'float':    
                    # print("Pruebas")
                    modificacion = 0
                    while modificacion == 0:
                        try:
                            modificacion = float(input(f'{campo[0]}: '))
                            if modificacion == 0:
                                print("Por favor ingresa una valor que no sea cero. ")
                        except:
                            print("Por favor ingresa un valor númerico. ")  
                    infoNueva[contador] = modificacion
                elif campo[1] == 'int':
                    modificacion = 0
                    while modificacion == 0:
                        try:
                            modificacion = int(input(f'{campo[0]}: '))
                            if modificacion == 0:
                                print("Por favor ingresa una valor que no sea cero. ")
                        except:
                            print("Por favor ingresa un valor númerico. ")  
                    infoNueva[contador] = modificacion

            else:
                if infoNueva[contador] == 0:
                    if contador == 0:
                        infoNueva[contador] = aumentarSecuencia(archivo, 1)
                    else:
                        infoNueva[contador] = 0
        else:    
            if campo != 'Almacen': 
                modificacion = input(f'{campo}: ')
                while modificacion == "" or modificacion == " " or modificacion.strip() == "":
                    print("Por favor ingresa información en el campo. ")
                    modificacion = input(f'{campo}: ')
                infoNueva[contador] = modificacion.replace('"', "").replace("'", "").replace(",","")
            elif almacen != 0: 
                infoNueva[contador] = almacen
        contador = contador + 1
    # print(f'{infoNueva}')
    nuevoArchivo, agregar = registrosTrasAgregar(archivo, infoNueva)
    if agregar == True: 
        guardarModificaciones(archivo, nuevoArchivo)
        print(f'Los cambios se han guardado con éxito. ')
    else: 
        print(f'Los cambios no han sido guardados con éxito. Por favor intenta nuevamente.')

# Función para obtener el nuevo archivo, el cual ya contiene el nuevo registro
def registrosTrasAgregar(archivo : str, modificaciones : list) -> list:
    agregar = False
    nuevoArchivo = []
    with open(f"DB\{archivo}", "r", encoding = 'utf8') as documento: 
        lector = csv.reader(documento)
        for fila, linea in enumerate(lector):
            if fila != 0: 
                nuevoArchivo.append([str(i) for i in linea])
    nuevoArchivo.append(modificaciones)
    agregar = True
    return nuevoArchivo, agregar
    # for nuevo in nuevoArchivo:
    #    print(nuevo)

if __name__ == '__main__':
    # agregarRegistro('Articulo.csv', camposArticulo(), 'Artículo')
    agregarRegistro('Socio de Negocios.csv', camposSocioDeNegocio(), 'Socio de Negocios')
    # print(find("Existencia.csv", "ID_articulo", 4))