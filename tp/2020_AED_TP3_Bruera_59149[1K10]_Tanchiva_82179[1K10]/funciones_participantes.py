import random

print("Para la carga de los participantes")

#Aquí se encuentran las clases Participantes y Fixture

class Participantes:
    def __init__(self, nom, conti, rank):
        self.nombre = nom
        self.continente = conti
        self.ranking = rank


def to_string(participantes):
    """
        Genera una cadena que representa el contenido del registro
        Participantes
        :param participantes: convertir en string
        :return: un string representando a participantes
        """
    r = " "
    r += "{:<6}".format("Nombre: " + participantes.nombre)
    r += "{:<10}".format(" | Continente: " + str(participantes.continente))
    r += "{:<10}".format(" | Ranking: " + str(participantes.ranking))
    return r


class Fixture:
    def __init__(self, participantes, punt):
        self.nombre = participantes.nombre
        self.puntos = punt

def to_string_fixture(fixture):
    """
        Genera una cadena que representa el contenido del registro Fixture
        :param fixture: a convertir en string
        :return: un string representando a fixture
        """
    r = " "
    r += "{:<6}".format("Nombre: " + fixture.nombre)
    r += "{:<10}".format(" | Puntos: " + str(fixture.puntos))
    return r

def mostrar_participantes(participantes):
    """
    Muestra los elementos de un vector de registros de
    tipo Participantes
    :param participantes: El vector de registros de tipo Participantes
    :return: None
    """
    for i in range(len(participantes)):
        print(to_string(participantes[i]))

#------------------------------------------------------------------------------


# Primera parte del ejercicio: Carga manual y automática del vector de
# participantes

# Validación para que no se repitan los nombres
def buscar_nombre(nom, participantes):
    """
    Busca en el vector participantes si un nombre se repite
    :param nom: El nombre que se ingresará
    :param participantes: vector de registro Tipo Participantes
    :return: True si ya existe el nombre. Y False si no está
    """
    for reg in participantes:
        if reg.nombre == nom:
            return True
    return False

# Validar el rango para continente y ranking
def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Valor no válido. Ingrese un valor entre",str(inf),"y",
                  str(sup))
    return n

#Carga manual del vector
def carga_manual(participantes):
    """
        Genera el vector de registros tipo Participantes de forma manual
        :return: vector de participantes con datos cargados manualmente
        """
    for i in range(16):
        nombre = input("Ingrese el nombre de los participantes: ")
        while buscar_nombre(nombre, participantes):
            nombre = input("Ingrese el nombre de los participantes: ")

        continente = validar_rango(0, 4, "Ingrese el continente [0-América. "
                                         "1-Europa. 2-Asia. 3-África. "
                                         "4-Oceanía")
        ranking = validar_rango(1, 100, "Ingrese el ranking: ")
        reg1 = Participantes(nombre, continente, ranking)
        participantes.append(reg1)


# Esta sección es para la carga automática

# Una tupla para que nombre lo use en el random.choice
nom = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express")

def carga_automatica(participantes):
    """
    Genera el vector de registros tipo Participantes de forma automática
    :return: vector de participantes con datos aleatorios
    """
    for i in range(16):
        nombre = random.choice(nom)
        while buscar_nombre(nombre, participantes):
            nombre = random.choice(nom)

        continente = random.randint(0, 4)
        ranking = random.randint(1, 100)
        reg1 = Participantes(nombre, continente, ranking)
        participantes.append(reg1)


# Ordenamiento de mayor a menor
def orden_sort(participantes):
    """
    Algoritmo de Selección Directa para ordenar de mayor a menor el arreglo
    :param participantes: El vector de registros de tipo Participantes
    :return: El vector ordenado
    """
    n = len(participantes)
    for i in range(n-1):
        for j in range(i+1, n):
            if participantes[i].ranking < participantes[j].ranking:
                participantes[i], participantes[j] = participantes[j], \
                                                     participantes[i]

#Estadística participante por continente
def estadistica_continente(participantes):
    """
    Arma y muestra el vector de conteo de continente
    :param participantes: El vector de registros de tipo Participantes
    :return: El vector de conteo de participantes por continente
    """
    conteo_continente = [0] * 16
    for i in range(len(participantes)):
        cont = int(participantes[i].continente)
        conteo_continente[cont] += 1
    for i in range(16):
        if conteo_continente[i] != 0:
            print("Continente:",i,"| Cantidad de participantes:",
                  conteo_continente[i])

#------------------------------------------------------------------------------


