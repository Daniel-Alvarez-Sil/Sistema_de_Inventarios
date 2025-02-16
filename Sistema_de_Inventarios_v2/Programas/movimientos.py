import csv
from Funciones import * 
import datetime
import math

def registrarMovimiento(ID_tipo_de_movimiento : int, ID_almacen : int) -> None:
    # empleados = []
    # tiposDeMovimiento = [1, 2, 3, 4, 5]
    continuar = 0
    departamentos = [1,1,2,3]
    opcion = -1
    opcionesEmp = []
    modoDeBusqueda = 0
    elemento = {'ID_movimiento': '',
                'ID_articulo': '',
                'Descripcion': '', 
                'Cantidad': '',
                'Importe sin Iva': '',
                'IVA': ''}
    elementos = []
    movimiento = [0,0,0,0,0,'','',0,0,0,0]
    while (opcion != len(opcionesEmp)):
        opcion = -1
        contador = 0
        opcionesEmp = []
        indices = []
        if modoDeBusqueda not in [1,2]:
            with open("DB\Empleado.csv", "r", encoding = 'utf8') as documento: 
                lector = csv.DictReader(documento)
                for fila, linea in enumerate(lector):
                    # print(linea)
                    if int(linea['ID_almacen'] ) == ID_almacen and int(linea['ID_departamento']) == departamentos[ID_tipo_de_movimiento - 1]: 
                        contador += 1
                        if contador == 1:
                            print("Escoge el empleado encargado de este movimiento: \n")
                        # empleados.append(str(linea['Nombre'] + linea['Apellido Paterno'] + linea['Apellido Materno']))
                        print(f"\t{contador}) {find('Departamento.csv', 'ID_departamento', linea['ID_departamento'])[1]}: {str(linea['Nombre'] + ' ' + linea['Apellido Paterno'] + ' ' + linea['Apellido Materno'])}")
                        opcionesEmp.append(contador)
                        indices.append(int(linea['ID_empleado']))
                print()
                print(f'    {contador + 1}) Regresar')
                opcionesEmp.append(contador + 1)
            # print("Prueba 1")
            while opcion not in opcionesEmp:
                try:
                    opcion = int(input("\nIngresa tu opción: "))
                    if opcion not in opcionesEmp: 
                        print("Por favor ingresa una opción correcta")
                except: 
                    print("Por favor ingresa un valor númerico")
                    opcion = 0
        if opcion != len(opcionesEmp):
            print("""
            Ingrese su manera de búsqueda: 
                
                1) Por Menú de Búsqueda
                2) Por Código de Barras
            
            3) Cancelar
                """)
            # print("Prueba 2")
            modoDeBusqueda = 0
            while modoDeBusqueda not in [1,2,3]:
                # Cancelar
                if continuar == 3: 
                    elementos = []
                    movimiento = [0,0,0,0,0,'','',0,0,0,0]
                    modoDeBusqueda = 0
                continuar = 1
                try:
                    modoDeBusqueda = int(input("\nIngresa tu opción: "))
                    if modoDeBusqueda not in [1,2,3]: 
                        print("Por favor ingresa una opción correcta")
                except: 
                    print("Por favor ingresa un valor númerico")
                    modoDeBusqueda = 0
            while continuar == 1:
                if modoDeBusqueda == 1:
                    indice = busquedaPorMenu(ID_almacen)
                elif modoDeBusqueda == 2:
                    indice = busquedaPorCodigo(ID_almacen)
                else: 
                    elementos = []
                    movimiento = [0,0,0,0,0,'','',0,0,0,0]
                    modoDeBusqueda = 0    
                # print("Prueba")            
                if indice != "0":
                    articulo = find("Articulo.csv", 'ID_articulo', indice)
                    elemento['ID_articulo'] = indice
                    elemento['Descripción'] = articulo[2]
                    elemento['Importe sin IVA'] = float(articulo[6])
                    elemento['IVA'] = round((elemento['Importe sin IVA'] * (int(find('IVA.csv', 'ID_IVA', articulo[5])[2])/100)), 2)
                    cantidad = 0
                    while cantidad == 0 or ((tieneExistencias(int(indice), ID_almacen) + cantidad) < 0):
                        try:
                            cantidad = float(input(f"\nIngresa la cantidad de '{articulo[2]}': "))
                            cantidad = -abs(cantidad) if ID_tipo_de_movimiento == 1 else abs(cantidad)
                            if cantidad == 0 or cantidad % float(articulo[7]) != 0: 
                                print(f"La cantidad no se alinea con el múltiplo de venta del artículo, el cual es {articulo[7]}")
                            if tieneExistencias(int(indice), ID_almacen) + cantidad < 0:
                                print(f'La cantidad ingresada no es aceptable porque no hay suficiente stock. Existencia del producto: {tieneExistencias(int(indice), ID_almacen)}')
                        except: 
                            print("Por favor ingresa un valor númerico")
                            cantidad = 0
                    elemento['Cantidad'] = cantidad
                    movimiento[1] = ID_tipo_de_movimiento
                    movimiento[2] = ID_almacen
                    movimiento[3] += cantidad
                    movimiento[4] += ((elemento['Importe sin IVA'] + elemento['IVA']) * cantidad * -1)
                    movimiento[5] = str(datetime.datetime.now().date())
                    movimiento[6] = str(datetime.datetime.now().time())
                    movimiento[8] = opcion
                    elementos.append(elemento)

                    continuar = 0
                    print("Selecciona la forma de proceder del sistema: \n")
                    print(" 1) Agregar otro Artículo")
                    print(" 2) Finalizar el Movimiento")
                    print(" 3) Cancelar")
                    while continuar not in [1,2,3]:

                        try:
                            continuar = int(input(f"\nSelecciona una opción: "))
                            if continuar not in [1,2,3]: 
                                print(f"Por favor ingresa una opción correcta")
                        except: 
                            print("Por favor ingresa un valor númerico")
                            continuar = 0
                    if continuar == 2: 
                        if len(elementos) > 0:
                            movimiento[7] = seleccionDeSocio(ID_tipo_de_movimiento)
                            movimiento[9] = opciones("DB", "Tipo de Pago.csv", 'tipo de pago', [1], False)[2]
                            movimiento[10] = opciones("DB", "Método de Pago.csv", 'método de pago', [1], False)[2]
                            movimiento[0] = aumentarSecuenciaMovimientos(ID_tipo_de_movimiento, ID_almacen)
                            for i in range(len(elementos)): 
                                elementos[i]['ID_movimiento'] = movimiento[0]
                            nuevoArchivo = elementosDeMovimientoTrasAgregar(elementos)
                            guardarModificaciones("Elemento de Movimiento.csv", nuevoArchivo)
                            nuevoArchivo = movimientoTrasAgregar(movimiento)
                            guardarModificaciones("Movimiento.csv", nuevoArchivo)
                            if ID_tipo_de_movimiento == 1:
                                for elemento in elementos:
                                    print(elemento['Cantidad'])
                                    impactarInventarios(ID_almacen, int(elemento['ID_articulo']), elemento['Cantidad'])
                            modoDeBusqueda = 0
                            print(f'\n¡Los movimientos han sido registrados con éxito!\n')
                        else:
                            print(f'No has añadido ningún artículo al movimiento. Por favor intenta nuevamente\n')
                else: 
                    continuar = 0

