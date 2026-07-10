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
        return

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
        print(f"Productos encontrados entre ${p_min} y ${p_max}:")
        for producto in lista_resultados:
            print(f"- {producto}")
    else:
        print("No hay productos en ese rango de precios con stock disponible.")

def buscar_codigo(codigo, stock):
    return codigo.upper() in stock

def actualizar_precio(codigo, nuevo_precio, stock):
    codigo_buscado = codigo.upper()

    if buscar_codigo(codigo_buscado, stock):
        stock[codigo_buscado][0] = nuevo_precio
        return True
    return False   

def validar_codigo_vacio(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_marca(marca):
    return marca.strip() != ""

def validar_peso(peso_str):
    try:
        peso = float(peso_str)
        return peso > 0
    except ValueError:
        return False

def validar_es_importado(opcion):
    return opcion.lower() in ['s', 'n']

def validar_es_para_cachorro(opcion):
    return opcion.lower() in ['s', 'n']

def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_unidades(unidades_str):
    try:
        unidades = int(unidades_str)
        return unidades >= 0
    except ValueError:
        return False


def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, productos, stock):
    cod_upper = codigo.upper()
    
    if cod_upper in productos or cod_upper in stock:
        return False
        
    importado_bool = (es_importado.lower() == 's')
    cachorro_bool = (es_para_cachorro.lower() == 's')
    
    productos[cod_upper] = [nombre, categoria, marca, float(peso_kg), importado_bool, cachorro_bool]
    stock[cod_upper] = [int(precio), int(unidades)]
    return True     

def eliminar_producto(codigo, productos, stock):
    codigo_buscado = codigo.upper()

    if buscar_codigo(codigo_buscado, stock):
        
        del productos[codigo_buscado]
        del stock[codigo_buscado]
        return True
    return False

def main():
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
                try:
                    precio_minimo = int(input("Ingrese el precio mínimo: "))
                    precio_maximo = int(input("Ingrese el precio máximo: "))
                    busqueda_precio(precio_minimo, precio_maximo, productos, stock)
                except ValueError:
                    print("Error: Debe ingresar valores enteros numéricos.")

            case 3:
                print("=== ACTUALIZAR PRECIO DE PRODUCTO ===")
                cod_usuario = input("Ingrese el código del producto (ej: M001): ")
                try:
                    precio_input = int(input("Ingrese el nuevo precio (entero positivo): "))
                    if precio_input > 0:
                        fue_actualizado = actualizar_precio(cod_usuario, precio_input, stock)
                        if fue_actualizado:
                            print("Precio actualizado con éxito.")
                        else:
                            print("Error: El código no existe.")
                    else:
                        print("Error: El precio debe ser un valor mayor a cero.")
                except ValueError:
                    print("Error: Debe ingresar un número entero válido.")
               
            case 4:
                print("=== AGREGAR PRODUCTO ===")
                codigo = input("Ingrese el código del producto: ")
                if not validar_codigo_vacio(codigo):
                    print("Error: El código no puede estar vacío.")
                    continue 

                nombre = input("Ingrese el nombre del producto: ")
                if not validar_nombre(nombre):
                    print("Error: El nombre no puede estar vacío.")
                    continue

                categoria = input("Ingrese la categoría: ")
                if not validar_categoria(categoria):
                    print("Error: La categoría no puede estar vacía.")
                    continue

                marca = input("Ingrese la marca: ")
                if not validar_marca(marca):
                    print("Error: La marca no puede estar vacía.")
                    continue

                peso_kg = input("Ingrese el peso en kg (mayor a cero): ")
                if not validar_peso(peso_kg):
                    print("Error: El peso debe ser un número numérico mayor a cero.")
                    continue

                es_importado = input("¿Es importado? (s/n): ")
                if not validar_es_importado(es_importado):
                    print("Error: Debe ingresar 's' o 'n'.")
                    continue

                es_para_cachorro = input("¿Es para cachorro? (s/n): ")
                if not validar_es_para_cachorro(es_para_cachorro):
                    print("Error: Debe ingresar 's' o 'n'.")
                    continue

                precio = input("Ingrese el precio (entero mayor a cero): ")
                if not validar_precio(precio):
                    print("Error: El precio debe ser un número entero mayor a cero.")
                    continue

                unidades = input("Ingrese las unidades (entero mayor o igual a cero): ")
                if not validar_unidades(unidades):
                    print("Error: Las unidades deben ser un número entero mayor o igual a cero.")
                    continue

                exito = agregar_producto(
                    codigo, nombre, categoria, marca, peso_kg, 
                    es_importado, es_para_cachorro, precio, unidades, 
                    productos, stock
                )
                if exito:
                    print("Producto agregado con éxito.")
                else:
                    print("Error: El código ya existe en el sistema. No se pudo registrar.")
                
            case 5:
                print("=== ELIMINAR PRODUCTO ===")
                cod_eliminar = input("Ingrese el código del producto que desea eliminar (ej: M001): ")
                fue_eliminado = eliminar_producto(cod_eliminar, productos, stock)
                
                if fue_eliminado:
                    print("Producto eliminado con éxito.")
                else:
                    print("Error: El código no existe.")
                
            case 6:
                print("Programa finalizado. Hasta luego.")
                break

            case _:
                print("Error: Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()