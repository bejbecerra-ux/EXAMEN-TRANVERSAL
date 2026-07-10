def mostrar_menu():
    print("========== MENÚ PRINCIPAL ===========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

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

def unidades_categoria(categoria, productos, stock):
    categoria_buscada = categoria.lower()
    total_unidades = 0
    encontrado = False 

    
    for codigo, info in productos.items():
        categoria_producto = info[1].lower() 
        
        if categoria_producto == categoria_buscada:
            encontrado = True
            if codigo in stock:
                total_unidades += stock[codigo][1]
                
    if encontrado:
        print(f"El total de unidades disponibles para la categoría '{categoria}' es: {total_unidades}")
    else:
        print(f"No se encontraron productos en la categoría '{categoria}'.")

def busqueda_precio(p_min, p_max, productos, stock):
    if p_min < 0 or p_max < 0 or p_min > p_max:
        print("Error: Los precios deben ser mayores o iguales a cero, y el precio mínimo no puede superar al máximo.")

    lista_resultados = []

    for codigo, info_stock in stock.items():
        precio = info_stock[0]
        cantidad = info_stock[1]

        if p_min <= precio <= p_max and cantidad > 0:
            if codigo in productos:
                nombre_producto = productos[codigo][0]
                lista_resultados.append(f"{nombre_producto} -- {codigo}")

    if lista_resultados:
        lista_resultados.sort() 
        print(f"\nProductos encontrados entre ${p_min} y ${p_max}:")
        for producto in lista_resultados:
            print(f"- {producto}")
    else:
        print("No hay productos en ese rango de precios.")
        
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

while True:
    mostrar_menu()
    opcion_elegida = leer_opcion()

    match opcion_elegida:
        case 1:
            print("=== UNIDADES POR CATEGORÍA ===")
            cat_usuario = input("Ingrese el nombre de la categoría (ej: comida, higiene, snack): ")
            
            unidades_categoria(cat_usuario, productos, stock)

        case 2:
            print("=== BÚSQUEDA DE PRODUCTOS POR RANGO DE PRECIO ===")
            
            while True:
                try:
                    precio_minimo = int(input("Ingrese el precio mínimo: "))
                    precio_maximo = int(input("Ingrese el precio máximo: "))
                    break 
                    
                except ValueError:
                    print("Debe ingresar valores enteros. Intente de nuevo.")

            busqueda_precio(precio_minimo, precio_maximo, productos, stock)
            
        case 3:
            print("")
           
        case 4:
            print("")
            
        case 5:
            print("")
            
        case 6:
            print("")
            break