def registrarMovimientoPar(nombre : str, ID_tipo_de_movimiento : int, ID_almacen : int, movimiento_contrario : int) -> None: 
    # empleados = []
    # tiposDeMovimiento = [1, 2, 3, 4, 5]
    continuar = 0
    departamentos = [1,1,2,3]
    opcion = -1
    opcionesEmp = []
    modoDeBusqueda = 0
    elemento = {'ID_movimiento': '',
                'ID_articulo': '',
                'Descripción': '', 
                'Cantidad': '',
                'Importe sin Iva': '',
                'IVA': ''}
    elementos = []
    movimiento = [0,0,0,0,0,'','',0,0,0,0]
    while (opcion != len(opcionesEmp)):
        opcion = -1
        contador = 0
        opcionesEmp = []
        indices = []
        indice = 0
        with open("DB\Empleado.csv", "r", encoding = 'utf8') as documento: 
            lector = csv.DictReader(documento)
            for fila, linea in enumerate(lector):
                # print(linea)
                if int(linea['ID_almacen'] ) == ID_almacen and int(linea['ID_departamento']) == departamentos[ID_tipo_de_movimiento - 1]: 
                    contador += 1
                    if contador == 1:
                        print("Escoge el empleado encargado de este movimiento: \n")
                    # empleados.append(str(linea['Nombre'] + linea['Apellido Paterno'] + linea['Apellido Materno']))
                    print(f"\t{contador}) {find('Departamento.csv', 'ID_departamento', linea['ID_departamento'])[1]}: {str(linea['Nombre'] + ' ' + linea['Apellido Paterno'] + ' ' + linea['Apellido Materno'])}")
                    opcionesEmp.append(contador)
                    indices.append(int(linea['ID_empleado']))
        print()
        print(f'    {contador + 1}) Regresar')
        opcionesEmp.append(contador + 1)
        # print("Prueba 1")
        while opcion not in opcionesEmp:
            try:
                opcion = int(input("\nIngresa tu opción: "))
                if opcion not in opcionesEmp: 
                    print("Por favor ingresa una opción correcta")
            except: 
                print("Por favor ingresa un valor númerico")
                opcion = 0
        if opcion != len(opcionesEmp):
            modoDeBusqueda = 0
            while modoDeBusqueda != 3:
                print("""
                Ingrese su manera de búsqueda: 
                    
                    1) Por Menú de Búsqueda
                    2) Por Folio de Movimiento
                
                3) Regresar 
                    """)
                # print("Prueba 2")
                modoDeBusqueda = 0
                while modoDeBusqueda not in [1,2,3]:               
                    try:
                        modoDeBusqueda = int(input("\nIngresa tu opción: "))
                        if modoDeBusqueda not in [1,2,3]: 
                            print("Por favor ingresa una opción correcta")
                    except: 
                        print("Por favor ingresa un valor númerico")
                        modoDeBusqueda = 0
                if modoDeBusqueda == 1:
                    indice = movimientoMenu(nombre, ID_almacen, ID_tipo_de_movimiento, movimiento_contrario)
                elif modoDeBusqueda == 2:
                    indice = movimientosBusqueda(nombre, ID_almacen, ID_tipo_de_movimiento, movimiento_contrario)
                else: 
                    elementos = []
                    movimiento = [0,0,0,0,0,'','',0,0,0,0]
                # print("Prueba")            
                if indice != 0:
                    movimiento = find('Movimiento.csv', 'ID_movimiento', str(indice))
                    movimiento[1] = ID_tipo_de_movimiento
                    movimiento[3] = abs(float(movimiento[3]))
                    movimiento[5] = str(datetime.datetime.now().date())
                    movimiento[6] = str(datetime.datetime.now().time())
                    movimiento[8] = opcion
                    nuevoArchivo = movimientoTrasAgregar(movimiento)
                    guardarModificaciones("Movimiento.csv", nuevoArchivo)
                    with open("DB\Elemento de Movimiento.csv", "r", encoding = 'utf8') as documento:
                        lector = csv.DictReader(documento)
                        for linea in lector: 
                            if int(linea['ID_movimiento']) == indice: 
                                linea['Cantidad'] = abs(float(linea['Cantidad']))
                                elementos.append(linea)
                    nuevoArchivo = elementosDeMovimientoTrasAgregar(elementos)
                    guardarModificaciones("Elemento de Movimiento.csv", nuevoArchivo)      
                    for elemento in elementos:
                        print(elemento['Cantidad'])
                        impactarInventarios(ID_almacen, int(elemento['ID_articulo']), elemento['Cantidad'])
                    modoDeBusqueda = 3
                    print(f'\n¡Los movimientos han sido registrados con éxito!\n')

