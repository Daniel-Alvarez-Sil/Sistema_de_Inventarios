import csv

# Mensaje Inicial del Sistema
def mensajeInicial() -> None:
    print("""
¡Bienvenido al Sistema de la Tienda!                       
""")
    
# Impresión de Opciones de cualquier Menú 
def opciones(carpeta : str, archivo : str, seleccion : str, indice : int, regresar : bool, almacen : int = 0) -> list:
    print(f"Selecciona un {seleccion}: \n")
    opciones = []
    indices = []
    opcion = 0
    contador = 0
    with open(f'{carpeta}\{archivo}', "r", encoding = 'utf8') as documento:
        lector = csv.reader(documento)
        
        for fila, linea in enumerate(lector):
            # print(linea)
            if fila != 0:
                if almacen == 0: 
                    contador += 1
                    print(f'    {contador}) {linea[indice]}')                    
                    opciones.append(contador)
                    indices.append(linea[0])
                else: 
                    if int(linea[titulos(carpeta, archivo).index("ID_almacen")]) == almacen: 
                        contador += 1
                        print(f'    {contador}) {linea[indice]}')                        
                        opciones.append(contador)
                        indices.append(linea[0])
    if regresar == True:
        opciones.append(len(opciones) + 1)
        print(f'\n  {len(opciones)}) Regresar')
        # if opcion == len(opciones):
        #     indice = -1
        # else:
        #   indice = indices[opcion -1]
    while(opcion not in opciones):
        try:
            opcion = int(input("\nIngresa tu opción: "))
            if opcion not in opciones: 
                print("Por favor ingresa una opción correcta")
        except: 
            print("Por favor ingresa una opción correcta")
            opcion = 0
    print()
    # print(opciones)
    # print(indices)
    if regresar == False:
        return opcion, indices[opcion - 1], len(opciones)
    else:
        if opcion == len(opciones):
            return opcion, -1, len(opciones)
        else:
            return opcion, indices[opcion - 1], len(opciones)

# Redundancia de la función anterior para facilitar sintáxis
def obtenerAlmacen(carpeta : str = "DB", archivo : str = "Almacén.csv", seleccion : str = "almacén", indice : int = 1, regresar : bool = True) -> int:
    return opciones(carpeta, archivo, seleccion, indice, regresar)

def obtenerModulo(carpeta : str = "Menus", archivo : str = "Menú Principal.csv", seleccion : str = "módulo", indice : int = 1, regresar : bool = True) -> int:
    return opciones(carpeta, archivo, seleccion, indice, regresar)

def obtenerOpcionInicial(carpeta : str = "Menus", archivo : str = "Menú Inicial.csv", seleccion : str = "apartado", indice : int = 1, regresar : bool = False) -> int:
    return opciones(carpeta, archivo, seleccion, indice, regresar)

def obtenerOpcionArticulos(carpeta : str = "Menus", archivo : str = "Menú de Artículos.csv", seleccion : str = "apartado de artículos", indice : int = 1, regresar : bool = True) -> int:
    return opciones(carpeta, archivo, seleccion, indice, regresar)

def obtenerOpcionSociosDeNegocios(carpeta : str = "Menus", archivo : str = "Menú de Socios de Negocios.csv", seleccion : str = "apartado de socio de negocios", indice : int = 1, regresar : bool = True) -> int:
    return opciones(carpeta, archivo, seleccion, indice, regresar)

def obtenerOpcionEmpleados(carpeta : str = "Menus", archivo : str = "Menú de Empleados.csv", seleccion : str = "apartado de empleados", indice : int = 1, regresar : bool = True) -> int:
    return opciones(carpeta, archivo, seleccion, indice, regresar)


def obtenerArtículo(carpeta : str = "DB", archivo : str = "Articulo.csv", seleccion : str = "artículo", indice : int = 2, regresar : bool = True) -> int:
    return opciones(carpeta, archivo, seleccion, indice, regresar)

