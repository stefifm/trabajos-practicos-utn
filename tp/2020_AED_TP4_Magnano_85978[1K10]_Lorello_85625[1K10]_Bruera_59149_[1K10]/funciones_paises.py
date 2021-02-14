"""
Aquí están las funciones para el programa principal del trabajo práctico
"""


import os.path
import pickle
import random

import registro_confederacion
import registro_paises
from registro_confederacion import Confederacion


# ------------------------------------------------------------------------------
# Funciones de interfaz

# Stop
def enter():
    Enter = input("\x1b[1;36m"+"Presione enter para continuar..."+"\x1b[0;m")




# ------------------------------------------------------------------------------
# Sector de validaciones y conversiones


# Función para validar las confederaciones y opciones
def validar_rango(inf, sup, mensaje):
    """
    Valida si un número está en cierto rango
    :param inf: Un número que marca el inicio del rangp
    :param sup: Otro número que indica el final del rango
    :param mensaje: Un mensaje cualquiera
    :return: El número que puede estar dentro del rango y si no, marca error
    """
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("\n\033[1;31m"+"Valor no válido. Ingrese un valor entre",str(inf),"y",
                  str(sup) + "\033[0;m\n")
    return n


# Funcion para validar que el anfitrión está en la lista
def validar_anfitrion(vec_paises):
    """
    Hace una validación de si el anfitrión está en el vector países
    :param vec_paises: Vector original de países
    :return: el anfitrión ya validado
    """
    print("\033[1;30m"+"Le daremos la oportunidad de elegir el anfitrion del mundial.\n"
          "Usted debe ingresarlo (como todo nombre propio) con la primer letra en mayuscula.\n"+"\033[0;m")
    anfi = input("\033[1;30m"+"Ingrese el país anfitrión: "+"\033[0;m")
    paises = [pais.nombre for pais in vec_paises]
    while anfi not in paises:
        print("\n\t\t\t\033[1;31m"+"No se encuentra en la lista.\n"
              "Por favor, revise la forma en la que escribio el pais.\n"+ "\033[0;m")
        anfi = input("\033[1;30m"+"Ingrese el país anfitrión: "+"\033[0;m")
    return anfi


def convertir_num_letra_grupo(j):
    """
    Convierte un número en letra de un grupo
    :param j: el número del 0 al 7
    :return: la cadena ya convertida
    """
    if 0 > j > 8:
        return "Valor inválido."
    grupos = ("A", "B", "C", "D", "E", "F", "G", "H")
    return grupos[j]


def convertir_num_conf(i):
    """
    Convierte un número de codificación de una confederación en cadena
    :param i: el código de confederación
    :return: la cadena ya transformada
    """
    if 0 > i > 5:
        return "\033[1;31m"+"Valor inválido." +"\033[0;m\n"
    confederacion = ("UEFA", "CONMEBOL", "CONCACAF", "CAF", "AFC", "OFC")
    return confederacion[i]


# ------------------------------------------------------------------------------
# Orden de mayor a menor con add_in_order


def add_in_order(vec_paises, paises):
    """
    Usa el algoritmo de búsqueda binaria para ordenar de mayor a menor y luego
    los carga en el vector
    :param vec_paises: vector de países que todavía no se generó
    :param paises: una variable que contiene las líneas previamente
    transformadas en cadenas del registro Países
    :return: None
    """
    n = len(vec_paises)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if vec_paises[c].puntos == paises.puntos:
            pos = c
            break
        if paises.puntos > vec_paises[c].puntos:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec_paises[pos:pos] = [paises]


def cargar_vector(fd, vec_paises):
    """
    Se hace la carga del vector, abriendo el archivo de texto,
    transformándolo en cadena de registros y finalmente, se carga al vector
    :param fd: el archivo de texto
    :param vec_paises: vector de países que se recibirá el contenido del
    archivo prevuamente convertido en cadena
    :return: vector países
    """
    if not os.path.exists(fd):
        print("El archivo no existe.")
        return None

    m = open(fd, "rt", encoding="utf-8")
    linea = m.readline()
    while linea != "":
        if linea[-1] == "\n":
            linea = linea[:-1]
        if linea != "" and linea[0] != "#":
            paises = registro_paises.csv_to_linea(linea)
            add_in_order(vec_paises, paises)
        linea = m.readline()
    m.close()


def mostrar_vector_paises(vec_paises):
    for i in range(len(vec_paises)):
        print(registro_paises.to_string_paises(vec_paises[i]))


# Opcion 2: busca el mayor

def mayor(vec_paises):
    """
    Hace una búsqueda del mayor. Si hay más mayores, los carga en el vector
    mayores
    :param vec_paises: vector original de países
    :return: El vector de mayores
    """
    mayor = None
    for paises in vec_paises:
        if mayor is None or paises.campeonatos > mayor:
            mayor = paises.campeonatos
    mayores = []
    for paises in vec_paises:
        if paises.campeonatos == mayor:
            mayores.append(paises)
    return mayores


# Opcion 3: vector de conteo

def contador_paises_campeonatos(vec):
    """
    Carga un vector de conteo para saber la cantidad de países que consiguieron
    campeonatos por cada confederación
    :param vec: el vector original de países
    :return: vector de conteo
    """
    cont_camp = [0] * 6
    for i in range(len(vec)):
        c = int(vec[i].confederacion)
        if vec[i].campeonatos > 0:
            cont_camp[c] += 1
    for i in range(6):
        print(str(i) + "." + convertir_num_conf(i) + " ====> " + "Cantidad "                                    
            "de países con campeonatos: " + str(cont_camp[i]))


# Opcion 4