def existeMovimiento(almacen : int, ID_tipo_de_movimiento : int, ID_movimiento : int) -> bool:
    with open('DB\Movimiento.csv', "r", encoding = 'utf8') as documento:
        lector = csv.DictReader(documento)
        for linea in lector: 
            if int(linea['ID_almacén']) == almacen and int(linea['ID_movimiento']) == ID_movimiento and int(linea['ID_tipo_de_movimiento']) == ID_tipo_de_movimiento:
                return True
    return False


def movimientoMenu(nombre : str, almacen : int, ID_tipo_de_movimiento : int, movimiento_contrario : int) -> int:
    opciones = []
    indices = []
    opcion = 0
    contador = 0
    with open("DB\Movimiento.csv", "r", encoding = 'utf8') as documento: 
        lector = csv.DictReader(documento)
        for linea in lector: 
            if int(linea['ID_almacén']) == almacen and int(linea['ID_tipo_de_movimiento']) == movimiento_contrario and not existeMovimiento(almacen, ID_tipo_de_movimiento, int(linea['ID_movimiento'])):
                contador += 1
                if contador == 1: 
                    print(f"\nPor favor escoge una {nombre} correspondiente: \n")
                opciones.append(contador)
                indices.append(int(linea['ID_movimiento']))
                print(f'    {contador}) {nombre.title()}: {linea["ID_movimiento"]}')
                print(f'                Importe: {linea["Importe Total"]}')
    opciones.append(contador + 1)
    print()
    print(f'{contador + 1}) Regresar')
    while opcion not in opciones: 
        try: 
            opcion = int(input("Ingresa tu opción: "))
            if opcion not in opciones: 
                print(f'Por favor ingresa una opción correcta')
        except: 
            print(f'Por favor ingresa un valor númerico')
            opcion = 0
    if opcion != len(opciones):
        return indices[opcion - 1]
    return 0
    
    

