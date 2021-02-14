"""
Aquí está el programa principal del trabajo práctico
"""

__author__: "Bruera, Stefania - Lorello, Luciano - Magnano, Nahuel"



import funciones_paises


def principal():
    print("\n\t\t\x1b[1;34m"+"!Bienvenidos a nuestro Sistema de gestion de una competencia mundial!\n"+"\x1b[0;m")

    vec_paises = []
    fd = "paises.csv"
    carga_matriz = False

    opcion = -1

    while opcion != 8:
        print("\t\t\t\033[1;33m"+"Menu de OPCIONES"+"\033[0;m\n"
            "\t--------------------------------\n"
            "\033[1;30m"+"\n1 - Muestra del listado completo de países.\n"
            "2 - País con mayor cantidad de campeonatos.\n"
            "3 - Cantidad de países que ganaron por confederación.\n"
            "4 - Registro y archivo de confederación.\n"
            "5 - Búsqueda de una confederación.\n"
            "6 - Fixture matriz del proximo mundial.\n"
            "7 - Busqueda del pais en el nuevo Fixture.\n"
            "8 - Salir.\n\n"+"\033[0;m"
            "\t--------------------------------\n")

        opcion = funciones_paises.validar_rango(1, 8,"\033[1;30m"+"Elija la opcion deseada: "+"\033[0;m")

        # Opcion 1
        if opcion == 1:
            print("\033[1;30m"+"\nA continuacion usted podra ver todos los paises registrados:"+"\033[0;m")
            print("\n\t\t\t\t\t\t\033[1;33m"+"Listado completo de paises"+"\033[0;m")
            print("-" *80, "\n")
            funciones_paises.cargar_vector(fd, vec_paises)
            funciones_paises.mostrar_vector_paises(vec_paises)
            print()
            funciones_paises.enter()

        # Opcion 2
        elif opcion == 2:
            if not vec_paises:
                print("\n\t\t\033[1;31m"+"Usted no cargo los paises.")
                print("Por favor primero ingrese la opcion N°1." + "\033[0;m\n")
            else:
                print()
                print("-" * 80, "\n")
                print("\033[1;30m"+"Pais con mayor cantidad de campeonatos:\n"+"\033[0;m")

                mayor = funciones_paises.mayor(vec_paises)
                funciones_paises.mostrar_vector_paises(mayor)
                print()
            funciones_paises.enter()
        # Opcion 3
        elif opcion == 3:
            if not vec_paises:
                print("\n\t\t\033[1;31m"+"Usted no cargo los paises.")
                print("Por favor primero ingrese la opcion N°1." + "\033[0;m\n")
            else:
                print()
                print("-" * 80, "")
                print("\033[1;30m"+"\nCantidad de paises que fueron campeones por confederacion:\n"+"\033[0;m")
                funciones_paises.contador_paises_campeonatos(vec_paises)
            print()
            funciones_paises.enter()

        # Opcion 4
        elif opcion == 4:
            if not vec_paises:
                print("\n\t\t\033[1;31m"+"Usted no cargo los paises.")
                print("Por favor primero ingrese la opcion N°1." + "\033[0;m\n")
            else:
                print()
                print("-" * 80, "\n")
                print("\033[1;30m"+"Para facilitar el ingreso de las confederaciones, "
                      "tenga en cuenta lo siguiente :"+"\033[0;m")
                print()
                print("0 = UEFA\n"
                      "1 = CONMEBOL\n"
                      "2 = CONCACAF\n"
                      "3 = CAF\n"
                      "4 = AFC\n"
                      "5 = OFC\n")
                print("\033[1;30m"+"Una confederacion, un archivo\n"+"\033[0;m")
                x = funciones_paises.validar_rango(0, 5,"\033[1;30m"+"Ingrese una "
                                                         "confederación (en numeros): "+"\033[0;m")
                print()
                vec_conf = funciones_paises.vector_confederacion(vec_paises, x)
                funciones_paises.orden_sort(vec_conf)
                archivo = "clasificacion" + str(x) + ".dat"
                funciones_paises.grabar_archivo_confederacion(vec_conf, archivo)
            print()
            funciones_paises.enter()

        #Opcion 5
        elif opcion == 5:
            if not vec_paises:
                print("\n\t\t\033[1;31m"+"Usted no cargo los paises.")
                print("Por favor primero ingrese la opcion N°1." + "\033[0;m\n")
            else:
                print()
                print("-" * 80, "\n")
                print("\033[1;30m"+"Para facilitar la busqueda de las confederaciones, "
                      "tenga en cuenta lo siguiente :"+"\033[0;m")
                print()
                print("0 = UEFA\n"
                      "1 = CONMEBOL\n"
                      "2 = CONCACAF\n"
                      "3 = CAF\n"
                      "4 = AFC\n"
                      "5 = OFC\n")
                conf = funciones_paises.validar_rango(0, 5, "\033[1;30m"+"Ingrese una "
                                                            "confederación (en numeros): "+"\033[0;m")
                print()
                vec_conf = funciones_paises.vector_confederacion(vec_paises, conf)
                funciones_paises.orden_sort(vec_conf)
                archivo = "clasificacion" + str(conf) + ".dat"
                funciones_paises.buscar_archivo(archivo, vec_conf)
            print()
            funciones_paises.enter()

        # Opcion 6
        elif opcion == 6:
            if not vec_paises:
                print("\n\t\t\033[1;31m"+"Usted no cargo los paises.")
                print("Por favor primero ingrese la opcion N°1." + "\033[0;m\n")

            else:
                print()
                print("-" * 80, "\n")
                print()
                y = funciones_paises.validar_anfitrion(vec_paises)
                mat = funciones_paises.matriz(vec_paises, y)
                print()
                funciones_paises.mostrar_matriz(mat)
                carga_matriz = True
            print()
            funciones_paises.enter()

        # Opcion 7
        elif opcion == 7:
            if not vec_paises:
                print("\n\t\t\033[1;31m"+"Usted no cargo los paises.")
                print("Por favor primero ingrese la opcion N°1." + "\033[0;m\n")

            else:
                print()
                print("-" * 80, "\n")
                if not carga_matriz:
                    print("\033[1;30m"+"Antes de buscar un pais en el Fixture,"
                          " usted debe crearlo.\n"+"\033[0;m" + "\033[1;31m" +
                          "Por favor, Seleccione la opcion N°6 para crear el mismo."+ "\033[0;m")
                else:
                    print("\033[1;31m"+"Recuerde que debe ingresar el pais con la primera letra en MAYUSCULA.\n"
                          + "\033[0;m")
                    pais = input("\033[1;30m"+"Ingrese el pais a buscar: "+"\033[0;m")
                    grupo = funciones_paises.buscar_pais_matriz(mat, pais)
                    if grupo is not None:
                        print("\033[1;30m"+"\nEl pais ingresado está en el mundial y se encuentra"
                              " en el grupo:",
                              funciones_paises.convertir_num_letra_grupo(grupo)+"\033[0;m")
                    else:
                        print()
                        print("\033[1;30m"+"El pais ingresado no clasifico al mundial"+"\033[0;m")
            print()
            funciones_paises.enter()
        print()
    print("==============="+"\033[1;33m"+"PROGAMA FINALIZADO"+"\033[0;m"+ "=================")


if __name__ == "__main__":
    principal()
