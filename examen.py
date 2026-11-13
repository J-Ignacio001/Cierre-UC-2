estudiantes = []
def menu_opciones ():
    print("1.- Registrar un estudiante")
    print("2.- Mostrar todos los estudiantes registrados")
    print("3.- Consultar el promedio de un estudiante")
    print("4.- Mostrar estadisticas generales del grupo")
    print("5.- Salir del programa")


def registrar_estudiante():
    validar = 1 #Funcionar ciclo while
    estudiantes = [
                {"ID": ide, "nombre": nombre, "calificaciones": calificaciones, "promedio":promedio, "situacion":situacion}
            ]
    while validar != 0:
        ide = input("Ingrese el ID del estudiante.\n Ejemplo: 00000288570: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        calificacion1 = int(input("Ingrese su calificacion 1: "))
        calificacion2 = int(input("Ingrese su calificacion 2: "))
        calificacion3 = int(input("Ingrese su calificacion 3: "))
        
        calificaciones = (calificacion1,calificacion2,calificacion3)

        datos_validos = True #Validar datos 
        #Validar calificaciones del 1 al 100
        for i in calificaciones:
            if i < 0 or i > 100:
                print("Error, numeros no validos. Intente de nuevo.")
                datos_validos = False

        #Identificar si ID y nombre no queden vacios
            if ide == "" or nombre == "":
                print("Error, dejo algun espacio en blanco. Intente de nuevo")
                datos_validos = False
            else:
                nombrelimpio = nombre.strip()
                ide_limpio = ide.strip()
                validar = 0
                with open("registro.txt", "a") as archivo:
                    archivo.write(f"{ide_limpio},{nombrelimpio},{calificaciones} \n") 
                    print("Calificacion guardada con exito. \n")
        #No registrar dos estudiantes con la misma identififacion
        for e in estudiantes:
            if e["ID"] == ide:
                print("Error, ID ya registrado. Intente de nuevo.")
                datos_validos = False
        #Si todo funciona validar y guardar todos los datos correctamente
        if datos_validos:
            promedio = calcular_promedio(calificaciones)
            if promedio >= 70:
                situacion = "Aprobado"
            else:
                situacion = "Reprobado"
            estudiantes = [{"ID": ide,
                            "nombre": nombre,
                            "calificaciones": calificaciones,
                            "promedio":promedio,
                            "situacion":situacion}]

            with open("registro.txt", "a") as archivo:
                archivo.write(f"{ide},{nombre},{calificacion1},{calificacion2},{calificacion3},{promedio},{situacion}")
            print("Estudiante guardada con exito. \n")
            validar = 0
       
def calcular_promedio(calificaciones):
    with open("registro.txt", "r") as archivo:
        for linea in calificaciones:

            suma = 0
            for k in calificaciones:
                suma += k
            promedio = suma/ len(calificaciones)
            return promedio

def mostrar_estudiantes ():
    print("prueba")

def consultar_estudiante ():
    print("prueba")

def mostrar_estadisticas ():
    print("prueba")
    

opciones = 1
while opciones != 0:
    menu_opciones() 
    opcion = int(input("\nEliga una opcion: "))
    if opcion == 1:
        registrar_estudiante()
    elif opcion == 2:
        print("nose")
    elif opcion == 3:
        print("nose")
    elif opcion == 4:
        print("nose")
    elif opcion == 5:
        opciones = 1
        print("Salio exitosamente. Hasta pronto :)")
    else:
        print("Error, numero no valido. Intente de nuevo.")
