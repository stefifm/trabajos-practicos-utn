"""
Clase Confederación que se usará en los puntos 4 y 5
"""

class Confederacion:
    def __init__(self, nom, punt, camp):
        self.nombre = nom
        self.puntos = punt
        self.campeonatos = camp


def to_string_confederacion(confederacion):
    """
    Transforma la clase Confederación en string
    :param confederacion: el registro Confederación
    :return: las líneas en string
    """
    r = " "
    r += "Nombre: " + confederacion.nombre
    r += " - Puntos: " + str(confederacion.puntos)
    r += " - Campeonatos: " + str(confederacion.campeonatos)
    return r