# Función  para armar y mostrar el fixture de octavos
def fixture(fixture):
    """
    Genera y muestra los elementos de un vector de registros de
    tipo Fixture solo para octavos
    :param fixture: El vector de registros de tipo Fixture
    :return: El vector de registros Tipo Fixture ya mostrando los
    enfrentamientos y por elección nuestra, los puntos. Solo sirve para octavos
    """
    n = len(fixture) // 2
    posicion = len(fixture) - 1
    c = 0
    for i in range(n):
        fixture[i].puntos = random.randint(100, 1000)
        fixture[posicion - c].puntos = random.randint(100, 1000)
        e1 = Fixture(fixture[i],fixture[i].puntos)
        e2 = Fixture(fixture[posicion-c], fixture[posicion - c].puntos)
        c += 1
        print(to_string_fixture(e1), "vs", to_string_fixture(e2))

def mostrar_fixture(fixture):
    """
        Muestra los cruces de cuartos, semis, tercero y final
        :param fixture: El vector de registros de tipo Fixture
        :return: Muestra de los cruces + puntos de cuartos, semis, tercero y
        final
        """
    n = len(fixture) // 2
    posicion = len(fixture) - 1
    c = 0
    for i in range(n):
        e1 = fixture[i]
        e2 = fixture[posicion-c]
        c += 1
        print(to_string_fixture(e1), "vs", to_string_fixture(e2))



#Función para determinar los ganadores de cada cruce
def ganador(fixture):
    """
    Determina el ganador de cada ronda
    :param fixture: El vector de registros de tipo Fixture
    :return: El vector ronda con los que pasaron a la siguiente instancia
    """
    n = len(fixture) // 2
    posicion = len(fixture) - 1
    c = 0
    ronda = []
    for i in range(n):
        if fixture[i].puntos > fixture[posicion-c].puntos:
            ronda.append(fixture[i])
        else:
            ronda.append(fixture[posicion-c])
        c += 1
    return ronda


#Función para armar el vector de la final
def final(fixture):
    """
    Genera el vector de la final
    :param fixture: El vector de registros de tipo Fixture
    :return: el vector con los finalistas
    """
    n = len(fixture) // 2
    posicion = len(fixture) - 1
    c = 0
    ronda_final = []
    for i in range(n):
        if fixture[i].puntos > fixture[posicion - c].puntos:
            ronda_final.append(fixture[i])
        else:
            ronda_final.append(fixture[posicion - c])
        c += 1
    return ronda_final

#Función para armar el vector del tercer puesto
def tercer(fixture):
    """
    Genra el vector con los que compiten por el tercer puesto
    :param fixture: El vector de registros de tipo Fixture
    :return: vector con los que van por el tercer puesto
    """
    n = len(fixture) // 2
    posicion = len(fixture) - 1
    c = 0
    ronda_tercero = []
    for i in range(n):
        if fixture[i].puntos < fixture[posicion - c].puntos:
            ronda_tercero.append(fixture[i])
        else:
            ronda_tercero.append(fixture[posicion - c])
        c += 1
    return ronda_tercero

# Función para calcular el promedio
def estadistica_promedio_ronda(fixture):
    """
        Función para el cálculo de promedio de puntos por partcipantes en
        octavos, cuartos y semis
        :param fixture: el vector de registros de tipo Fixture
        :return: promedio de los puntos por participantes
        """
    suma = 0
    contador = 0
    for reg in fixture:
        suma += reg.puntos
        contador += 1
    prom = round(suma / contador, 2)
    return prom


#------------------------------------------------------------------------------

# Función para determinar el campeón y subcampeón
def top2(final):
    """
    Determina quién fue campeón y subcampeón
    :param final: El vector de finalistas antes creado
    :return: ganador y segundo
    """
    posicion = len(final) - 1
    c = 0
    for i in range(len(final)):
        if final[i].puntos > final[posicion - c].puntos:
            ganador = final[i]
            segundo = final[posicion-c]
        else:
            ganador = final[posicion-c]
            segundo = final[i]
        c += 1
        return ganador, segundo

# Función para el tercer lugar
def tercero(ter):
    """
    Determina quién termina en el tercer lugar
    :param ter: El vector de tercer_puesto antes creado
    :return: tercer lugar
    """
    posicion = len(ter) - 1
    c = 0
    for i in range(len(ter)):
        if ter[i].puntos > ter[posicion - c].puntos:
            tercer_lugar = ter[i]
        else:
            tercer_lugar = ter[posicion-c]
        c += 1
        return tercer_lugar

#------------------------------------------------------------------------------

# Está función se ubica al último de porque suma los puntos al ranking
# de los tres primeros de la competencia y luego va a parar al nuevo arreglo

def nuevo_arreglo(pri, seg, ter, participantes):
    """
    Suma los puntos del ranking (25 al 1º, 15 al 2º y 5 al 3º)
    :param pri, seg, ter, participantes: primero, segundo, tercero y el
    vector de registros del tipo Participantes
    :return: El nuevo vector de registro de tipo Participantes con las
    modificaciones en el ranking
    """
    pri.ranking += 25
    seg.ranking += 15
    ter.ranking += 5
    return participantes