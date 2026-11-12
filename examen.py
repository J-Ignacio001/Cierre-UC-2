def menu_opciones ():
    print("1.- Registrar un estudiante")
    print("2.- Mostrar todos los estudiantes registrados")
    print("3.- Consultar el promedio de un estudiante")
    print("4.- Mostrar estadisticas generales del grupo")
    print("5.- Salir del programa")

def registrar_estudiante():
    validar = 1
    #Validar calificaciones del 1 al 100
    while validar != 0:
        ide = input("Ingrese el ID del estudiante.\n Ejemplo: 0000288570: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        calificacion1 = int(input("Ingrese su calificacion 1: "))
        calificacion2 = int(input("Ingrese su calificacion 2: "))
        calificacion3 = int(input("Ingrese su calificacion 3: "))
        
        calificaciones = (calificacion1,calificacion2,calificacion3)

        for i in calificaciones:
            if i < 0 and i > 100:
                print("Error, numeros no validos. Intente de nuevo.")
            
        if ide == "" and nombre == "":
            print("Error, dejo algun espacio en blanco. Intente de nuevo")
            
        else:
            nombrelimpio = nombre.strip()
            ide_limpio = ide.strip()
            validar = 0
            with open("registro.txt", "a") as archivo:
                archivo.write(f"{ide_limpio},{nombrelimpio},{calificaciones} \n") 
                print("Calificacion guardada con exito. \n")
        
    
    #Identificar si ID y nombre no queden vacios
    #No registrar dos estudiantes con la misma identififacion
                
  

def calcular_promedio ():
    with open("registro.txt", "r") as archivo:
        for calificaciones in archivo:
            promedio = calificaciones / len(calificaciones)
            print(promedio)
            



#Menu en si
'''
while True:
    menu_opciones()
    opcion = int(input("Eliga una opcion: "))
    if opcion == 1:
        registrar_estudiante()
    elif opcion == 2:
        print("nose")
    elif opcion == 3:
        print("nose")
    elif opcion == 4:
        print("nose")
    elif opcion == 5:
        False
'''