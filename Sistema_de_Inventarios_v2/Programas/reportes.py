import csv
from Funciones import *

def historicoDeMovimientos(almacen : int) -> None: 
    reporte = []
    with open("DB\Movimientos.csv", "r", encoding = 'utf8') as documento: 
        lector = csv.DictReader(documento)
        for linea in lector: 
            if int(linea['ID_almacen']) == almacen and int(linea['ID_tipo_de_movimiento']) != 3: 
                registro = [0 for i in range(12)]
                registro[0] = find('Almacén.csv', 'ID_almacen', almacen)
                registro[1] = find('Almace')

                reporte.append(registro)
                
    guardarModificaciones("Reporte Historico de Movimientos.csv", reporte, carpeta = 'Reportes')

def inventarios(almacen : int) -> None:
    pass

def ventasPorVendedor(almacen : int) -> None:
    pass

if __name__ == '__main__':
    pass
