"""
Clase Países para usarse en la transformación archivo a vector
(puntos 1, 2, 3, 6 y 7)
"""


class Paises:
    def __init__(self, conf, nom, punt, camp):
        self.confederacion = conf
        self.nombre = nom
        self.puntos = punt
        self.campeonatos = camp


def cadena_confederacion(confederacion):
    """
    Convierte el número de codificación a las siglas de la confederación
    :param confederacion: código a convertir
    :return: Las siglas de la confederación asociado al código
    """
    res = " "
    if confederacion == 0:
        res = "UEFA"
    if confederacion == 1:
        res = "CONMEBOL"
    if confederacion == 2:
        res = "CONCACAF"
    if confederacion == 3:
        res = "CAF"
    if confederacion == 4:
        res = "AFC"
    if confederacion == 5:
        res = "OFC"
    return res


def to_string_paises(paises):
    """
    Transforma la clase Países en un string
    :param paises: el país a convertir
    :return: La cadena que describe al país
    """
    r = " "
    r += "Confederacion: " + str(paises.confederacion) + "." + \
         cadena_confederacion(paises.confederacion)
    r += " - Nombre: " + paises.nombre
    r += " - Puntos: " + str(paises.puntos)
    r += " - Campeonatos: " + str(paises.campeonatos)
    return r


def csv_to_linea(linea):
    """
    Convierte una línea de texto a vector y la graba en el registro Países
    :param linea: la línea a convertir
    :return: una variable del registro Países con las lineas ya convertidas
    """
    campos = linea.split(",")
    paises = Paises(int(campos[0]), campos[1], int(campos[2]), int(campos[3]))
    return paises