def movimientosBusqueda(nombre : str, almacen : int, ID_tipo_de_movimiento : int, movimiento_contrario : int) -> int: 
    primeraOpcion = -1
    while primeraOpcion != 2: 
        print("\nEscoge una opción: ")
        print(" 1)  Generar {nombre.title()}")
        print(f" 2) Cancelar")
        while primeraOpcion not in [1,2]:
            try:
                primeraOpcion = int(input("\nIngresa tu opción: "))
                if primeraOpcion not in [1,2]:
                    print("Por favor ingresa una opción correcta")
            except:
                print("Por favor ingresa un valor númerico")
                primeraOpcion = 0
        if primeraOpcion == 1: 
            busqueda = 0
            while busqueda == 0: 
                try: 
                    busqueda = int(input(f"Ingresa el número de {nombre}: "))
                except: 
                    print("Por favor ingresa un valor númerico")
                    busqueda = 0
            with open("DB\Movimiento.csv", "r", encoding = 'utf8') as documento: 
                lector = csv.DictReader(documento)
                for linea in lector: 
                    if int(linea['ID_movimiento']) == busqueda and int(linea['ID_almacén']) == almacen and int(linea['ID_tipo_de_movimiento']) == movimiento_contrario and not existeMovimiento(almacen, ID_tipo_de_movimiento, busqueda):
                        return int(linea['ID_movimiento'])
            print(f"No existe una {nombre} correspondiente para realizar el movimiento deseado. Por favor valida tu información. ")
    return 0


def impactarInventarios(almacen : int, articulo : int, cantidad : int) -> None: 
    nuevoArchivo = []
    with open("DB\Existencia.csv", "r", encoding = 'utf8') as documento:
        lector = csv.reader(documento)
        for fila, linea in enumerate(lector):
            if fila != 0: 
                if int(linea[0]) == articulo and int(linea[1]) == almacen:
                    linea[2] = float(linea[2]) + cantidad
                    nuevoArchivo.append(linea)
                else:
                    nuevoArchivo.append(linea)
    guardarModificaciones("Existencia.csv", nuevoArchivo)


def movimientoTrasAgregar(movimiento : list) -> list:
    nuevoArchivo = []
    with open("DB\Movimiento.csv", "r", encoding = 'utf8') as documento:
        lector = csv.reader(documento)
        for fila, linea in enumerate(lector):
            if fila != 0: 
                nuevoArchivo.append(linea)
    nuevoArchivo.append(movimiento)
    return nuevoArchivo

def elementosDeMovimientoTrasAgregar(elementos : list) -> list:
    nuevoArchivo = []
    with open("DB\Elemento de Movimiento.csv", "r", encoding = 'utf8') as documento:
        lector = csv.reader(documento)
        for fila, linea in enumerate(lector):
            if fila != 0: 
                nuevoArchivo.append(linea)
    for elemento in elementos: 
        nuevoArchivo.append([elemento['ID_movimiento'], elemento['ID_articulo'], elemento['Descripcion'], elemento['Cantidad'], elemento['Importe sin Iva'], elemento['IVA']])
    return nuevoArchivo

def aumentarSecuenciaMovimientos(ID_tipo_de_movimiento : int, ID_almacen : int) -> int:
    retorno = 1
    nuevoArchivo = []
    with open("DB\Secuencia de Movimientos.csv", "r", encoding = 'utf8') as documento:
        lector = csv.reader(documento)
        for fila, linea in enumerate(lector):
            if fila != 0: 
                if int(linea[1]) == ID_almacen and int(linea[2]) == ID_tipo_de_movimiento:
                    retorno = int(linea[3]) + 1
                    linea[3] = retorno
                    nuevoArchivo.append(linea)
                else:
                    nuevoArchivo.append(linea)
        guardarModificaciones('Secuencia de Movimientos.csv', nuevoArchivo)
    return retorno

def seleccionDeSocio(ID_tipo_de_movimiento : int) -> int:
    movimientos = [2,2,1,1]
    opciones = []
    indices = []
    contador = 0
    opcion = 0
    with open("DB\Socio de Negocios.csv", "r", encoding = 'utf8') as documento:
        lector = csv.DictReader(documento)
        for linea in lector:
            if int(linea['ID_tipo_de_socio']) == movimientos[ID_tipo_de_movimiento - 1]:
                contador += 1
                if contador == 1:
                    print("Por favor escoge un socio de negocios: \n")
                print(f'    {contador}) Razón Social: {linea["Razón Social"]}')
                print(f'                RFC: {linea["RFC"]}')
                opciones.append(contador)
                indices.append(int(linea['ID_socio']))
    print()
    opcion = 0
    while opcion not in opciones:
        try: 
            opcion = int(input("Ingresa tu opción: "))
            if opcion not in opciones: 
                print("Por favor ingresa una opción correcta")
        except:
            print("Por favor ingresa un valor númerico")
            opcion = 0
    return indices[opcion - 1]

