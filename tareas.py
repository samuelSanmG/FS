FILE_NAME = "tareas.txt"
tareas = []  

def cargarTareas():
    # Carga las tareas desde el archivo
    global tareas
    tareas = []  
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                tarea = line.strip().split(",")
                tareas.append([tarea[0], tarea[1] == "True"])  
    except FileNotFoundError:
        with open(FILE_NAME, "w"):  
            pass

def guardarTareas():
    # Guarda las tareas en el archivo
    with open(FILE_NAME, "w") as file:
        for tarea in tareas:
            file.write(f"{tarea[0]},{tarea[1]}\n")

def agregarTarea():
    # Agrega una nueva tarea
    tarea = input("Ingrese la tarea: ").strip()
    if tarea:
        tareas.append([tarea, False]) 
        with open(FILE_NAME, "a") as file:
            file.write(f"{tarea},False\n")
        print("Tarea agregada con éxito")
    else:
        print("La tarea no puede estar vacía")

def verTareas():
    # Muestra todas las tareas
    if not tareas:
        print("No hay tareas registradas")
        return
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        estado = "Completado" if tarea[1] else "Pendiente"
        print(f"{i}. {tarea[0]} - {estado}")

def marcarCompleta():
    # Marca una tarea como completada
    verTareas()
    try:
        index = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
        if 0 <= index < len(tareas):
            tareas[index][1] = True
            guardarTareas()
            print("Tarea marcada como completada")
        else:
            print("Número de tarea inválido")
    except ValueError:
        print("Entrada no válida")

def eliminarTarea():
    # Elimina una tarea
    verTareas()
    try:
        index = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= index < len(tareas):
            del tareas[index]
            guardarTareas()
            print("Tarea eliminada")
        else:
            print("Número de tarea inválido")
    except ValueError:
        print("Entrada no válida")

def mostrarMenu():
    # Muestra el menú de opciones
    print("\nMenú de tareas")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

cargarTareas()

continuar = True
while continuar:
    mostrarMenu()
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            agregarTarea()
        elif opcion == 2:
            verTareas()
        elif opcion == 3:
            marcarCompleta()
        elif opcion == 4:
            eliminarTarea()
        elif opcion == 5:
            continuar = False
            print("Saliendo del programa...")
        else:
            print("Opción inválida, intente de nuevo")
    except ValueError:
        print("Por favor, ingrese un número válido")