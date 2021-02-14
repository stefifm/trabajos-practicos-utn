print("Programa para facilitar el diagnóstico de COVID-19")

#Primer bloque de datos
edad = int(input("Ingrese edad: "))
temperatura_cuerpo = float(input("Ingrese Temperatura corporal: "))
neumonia = input("¿Evidencia de neumonía? SI/NO Mayúscula: ")

#Primer grupo de evaluación y segundo bloque de datos
if neumonia == "SI":
    print("Es un caso sospechoso por neumonía")
elif temperatura_cuerpo > 37:
    tos = input("¿Tiene tos? SI/NO Mayúscula: ")
    odinofagia = input("¿Tiene odinofagia? SI/NO Mayúscula: ")
    dificultad_respiratoria = input("¿Tiene dificultad respiratoria? SI/NO "
                                    "Mayúscula: ")

    #Segundo grupo de evaluación y tercer bloque de datos
    if temperatura_cuerpo or tos == "SI" or odinofagia == "SI" or \
            dificultad_respiratoria == "SI":
        personal_salud = input("¿Es personal de salud? SI/NO Mayúscula: ")
        confirmados = input("¿Estuvo en contacto con casos confirmados? "
                            "SI/NO Mayúscula: ")
        viaje_exterior = input("¿Viajó al exterior? SI/NO Mayúscula: ")
        transmision_local = input("¿Estuvo en zona de transmisión local? "
                                  "SI/NO Mayúscula: ")

        #Tercer grupo de evaluación
        if personal_salud == "SI":
            print("Caso sospechoso por ser personal de salud")
        elif confirmados == "SI":
            print("Caso sospechoso por estar en contacto con infectados")
        elif viaje_exterior == "SI":
            print("Caso sospechoso por viajar al exterior")
        elif transmision_local == "SI":
            print("Caso autóctono por estar en zonas de transmisión local")
        elif edad > 60:
            print("No es caso sospechoso, pero pertenece al grupo de riesgo")
        else:
            if tos == "NO" and odinofagia == "NO":
                print("Siga atento a los síntomas")
            elif tos == "NO" and dificultad_respiratoria == "NO":
                print("Siga atento a los síntomas")
            elif odinofagia == "NO" and dificultad_respiratoria == "NO":
                print("Siga atento a los síntomas")
            else:
                print("Caso autóctono al tener dos o más síntomas "
                      "respiratorios")
else:
    print("No tiene coronavirus")