def busquedaPorMenu(almacen : int) -> str: 
    opciones = []
    indices = []
    opcion = 0
    indice = "0"
    contador = 0
    disponible = True
    with open("DB\Articulo.csv", "r", encoding = 'utf8') as documento: 
        lector = csv.DictReader(documento)
        for linea in lector: 
            if tieneExistencias(int(linea['ID_articulo']), almacen):
                contador += 1
                print(f'    {contador}) Código de Barras: {linea["Código de Barras"]}')
                print(f"\t\tDescripción: {linea['Descripción']}")
                print(f"\t\tPrecio: {(float(linea['Precio de Venta sin IVA']) * (1 + (int(find('IVA.csv', 'ID_IVA', linea['ID_IVA'])[2]) / 100))):.2f}")
                opciones.append(contador)
                indices.append(linea['ID_articulo'])
        opciones.append(contador + 1)
        print()
        print(f'{contador + 1}) Regresar')
    while opcion not in opciones:
        try:
            opcion = int(input("\nIngresa tu opción: "))
            if opcion not in opciones: 
                print("Por favor ingresa una opción correcta")
        except: 
            print("Por favor ingresa un valor númerico")
            opcion = 0
    if opcion != len(opciones):        
        indice = indices[opcion - 1]
    return indice
    

def busquedaPorCodigo(almacen : int) -> str:
    primeraOpcion = -1
    while primeraOpcion != 2: 
        print("\nEscoge una opción: ")
        print(" 1) Buscar")
        print(" 2) Regresar")
        while primeraOpcion not in [1,2]:
            try:
                primeraOpcion = int(input("\nIngresa tu opción: "))
                if primeraOpcion not in [1,2]:
                    print("Por favor ingresa una opción correcta")
            except:
                print("Por favor ingresa un valor númerico")
                primeraOpcion = 0
        if primeraOpcion == 1: 
            disponible = False
            while disponible == False:
                busqueda = input("Ingresa el código de barras: ")
                while busqueda == "" or busqueda == " " or busqueda.strip() == "":
                    busqueda = input("Ingresa el código de barras: ")                    
                articulos = []
                opciones = []
                indices = []
                opcion = 0
                indice = "0"
                contador = 0
                disponible = True
                with open("DB\Articulo.csv", "r", encoding = 'utf8') as documento: 
                    lector = csv.DictReader(documento)
                    for linea in lector: 
                        if linea['Código de Barras'].strip() == busqueda.strip() and tieneExistencias(int(linea['ID_articulo']), almacen):
                            contador += 1
                            articulos.append(linea)
                            opciones.append(contador)
                            indices.append(linea['ID_articulo'])
                if len(articulos) > 1: 
                    print('Hay varios articulos con el mismo código. Por favor escoge el correcto: ')
                    print()
                    cOpcion = ''        
                    for i in range(contador):
                        cOpcion += f"{contador + 1}) Descripción: {articulos[i]['Descripción']} \tPrecio: {(float(articulos[i]['Precio de Venta sin IVA']) * (1 + (int(find('IVA.csv', 'ID_IVA', linea['ID_IVA'])[2]) / 100))):.2f}\n"
                    print(cOpcion)
                    while opcion not in opciones:
                        try:
                            opcion = int(input("\nIngresa tu opción: "))
                            if opcion not in opciones: 
                                print("Por favor ingresa una opción correcta")
                        except: 
                            print("Por favor ingresa un valor númerico")
                            opcion = 0
                    indice = indices[opcion - 1]
                elif len(articulos) == 1:  
                    indice = indices[0]
                else:
                    disponible = False
            return indice
    return "0"
        

def tieneExistencias(ID_articulo : int, ID_almacen : int) -> int: 
    existencia = 0
    with open("DB\Existencia.csv", "r", encoding = 'utf8') as documento:
        lector = csv.DictReader(documento)
        for linea in lector:
            if int(linea['ID_articulo']) == ID_articulo and int(linea['ID_almacen']) == ID_almacen:
                existencia = float(linea['Cantidad'])
    return existencia

if __name__ == '__main__':
#    registrarMovimiento(1,1)
    registrarMovimientoPar("devolución", 2, 1, 1)