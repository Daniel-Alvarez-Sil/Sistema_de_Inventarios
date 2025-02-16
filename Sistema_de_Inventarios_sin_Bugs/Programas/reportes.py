import csv
from Funciones import *
from movimientos import tieneExistencias

# Este procedimiento genera un reporte de inventarios
def inventarios(almacen : int) -> None:
    inventarios = []
    with open("DB\Existencia.csv", "r", encoding = 'utf8') as documento: 
        lector = csv.DictReader(documento)
        for linea in lector: 
            if int(linea['ID_almacen']) == almacen:
                lista = []
                articulo = find("Articulo.csv", 'ID_articulo', linea['ID_articulo'])
                lista.append(articulo[1])
                lista.append(articulo[2])
                lista.append(find("Almacén.csv", 'ID_almacen', linea['ID_almacen'])[1])
                lista.append(linea['Cantidad'])
                inventarios.append(lista)
    print(inventarios)
    print(type(inventarios))
    guardarModificaciones("Reporte de Inventarios.csv", inventarios, 'Reportes')

# Este procedimiento genera un reporte de ventas dandole prioridad a los campos del vendedor
def ventasPorVendedor(almacen : int) -> None:
    ventas = []
    movimiento = 0
    with open("DB\Movimiento.csv", "r", encoding = 'utf8') as documento1: 
        lector1 = csv.DictReader(documento1)
        for linea1 in lector1:
            if int(linea1['ID_tipo_de_movimiento']) == 1 and int(linea1['ID_almacén']) == almacen:
                # print(linea1)
                movimiento = int(linea1['ID_movimiento'])
                with open("DB\Elemento de Movimiento.csv", "r", encoding = 'utf8') as documento2:
                    lector2 = csv.DictReader(documento2)
                    for linea2 in lector2:
                        if int(linea2['ID_tipo_de_movimiento']) == 1 and int(linea2['ID_movimiento']) == movimiento and int(linea2['ID_almacen']) == almacen: 
                            lista = []
                            empleado = find("Empleado.csv", 'ID_empleado', linea1['ID_empleado'])
                            # print(empleado)
                            articulo = find("Articulo.csv", 'ID_articulo', linea2['ID_articulo'])
                            lista.append(empleado[3])
                            lista.append(empleado[4])
                            lista.append(linea1['Fecha'])
                            lista.append(movimiento)
                            lista.append(find("Almacén.csv", "ID_almacen", linea2['ID_almacen'])[1])
                            lista.append(articulo[1])
                            lista.append(articulo[2])
                            lista.append(linea2['Importe sin Iva'])
                            lista.append(linea2['IVA'])
                            lista.append(linea2['Cantidad'])
                            ventas.append(lista) 
    guardarModificaciones("Reporte de Ventas por Vendedor.csv", ventas, "Reportes")
    print("\nEl reporte ha sido generado y guardado con éxito\n")                            

# Este procedimiento genera un reporte de ventas dandole prioridad a los campos del artículo
def ventasPorArticulo(almacen : int) -> None:
    ventas = []
    movimiento = 0
    with open("DB\Movimiento.csv", "r", encoding = 'utf8') as documento1: 
        lector1 = csv.DictReader(documento1)
        for linea1 in lector1:
            if int(linea1['ID_tipo_de_movimiento']) == 1 and int(linea1['ID_almacén']) == almacen:
                # print(linea1)
                movimiento = int(linea1['ID_movimiento'])
                with open("DB\Elemento de Movimiento.csv", "r", encoding = 'utf8') as documento2:
                    lector2 = csv.DictReader(documento2)
                    for linea2 in lector2:
                        if int(linea2['ID_tipo_de_movimiento']) == 1 and int(linea2['ID_movimiento']) == movimiento and int(linea2['ID_almacen']) == almacen: 
                            lista = []
                            # print(empleado)
                            articulo = find("Articulo.csv", 'ID_articulo', linea2['ID_articulo'])
                            lista.append(articulo[0])
                            lista.append(articulo[1])
                            lista.append(articulo[2])
                            lista.append(linea1['Fecha'])
                            lista.append(movimiento)
                            lista.append(find("Almacén.csv", "ID_almacen", linea2['ID_almacen'])[1])
                            lista.append(linea2['Importe sin Iva'])
                            lista.append(linea2['IVA'])
                            lista.append(linea2['Cantidad'])
                            ventas.append(lista) 
    guardarModificaciones("Reporte de Ventas por Artículo.csv", ventas, "Reportes")          
    print("\nEl reporte ha sido generado y guardado con éxito\n")                                 

