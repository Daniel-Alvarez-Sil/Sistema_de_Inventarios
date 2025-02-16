from Funciones import *
from agregar import *
from modificar import *
from eliminar import *
from movimientos import *


def home() -> None: 
    mensajeInicial()
    while (opcioninicial := obtenerOpcionInicial()[0] != 2):
        almacen = 0
        while (almacen != 3):
            almacen = obtenerAlmacen()[0]
            if almacen == 3:
                continue
            modulo = 0
            while (modulo != 9):
                opcionActual = 0
                modulo = obtenerModulo()[0]
                match modulo:
                    case 1:
                        registrarMovimiento(1,almacen)
                    case 2:
                        registrarMovimientoPar("devolución", 2, almacen, 1)
                    case 3:
                        registrarMovimiento(3, almacen)         
                    case 4:
                        registrarMovimientoPar("entrada de mercancía", 4, almacen, 3)            
                    case 5:
                        pass
                    case 6:
                        while (opcionActual != 4):
                            opcionActual = obtenerOpcionSociosDeNegocios()[0]
                            match opcionActual:
                                case 1:
                                    agregarRegistro('Socio de Negocios.csv', camposSocioDeNegocio(), 'Socio de Negocios')
                                case 2:
                                    modificarRegistro('Socio de Negocios.csv', 'ID_socio', camposSocioDeNegocio(), [3,10,13], 'Socio de negocios', 'socio de negocios')
                                case 3:
                                    eliminarRegistro("DB", "Socio de Negocios.csv", "socio de negocios", [3,10,13], True, ['Movimiento.csv'], "ID_socio")
                    case 7:
                        while (opcionActual != 4):
                            opcionActual = obtenerOpcionEmpleados()[0]
                            match opcionActual:
                                case 1:
                                    agregarRegistro('Empleado.csv', camposEmpleado(), 'Empleado', almacen)
                                case 2:
                                    modificarRegistro('Empleado.csv', 'ID_empleado', camposEmpleado(), [3,4,5], 'Empleado', 'Empleado', almacen)
                                case 3:
                                    eliminarRegistro("DB", "Empleado.csv", "empleado", [3,4,5], True, ['Movimiento.csv'], "ID_empleado", almacen)          
                    case 8:
                        while (opcionActual != 4):
                            opcionActual = obtenerOpcionArticulos()[0]
                            match opcionActual:
                                case 1:
                                    agregarRegistro('Articulo.csv', camposArticulo(), 'Artículo')
                                case 2:
                                    modificarRegistro('Articulo.csv', 'ID_articulo', camposArticulo(), [1,2,6], 'Artículo', 'artículo')
                                case 3:
                                    eliminarRegistro("DB", "Articulo.csv", "articulo", [1,2,6], True, ['Elemento de Movimiento.csv', 'Existencia.csv'], "ID_articulo")
                      
    print("¡Gracias por usar el sistema! Por favor vuelva pronto. \n\n") 

home()            
