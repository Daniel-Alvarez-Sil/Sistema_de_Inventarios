from Funciones import *
from agregar import *
from modificar import *
from eliminar import *


def home() -> None: 
    mensajeInicial()
    while (opcioninicial := obtenerOpcionInicial()[0] != 2):
        almacen = 0
        while (almacen != 3):
            almacen = obtenerAlmacen()[0]
            if almacen == 3:
                continue
            modulo = 0
            while (modulo != 10):
                opcionActual = 0
                modulo = obtenerModulo()[0]
                match modulo:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass            
                    case 4:
                        pass            
                    case 5:
                        pass
                    case 6:
                        while (opcionActual != 4):
                            opcionActual = obtenerOpcionSociosDeNegocios()[0]
                            match opcionActual:
                                case 1:
                                    agregarRegistro('Socio de Negocios.csv', camposSocioDeNegocio(), 'Socio de Negocios')
                                case 2:
                                    modificarRegistro('Socio de Negocios.csv', 'ID_socio', camposSocioDeNegocio(), 3, 'Socio de negocios', 'socio de negocios')
                                case 3:
                                    eliminarRegistro("DB", "Socio de Negocios.csv", "socio de negocios", 3, True, ['Movimiento.csv'], "ID_socio")
                    case 7:
                        while (opcionActual != 4):
                            opcionActual = obtenerOpcionEmpleados()[0]
                            match opcionActual:
                                case 1:
                                    agregarRegistro('Empleado.csv', camposEmpleado(), 'Empleado', almacen)
                                case 2:
                                    modificarRegistro('Empleado.csv', 'ID_empleado', camposEmpleado(), 3, 'Empleado', 'Empleado', almacen)
                                case 3:
                                    eliminarRegistro("DB", "Empleado.csv", "empleado", 3, True, ['Movimiento.csv'], "ID_empleado", almacen)          
                    case 8:
                        while (opcionActual != 4):
                            opcionActual = obtenerOpcionArticulos()[0]
                            match opcionActual:
                                case 1:
                                    agregarRegistro('Articulo.csv', camposArticulo(), 'Artículo')
                                case 2:
                                    modificarRegistro('Articulo.csv', 'ID_articulo', camposArticulo(), 2, 'Artículo', 'artículo')
                                case 3:
                                    eliminarRegistro("DB", "Articulo.csv", "articulo", 2, True, ['Elemento de Movimiento.csv', 'Existencia.csv'], "ID_articulo")

                    case 9:
                        pass                       
    print("¡Gracias por usar el sistema! Por favor vuelva pronto. \n\n") 

home()            