# Este procedimiento genera un reporte de ventas con el mayor nivel de detalle
def ventas(almacen : int) -> None:
    ventas = []
    movimiento = 0
    with open("DB\Movimiento.csv", "r", encoding = 'utf8') as documento1: 
        lector1 = csv.DictReader(documento1)
        for linea1 in lector1:
            if int(linea1['ID_tipo_de_movimiento']) == 1 and int(linea1['ID_almacén']) == almacen:
                # print(linea1)
                movimiento = int(linea1['ID_movimiento'])
                with open("DB\Elemento de Movimiento.csv", "r", encoding = 'utf8') as documento2:
                    lector2 = csv.DictReader(documento2)
                    for linea2 in lector2:
                        if int(linea2['ID_tipo_de_movimiento']) == 1 and int(linea2['ID_movimiento']) == movimiento and int(linea2['ID_almacen']) == almacen: 
                            lista = []
                            # print(empleado)
                            articulo = find("Articulo.csv", 'ID_articulo', linea2['ID_articulo'])
                            lista.append(movimiento)
                            lista.append(find("Almacén.csv", "ID_almacen", linea2['ID_almacen'])[1])
                            lista.append("Venta")
                            lista.append(linea1['Fecha'])
                            lista.append(linea1['Hora'][:8])
                            lista.append(articulo[2])
                            lista.append(articulo[1])
                            lista.append(linea2['Cantidad'])
                            lista.append(linea2['Importe sin Iva'])
                            lista.append(linea2['IVA'])
                            lista.append(find("Tipo de Pago.csv", "ID_tipo_de_pago", linea1['ID_tipo_de_pago'])[1])
                            lista.append(find("Método de Pago.csv", "ID_método_de_pago", linea1['ID_método_de_pago'])[1])                            
                            ventas.append(lista) 
    guardarModificaciones("Reporte de Ventas.csv", ventas, "Reportes")          
    print("\nEl reporte ha sido generado y guardado con éxito\n")                                 

# Este procedimiento permite consultar las existencias de un artículo dentro del sistema
def consultarInventario(almacen : int) -> None: 
    print("Escoge un artículo para revisar su existencia: \n")
    opcionArticulo = opciones("DB", "Articulo.csv", "artículo", [2,1], True)[1]
    print(f"El artículo cuenta con {tieneExistencias(int(opcionArticulo), almacen)} piezas en el almacen. ")

# Este procedimiento permite consultar el detalle de una venta dentro del sistema
def consultarVenta(almacen : int) -> None:
    opcionVenta = 0
    contador = 0
    opciones = []
    indices = []
    print("Por favor escoge una venta: \n")
    with open("DB\Movimiento.csv", "r", encoding = 'utf8') as documento:
        lector = csv.DictReader(documento)
        for linea in lector: 
            if int(linea['ID_tipo_de_movimiento']) == 1 and int(linea['ID_almacén']) == almacen:
                contador += 1
                print(f'\t{contador}) Folio: {linea["ID_movimiento"]} - Total: {linea["Importe Total"]}')
                opciones.append(contador)
                indices.append(linea['ID_movimiento'])

    opciones.append(contador + 1)
    print(f'\n{len(opciones)}) Regresar')

    while opcionVenta not in opciones:
        try: 
            opcionVenta = int(input("Ingresa una opción: "))
            if opcionVenta not in opciones:
                print("Por favor ingresa una opción correcta")
        except:
            print("Por favor ingresa un valor númerico: ")
            opcionVenta = 0
    
    if opcionVenta != len(opciones): 
         indice = int(indices[opcionVenta - 1])
         with open("DB\Movimiento.csv", "r", encoding = 'utf8') as documento1:
             lector1 = csv.DictReader(documento1)
             for linea1 in lector1: 
                 if int(linea1['ID_tipo_de_movimiento']) == 1 and int(linea1['ID_almacén']) == almacen and int(linea1['ID_movimiento']) == indice:
                    with open("DB\Elemento de Movimiento.csv", "r", encoding = 'utf8') as documento:
                                lector = csv.DictReader(documento)
                                for linea in lector:
                                    if int(linea['ID_tipo_de_movimiento']) == 1 and int(linea['ID_movimiento']) == indice and int(linea['ID_almacen']) == almacen: 
                                        # print(empleado)
                                        print("\nDetalle de la venta: ")
                                        articulo = find("Articulo.csv", 'ID_articulo', linea['ID_articulo'])
                                        print(f'\t\tFolio: {indice}')
                                        print(f'\t\tAlmacén: {find("Almacén.csv", "ID_almacen", linea["ID_almacen"])[1]} ')
                                        print(f"\t\tFecha: {linea1['Fecha']}")
                                        print(f"\t\tHora: {linea1['Hora'][:8]}")
                                        print(f'\t\tArticulo: {articulo[2]}')
                                        print(f'\t\tCódigo de Barras: {articulo[1]}')
                                        print(f"\t\tCantidad: {linea['Cantidad']}")
                                        print(f"\t\tImporte sin Iva: {linea['Importe sin Iva']}")
                                        print(f"\t\tIVA: {linea['IVA']}")
                                        print(f'\t\tTipo de Pago: {find("Tipo de Pago.csv", "ID_tipo_de_pago", linea1["ID_tipo_de_pago"])[1]}')
                                        print(f'\t\tMétodo de Pago: {find("Método de Pago.csv", "ID_método_de_pago", linea1["ID_método_de_pago"])[1]}')     


if __name__ == '__main__':
    # inventarios(1)
    # ventasPorVendedor(1)
    # ventasPorArticulo(1)
    # ventas(1)
    # consultarInventario(1)
    consultarVenta(1)
