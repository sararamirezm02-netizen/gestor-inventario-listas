productos = []
cantidades = []

def buscar_indice(nombre):
    nombre = nombre.strip().lower()
    for i in range(len(productos)):
        if productos[i].lower() == nombre:
            return i
    return -1

def registrar_producto():
    nombre = input("Nombre del producto: ").strip()
    if buscar_indice(nombre) != -1:
        print("Ese producto ya esta registrado.")
    else:
        cantidad = int(input("Cantidad disponible: "))
        productos.append(nombre)
        cantidades.append(cantidad)
        print("Producto registrado.")

def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        for i in range(len(productos)):
            print(i + 1, productos[i], "-", cantidades[i])

def buscar_producto():
    nombre = input("Producto a buscar: ").strip()
    i = buscar_indice(nombre)
    if i == -1:
        print("El producto no existe.")
    else:
        print("Encontrado:", productos[i], "-", cantidades[i])

def modificar_cantidad():
    nombre = input("Producto a modificar: ").strip()
    i = buscar_indice(nombre)
    if i == -1:
        print("El producto no existe.")
    else:
        cantidades[i] = int(input("Nueva cantidad: "))
        print("Cantidad actualizada.")
def eliminar_producto():
    nombre = input("Producto a eliminar: ").strip()
    i = buscar_indice(nombre)
    if i == -1:
        print("El producto no existe.")
    else:
        productos.pop(i)
        cantidades.pop(i)
        print("Producto eliminado.")
def mostrar_resumen():
    print("Productos diferentes registrados:", len(productos))

def mostrar_mayor_cantidad():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        posicion_mayor = 0
        for i in range(1, len(cantidades)):
            if cantidades[i] > cantidades[posicion_mayor]:
                posicion_mayor = i
        print("Mayor cantidad:", productos[posicion_mayor], "-", cantidades[posicion_mayor])

opcion = ""
while opcion != "8":
    print("\n===== INVENTARIO =====")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Modificar cantidad")
    print("5. Eliminar producto")
    print("6. Cantidad de productos diferentes")
    print("7. Producto con mayor cantidad")
    print("8. Salir")
    opcion = input("Elija una opcion (1-8): ").strip()

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        modificar_cantidad()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        mostrar_resumen()
    elif opcion == "7":
        mostrar_mayor_cantidad()
    elif opcion == "8":
        print("Hasta luego.")
    else:
        print("Opcion no valida. Elija un numero entre 1 y 8.")
