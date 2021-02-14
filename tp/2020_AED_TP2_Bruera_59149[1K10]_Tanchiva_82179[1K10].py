print('Generación de Estadísticas de COVID-19')
print('=' * 80)
import random

#--------------------------Funciones-----------------------------
# Función de porcentaje
def porcentaje(n1, n2):
    if n2 != 0:
        p = n1 * 100 / n2
    else:
        p = 0
    return p

# Función para el cálculo de promedio de edad
def prom_e(ej, n4):
    if n4 != 0:
        e = ej // n4
    else:
        e = 0
    return e

# Función para la validación de la cuenta
def validacion(a):
    cl = -1
    for caracter in a:
        cl += 1
        #Esto es para que no haya dos arrobas.
        if "@@" in a:
            return False
        elif ".." in a:
            return False
        elif a[0] == '@' or a[cl - 1] == '@':
            return False
        elif a[0] == '.' or a[cl - 1] == '.':
            return False
        cl = 0
        return True
#--------------------------Validación del usuario-----------------------------
c = 1
usuario = input('Ingrese su usuario (formato nombre@dominio): ')
while c < 3:
    if validacion(usuario) == False:
        print('Error. Vuelva a cargar su usuario')
    else:
        print('usuario correcto')
        print('=' * 80)
        break
    c += 1
    usuario = input('Ingrese su usuario (formato nombre@dominio: ')
if c == 3:
    print('Sus intentos terminaron')
    exit(c)
#------------------------------------------------------------------------------
#-------------------Carga de datos --------------------------------------------
n = -1
while n <= 0:
    n = int(input('Ingrese cantidad de casos sospechosos: '))
    if n <= 0:
        print('Error. Se pide que no sea menor o igual a cero.')
print("=" * 80)

# Contadores
confirmados = 0
riesgo = 0
salud = 0
reg_norte = 0
reg_sur = 0
reg_gran_cordoba = 0
reg_capital = 0
con_viajes = 0
con_contacto = 0
autoctonos = 0

# Bandera para el cálculo del menor de la edad casos autóctonos
flag_auto = False

# Acumuladores
edades_riesgo = 0
edades_confirmados = 0

for caso in range(n):
    # Datos generados aleatoriamente
    edad = random.randint(10, 100)
    test_positivo = random.randint(0, 100) < 65
    region = random.randint(1, 10)
    contacto = random.randint(0, 100) < 60
    personal = random.randint(0, 100) < 15
    viaje = random.randint(0, 100) < 10

    # Condicionales
    # Se evalúa primero si el test es positivo. Luego se cuenta los
    # confirmados y acumula edades_confirmados para el cálculo del promedio
    # de edad de los positivos
    if test_positivo == True:
        confirmados += 1
        edades_confirmados += edad
        # Aquí comienza el subloque autóctono. Evalúa si es autóctono y luego
        # la edad menor del mismo.
        if contacto == False and personal == False and viaje == False:
            autoctonos += 1
            if flag_auto == False or edad < menor_auto:
                menor_auto = edad
                flag_auto = True
        # Subloque de las regiones. Se evalúa si es norte, sur, gran córdoba
        # y capital y se cuenta.
        if region < 3:
            reg_norte += 1
        elif region < 5:
            reg_sur += 1
        elif region < 8:
            reg_gran_cordoba += 1
        else:
            reg_capital += 1
        # Último subloque refiere si viajó al exterior y se cuenta al dar
        # verdadero.
        if viaje == True:
            con_viajes += 1
    else:
        # Si el test es falso o mejor dicho negativo, se evalúa si la edad es
        # mayor o igual a 60, se cuenta en riesgo y acumula en edades_riesgo
        # para sacar el promedio de edad del grupo de riesgo
        if edad >= 60:
            riesgo += 1
            edades_riesgo += edad
    # Bloque de personal de salud. Se analiza por fuera del bloque de los test
    # ya que se tiene en cuenta cuántos son de la carga de sospechosos.
    if personal == True:
        salud += 1
    # Bloque de contactos. Se analiza por fuera del bloque de los test
    # ya que se tiene en cuenta cuántos son de la carga de sospechosos.
    if contacto == True:
        con_contacto += 1

# Calculos
# Para el promedio de edad del grupo de riesgo:
prom_riesgo = prom_e(edades_riesgo, riesgo)
# Porcentaje de personal de salud
porc_salud = round(porcentaje(salud, n), 2)
# Porcentaje de positivos y promedio de edad de los confirmados
porc_positivos = round(porcentaje(confirmados, n), 2)
prom_edad = round(prom_e(edades_confirmados, confirmados), 2)
# Porcentaje de las regiones
porc_norte = round(porcentaje(reg_norte, confirmados), 2)
porc_sur = round(porcentaje(reg_sur, confirmados), 2)
porc_gcordoba = round(porcentaje(reg_gran_cordoba, confirmados), 2)
porc_capital = round(porcentaje(reg_capital, confirmados), 2)
# Porcentaje de los casos autóctonos
porc_autoctono = round(porcentaje(autoctonos, confirmados), 2)

