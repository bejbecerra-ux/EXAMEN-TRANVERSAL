
productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
}
stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}
def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            
            if 1 <= opcion <= 6:
                return opcion 
            else:
                print("Error: La opción debe estar entre 1 y 6. Intente de nuevo.")
                
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ===========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

while True:
    while True:
        mostrar_menu()

        opcion_elegida = leer_opcion()
    
        match opcion_elegida:
            case 1:
                print("n")
            case 2:
                print("")
            case 3:
                print("")
            case 4:
                print("")
            case 5:
                print("")
            case 6:
                print("")
                break
            case _:
                print("")