# Conseguimos los nombres de los campos de las tablas (los títulos de los archivos CSV)
def titulos(carpeta : str, archivo : str) -> list:
    titulos = []
    with open(f"{carpeta}\{archivo}", "r", encoding = 'utf8') as documento:
        lector = csv.reader(documento)
        for linea in lector:
            for campo in linea:
                titulos.append(campo)
            return titulos

# Guardamos cualquier cambio realizado (adición, modificación o eliminación)
def guardarModificaciones(archivo : str, modificaciones : list) -> None:
    headers = titulos('DB', archivo)
    with open(f'DB\{archivo}', "w", newline = '', encoding = "utf8") as documento:
        escritor = csv.writer(documento)
        # print(archivo)
        # print([headers] + modificaciones)
        escritor.writerows([headers] + modificaciones)

# Find - Nos ayuda a encontrar un registro en cualquier archivo CSV (tabla)
def find(archivo : str, campoCondicion : str, condicion : str) -> bool:
    # print(type(condicion))
    indice = 0
    with open(f'DB\{archivo}', "r", encoding = "utf8") as documento:
        lector = csv.reader(documento)
        for fila, linea in enumerate(lector):
            if fila == 0:
                for index, campo in enumerate(linea): 
                    # print(f"{campo} - {campoCondicion}")
                    if campo == campoCondicion:
                        indice = index
            else:
                if linea[indice] == condicion:
                    # return True
                    return list(linea)
    # return False
    return []   

# Conseguimos el número de líneas del archivo CSV, incluyendo el título
def longitud(carpeta : str, archivo: str) -> int:
    largo = 0
    with open(f'{carpeta}\{archivo}', 'r', encoding='utf8') as documento:
        lector = csv.reader(documento)
        for linea in documento:
            largo += 1
    return largo

# Campos de Lista
# Establecemos los campos necesarios para la adición o modificación de registros a un archivo CSV
def camposArticulo() -> list:
    return [[],'Código de Barras', 'Descripción', [], ['Porcentaje de Utilidad', 'Utilidad.csv', 1, 'ID_utilidad'], ['Tipo de IVA', 'IVA.csv', 1, 'ID_IVA'], [], ['Multiplo de Venta', "float"]]

def camposSocioDeNegocio() -> list:
    return [[], ['Tipo de Socio', 'Tipo de Socio.csv', 1, 'ID_tipo_de_socio'], ['Tipo de Persona', 'Persona.csv', 1, 'ID_persona'], 'Razón Social', ['CP', 'int'], 'Calle', 'Numero Exterior', 'Numero Interior', 'Colonia', 'Estado', 'RFC', ['Régimen Fiscal', 'Régimen Fiscal.csv', 1, 'ID_régimen_fiscal'], ['Uso de CFDI', 'Uso de CFDI.csv', 1, 'ID_uso_de_CFDI'], "Nombre de Contacto", "Teléfono de Contacto", "Correo de Contacto"]

def camposEmpleado() -> list:
    return [[], 'Almacen', ['Departamento', 'Departamento.csv', 1, 'ID_departamento'], 'Nombre', 'Apellido Paterno', 'Apellido Materno']

# Con esta función, aumentamos las secuencias que nos ayudan a manejar los IDs de los archivos CSVs
def aumentarSecuencia(condicion : str, paso : int) -> int:
    retorno = 1
    nuevoArchivo = []
    with open("DB\Secuencia.csv", "r", encoding = 'utf8') as documento:
        lector = csv.reader(documento)
        for fila, linea in enumerate(lector):
            if fila != 0: 
                if linea[1] == condicion:
                    retorno = int(linea[2]) + paso
                    linea[2] = retorno
                    nuevoArchivo.append(linea)
                else:
                    nuevoArchivo.append(linea)
        guardarModificaciones('Secuencia.csv', nuevoArchivo)
    return retorno

def aumentarSecuenciaMovimientos(archivo, ) -> int:
    pass

    


        
    