def vector_confederacion(vec_paises, x):
    """
    Aquí se arma el vector de una confederación X que se ingresa por teclado
    :param vec_paises: vector original de países
    :param x: el código de una confederación
    :return: vector de una confederación X
    """
    vec_conf = []
    for i in range(len(vec_paises)):
        if vec_paises[i].confederacion == x:
            nombre = vec_paises[i].nombre
            puntos = vec_paises[i].puntos
            campeonatos = vec_paises[i].campeonatos
            confederacion = Confederacion(nombre, puntos, campeonatos)
            vec_conf.append(confederacion)
    return vec_conf


def orden_sort(vec_conf):
    """
    Ordena de mayor a menor el vector confederación mediante el algoritmo de
    selección directa
    :param vec_conf: vector de confederación X
    :return: None
    """
    n = len(vec_conf)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vec_conf[i].puntos < vec_conf[j].puntos:
                vec_conf[i], vec_conf[j] = vec_conf[j], vec_conf[i]


def grabar_archivo_confederacion(vec_confederacion, archivo):
    """
    Graba un archivo a partir de un vector de confederación previamente armado
    :param vec_confederacion: vector confederación
    :param archivo: el archvio con una confederación X.
    :return: None
    """
    m = open(archivo, "wb")
    c = 0
    for i in range(len(vec_confederacion)):
        pickle.dump(vec_confederacion[i], m)
        c += 1
    print("\033[1;30m"+"El archivo", archivo, "está cargado","y se grabaron",c,"registros."+"\033[0;m")
    m.close()


# Opcion 5

def mostrar_archivo(archivo):
    """
    Muestra el archivo de una confederación
    :param archivo: archivo confederación X
    :return: None
    """
    m = open(archivo, "rb")
    t = os.path.getsize(archivo)
    while m.tell() < t:
        confederacion = pickle.load(m)
        print(registro_confederacion.to_string_confederacion(confederacion))
    m.close()


def buscar_archivo(archivo, vec_conf):
    """
    Hace la búsqueda del archivo de una confederación. Si existe, directamente
    lo muestra. Si no, carga el archivo y luego lo muestra.
    :param archivo: el archivo confederación
    :param vec_conf: vector de confederaciiones
    :return: None
    """
    escribir = True
    if not os.path.exists(archivo):
        nuevo = input("¿Desea escribir un nuevo archivo?(S/N): ")
        if nuevo == "S" or nuevo == "s":
            grabar_archivo_confederacion(vec_conf, archivo)
            mostrar_archivo(archivo)
            escribir = False
    if escribir == True:
        mostrar_archivo(archivo)


# Opcion 6: la matriz y ingresa por teclado

def vec_resto(vec_paises, y):
    """
    Vector auxiliar que toma al resto de los 24 países
    :param vec_paises: vector original de países
    :param y: país anfitrión cargado por teclado
    :return: vector con el resto de los 24 países
    """
    resto = []
    for i in range(len(vec_paises)):
        if i > 8 and i <= 33 and vec_paises[i].nombre != y:
            resto.append(vec_paises[i])
    return resto


def primeros(vec_paises, y):
    """
    Vector auxiliar que toma al resto de las cabezas de serie
    :param vec_paises: vector original de países
    :param y: país anfitrión cargado por teclado
    :return: vector con el resto de las cabezas de serie
    """
    cab = []
    c = 0
    for i in range(len(vec_paises)):
        c += 1
        if c > 0 and c <= 9 and vec_paises[i].nombre != y:
            cab.append(vec_paises[i])
    return cab


def matriz(vec_paises, y):
    """
    Se genera la matriz para el próximo mundial
    :param vec_paises: El vector original antes cargado
    :param y: El país anfitrión que se carga por teclado
    :return: La matriz
    """
    # Cantidad de columnas y filas
    columnas = 8
    filas = 4

    # Vectores auxiliares que contienen a los 28 restantes (resto)
     # y a las cabezas de serie (head)
    resto = vec_resto(vec_paises, y)
    head = primeros(vec_paises, y)

    mat = [[None] * columnas for i in range(filas)]

    # Primera pasada sobre el vector original para saber encontrar el país
    # anfitrión y grabarlo en el primer casillero de la matriz
    for i in range(len(vec_paises)):
        if vec_paises[i].nombre == y:
            mat[0][0] = vec_paises[i]
    # Recorrida de la columna desde el lugar 1 para cargar el resto de las
    # cabezas de serie
    for c in range(1, columnas):
        mat[0][c] = head[c]
    # Recorrida por el resto de las filas y columnas para cargar el resto de
    # los países
    for f in range(1,4):
        for c in range(columnas):
            mat[f][c] = random.choice(resto)
            resto.remove(mat[f][c]) # Aquí se remueve desde el vector
            # auxiliar resto para que no se repitan en cada vuelta
    return mat


#-----------------------------------------------------------------------------#

def mostrar_matriz(mat):
    """
    Muestra la matriz en forma de cadena
    :param mat: La matriz antes generada
    :return: None
    """
    for j in range(len(mat[0])):
        print("Grupo:",convertir_num_letra_grupo(j))
        for i in range(len(mat)):
            print(registro_paises.to_string_paises(mat[i][j]))


# Opcion 7

def buscar_pais_matriz(mat, pais):
    """
    Busca si un país está dentro de la matriz
    :param mat: La matriz antes generada
    :param pais: El país que ingresa por teclado
    :return: El grupo donde se encuentra ese país si está
    """
    grupo = None
    res = False
    for j in range(len(mat[0])):
        for i in range(len(mat)):
            if mat[i][j].nombre == pais:
                res = True
                grupo = j
                break
        if res:
            break
    return grupo