#------------------------------------------------------------------------------
#------------------------------Menu de opciones--------------------------------
def menu_opciones():
    op = 1
    while op != 11:
        print('♥♥♥♥♥♥♥ Menu de opciones ♥♥♥♥♥♥♥')
        print(
            '1) Cantidad de casos confirmados y porcentaje sobre el total de '
            'casos sospechosos.')
        print(
            '2) Edad promedio de pacientes que pertenecen al grupo de riesgo.')
        print(
            '3) Cantidad y porcentaje del personal de salud sobre el total de '
            'casos sospechosos.')
        print('4) Edad promedio de los casos confirmados.')
        print('5) Menor edad entre los casos autoctonos.')
        print(
            '6) Cantidad y porcentaje de casos por region respecto el total '
            'de casos confirmados')
        print('7) Cantidad de casos confirmados por viajes al exterior.')
        print('8) Cantidad de casos por contacto con contagiados.')
        print('9) Regiones sin casos confirmados.')
        print('10) Porcentajes de casos autoctonos sobre el total de casos '
              'confirmados.')
        print('11) Salir')
        print('♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
        print()
        op = int(input('Elija una opcion: '))
        if op == 1:
            print('Casos confirmados ===============>')
            print('Cantidad de casos confirmados:',confirmados)
            print('Y representa el',porc_positivos,'% sobre el total de los '
                                                   'casos sospechosos')
        elif op == 2:
            print('Edad promedio del grupo de riesgo ===============>')
            print('La edad promedio del grupo de riesgo:',prom_riesgo,'años')
        elif op == 3:
            print('Personal de salud ===================>')
            print('total de pacientes que son parte del personal de salud:',
                  salud)
            print('Y representa el',porc_salud,'% sobre el total de los '
                                               'casos sospechosos')
        elif op == 4:
            print('Edad promedio de los confirmados ====================>')
            print('La edad promedio de los casos confirmados es:',prom_edad,
                  'años')
        elif op == 5:
            print('Edad menor entre los autóctonos ================>')
            print('La edad menor entre los casos autóctonos:',menor_auto,
                  'años')
        elif op == 6:
            print('Cantidad de casos por region ==============>')
            print('Cantidad de casos en el Norte:',reg_norte)
            print('Y representa el',porc_norte,
                  '% sobre el total de los casos confirmados')
            print('-' * 80)
            print('Cantidad de casos en el Sur:',reg_sur)
            print('Y representa el', porc_sur, '% sobre el total de los '
                                               'casos confirmados')
            print('-' * 80)
            print('Cantidad de casos en Gran Córdoba:',reg_gran_cordoba)
            print('Y representa el',porc_gcordoba,'% sobre el total de los '
                                                  'casos confirmados')
            print('-' * 80)
            print('Cantidad de casos en Capital:',reg_capital)
            print('Y representa el', porc_capital,
                  '% sobre el total de los casos confirmados')
        elif op == 7:
            print('Casos por viaje al exterior ===============>')
            print('Cantidad de casos por viaje al exterior:', con_viajes)
        elif op == 8:
            print(
                'Casos sospechosos con contactos con contagiados ==========>')
            print('Cantidad de casos sospechosos que tuvieron contacto con '
                  'contagiados:', con_contacto)
        elif op == 9:
            print('Regiones que no tuvieron casos ======================>')
            if reg_norte == 0:
                print('La región Norte no tiene casos')
                print('-' * 80)
            if reg_sur == 0:
                print('La region Sur no tiene casos ')
                print('-' * 80)
            if reg_gran_cordoba == 0:
                print('La region Gran Córdoba no tiene casos')
                print('-' * 80)
            if reg_capital == 0:
                print('La region Capital no tiene casos')
                print('-' * 80)
            if reg_norte != 0 and reg_sur != 0 and reg_gran_cordoba != 0 and \
                    reg_capital != 0:
                print('Todas las regiones tienen al menos un caso')
        elif op == 10:
            print('Porcentaje de autóctonos ==============>')
            print('Porcentaje de casos autoctonos sobre el total de casos '
                  'confirmados es del', porc_autoctono, '%')
        else:
            if op == 11:
                print(' ♥♥♥♥♥♥♥ PROGRAMA TERMINADO ♥♥♥♥♥♥♥ ')
            else:
                print('La opcion ingresada es incorrecta')
menu_opciones()
