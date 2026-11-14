#Acumular en una lista el registro de cada estudiante exitosamente
estudiantes = []

def menu_opciones(): #Menu del programa
    print("=============================================")
    print("\t.-:MENÚ:-.")
    print("=============================================\n")
    print("1.- Registrar un estudiante")
    print("2.- Mostrar todos los estudiantes registrados")
    print("3.- Consultar el promedio de un estudiante")
    print("4.- Mostrar estadisticas generales del grupo")
    print("5.- Salir del programa")

def registrar_estudiante():
    validar = 1  # Funcionar ciclo while

    while validar != 0:
        #Entrada de datos al registrar
        ide = input("Ingrese el ID del estudiante.\nEjemplo: ABC123: ").strip()
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        calificacion1 = int(input("Ingrese su calificacion 1: "))
        calificacion2 = int(input("Ingrese su calificacion 2: "))
        calificacion3 = int(input("Ingrese su calificacion 3: "))

        #Guardar calificaciones en tupla
        calificaciones = (calificacion1, calificacion2, calificacion3)

        datos_validos = True  # Validar datos

        # Validar calificaciones del 0 al 100
        for i in calificaciones:
            if i < 0 or i > 100:
                print("\nError, numeros no validos. Intente de nuevo.\n")
                datos_validos = False

        # Identificar si ID y nombre no queden vacios
        if ide == "" or nombre == "":
            print("\nError, dejo algun espacio en blanco. Intente de nuevo\n")
            datos_validos = False

        # No registrar dos estudiantes con la misma identificacion
        for e in estudiantes:
            if e["ID"] == ide:
                print("Error, ID ya registrado. Intente de nuevo.")
                datos_validos = False

        # Si todo funciona, calcular y guardar los datos
        if datos_validos:
            promedio = calcular_promedio(calificaciones)
            if promedio >= 70:
                situacion = "Aprobado"
            else:
                situacion = "Reprobado"

            estudiante = { #Guardar datos en un diccionario
                "ID": ide,
                "nombre": nombre,
                "calificaciones": calificaciones,
                "promedio": promedio,
                "situacion": situacion,
            }
            estudiantes.append(estudiante)

            print("\nEstudiante guardado con exito. \n")
            validar = 0

def calcular_promedio(calificaciones):
    suma = 0
    for k in calificaciones:
        suma += k
    promedio = suma / len(calificaciones)
    return promedio


def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados anteriormente.\n")
    else:
        print("\n---Lista de estudiantes---")
        for i in range(len(estudiantes)):
            print(f"{i+1}. {estudiantes[i]}\n")


def consultar_estudiante():
    search = input("ingrese la ID del estudiante: ")
    encontrado = False
    for i in (estudiantes):
        if i["ID"] == search:
            print("\n---¡¡Estudiante encontrado!!---")
            print(f"- Nombre: {i["nombre"]}")
            print(f"- Promedio: {i["promedio"]:.2f}")
            print(f"- Situación: {i["situacion"]}")

            encontrado = True
    if encontrado == False:
        print("\nID no encontrado, porfavor intente de nuevo.\n")



def mostrar_estadisticas():
    promedios = []
    total_estudiante = reprobados = aprobados = 0
    calificaciones_acum = promedio_alto = promedio_general = 0
    encontrado = False
    print("\n=================================================")
    print("\t.-:ESTADISTICAS:-.")
    print("=================================================\n")

    for u in estudiantes:
        encontrado= True
        total_estudiante += 1
        promedio = calcular_promedio(u["calificaciones"])
        promedios.append(promedio)
        if promedio >= 70:
            aprobados += 1
        else:
            reprobados += 1
            
        #Acumular calificaciones
        calificaciones_acum += sum(u["calificaciones"])
    if encontrado == False:
        print("Error, no hay estudiantes registrados.\n")
    else:
        #Promedio mas alto del grupo:
        promedio_alto = max(promedios)

        promedio_general = calificaciones_acum / (total_estudiante*len(u["calificaciones"]))

        print(f"- Cantidad total de estudiantes: {total_estudiante}")
        print(f"- Promedio general del grupo: {promedio_general:.2f}")
        print(f"- Estudiantes aprobados: {aprobados}")
        print(f"- Estudiantes reprobados: {reprobados}")
        print(f"- Promedio mas alto del grupo: {promedio_alto:.2f}")

opciones = 1
while opciones != 0:
    menu_opciones()
    opcion = int(input("\nEliga una opcion (1-5): "))
    if opcion == 1:
        registrar_estudiante()
    elif opcion == 2:
        mostrar_estudiantes()
    elif opcion == 3:
        consultar_estudiante()
    elif opcion == 4:
        mostrar_estadisticas()
    elif opcion == 5:
        print("Salio exitosamente. Hasta pronto :)")
        opciones = 0
    else:
        print("Error, numero no valido. Intente de nuevo.")
