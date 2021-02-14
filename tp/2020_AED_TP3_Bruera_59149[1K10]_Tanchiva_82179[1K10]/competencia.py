
import funciones_participantes

__author__ = "Bruera, Stefania y Tanchiva, Melanie "

print("Programa principal del TP3")



def principal():
    competidores = [] # vector vacío

    print("=" * 80)

    print("\nLista de participantes que estarán en competencia\n")

    # Una lista que muestra los participantes de la competencia
    lista_participantes = ["Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express"]

    for i in range(len(lista_participantes)):
        print(lista_participantes[i]) # Aquí muestra la lista de participantes

    print("=" * 80)

    print("\nHora de cargar los participantes en los arreglos\n")
    opcion = int(input("\n1 para hacer la carga manual. 2 para carga "
                       "automática: "))   # Opción para que el usuiario
                                          # entre carga manual y automática
    if opcion == 1:
        funciones_participantes.carga_manual(competidores)
    else:
        funciones_participantes.carga_automatica(competidores)
        print("Hecho, Ya están cargado los competidores.")

    print("\nPresione <Enter> para continuar")
    input() # Decicimos poner input() para que el programa avance poco a poco

    print("=" * 80)

    # Lista ordenada de los competidores
    print("\nLista ordenada de los competidores\n")
    funciones_participantes.orden_sort(competidores)
    funciones_participantes.mostrar_participantes(competidores)

    # Estadística de participantes por continente
    print("\nEstádistica cantidad de participantes por continente\n")
    funciones_participantes.estadistica_continente(competidores)

    print("Presione <Enter> para empezar con la competencia")
    input()

    print("=" * 80)

    # Octavos de final
    print("\nLargamos con los octavos de final")
    print("Presione <Enter> para ver los enfrentamientos con sus puntos")
    input()

    print("\nRonda de octavos\n")
    funciones_participantes.fixture(competidores)

    print("\nEstadística promedio de puntos en octavos")
    prom_octavos = funciones_participantes.estadistica_promedio_ronda(competidores)
    print("\nPromedio de puntos en octavos:",prom_octavos)

    print("\nVamos con otro <Enter> para continuar con los cuartos de final")
    input()

    print("=" * 80)

    # Cuartos de final
    print("\nBandera verde para los cuartos de final")
    print("Presione <Enter> para ver los enfrentamientos con los puntos")
    input()

    print("\nRonda de Cuartos de Final\n")
    cuartos = funciones_participantes.ganador(competidores)
    funciones_participantes.mostrar_fixture(cuartos)

    print("\nEstadística promedio de puntos en cuartos:")
    prom_cuartos = funciones_participantes.estadistica_promedio_ronda(cuartos)
    print("\nPromedio de puntos en cuartos:",prom_cuartos)

    print("\nVamos con otro <Enter> para entrar a las semifinales")
    input()

    print("=" * 80)

    # Semifinales
    print("\n¡¡¡Aquí están las semis!!!")
    print("Presione <Enter> para ver los enfrentamientos con los puntos")
    input()

    print("\nRonda de semifinales\n")
    semis = funciones_participantes.ganador(cuartos)
    funciones_participantes.mostrar_fixture(semis)

    print("\nEstadística promedio de puntos en semifinales")
    prom_semis = funciones_participantes.estadistica_promedio_ronda(semis)
    print("\nPromedio de puntos en semifinales:",prom_semis)

    print("\nVamos con otro <Enter> para la definición del tercer puesto")
    input()

    print("=" * 80)

    # Decidimos ir primero a la definición del tercer puesto para recrear
    # de alguna manera la copa mundial de fútbol, donde primero está el partido
    # del tercer lugar

    print("\nAquí viene el tercer puesto")
    print("Presione <Enter> para ver los enfrentamientos con los puntos")
    input()

    print("\nRonda de Tercer Puesto\n")
    tercer = funciones_participantes.tercer(semis)
    funciones_participantes.mostrar_fixture(tercer)
    tercer_puesto = funciones_participantes.tercero(tercer)
    print("\nTercer puesto =======>",funciones_participantes.to_string(tercer_puesto))

    print("\n¡¡¡LLegamos a la final!!! <Enter> para la definición")
    input()

    print("=" * 80)

    # Final
    print("¡¡¡La gran final!!!")
    print("Presione <Enter> para ver los enfrentamientos con los puntos")
    input()

    print("\nFinal\n")
    final = funciones_participantes.final(semis)
    funciones_participantes.mostrar_fixture(final)
    primero, segundo = funciones_participantes.top2(final)

    print("\n!!!!Y aquí están los campeones y subcampeones!!!!\n")
    print("CAMPEÓN ==========>",funciones_participantes.to_string(primero))
    print("\nSubcampeón ========>",funciones_participantes.to_string(segundo))


    print("\nSe acabó..... ")
    print("Presione <Enter> para ver el nuevo ranking....")
    input()

    print("=" * 80)

    print("\nNuevo Ranking tras la competencia\n")
    new_list = funciones_participantes.nuevo_arreglo(primero, segundo, tercer_puesto,
                                   competidores)
    funciones_participantes.orden_sort(new_list)
    funciones_participantes.mostrar_participantes(new_list)



if __name__ == "__main__":
    principal()