# Ejercicio 1: Crear archivo inicial (solo la primera vez)

def crear_archivo_inicial():
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,450.0,15\n")
        archivo.write("Goma,80.0,50\n")
    print("Archivo 'productos.txt' creado correctamente.\n")


# Ejercicio 2: Leer productos y mostrarlos

def leer_productos():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    print("\nListado de productos:")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    return productos


# Ejercicio 3: Agregar producto nuevo

def agregar_producto():
    nombre = input("\nIngrese el nombre del nuevo producto: ")
    precio = input("Ingrese el precio: ")
    cantidad = input("Ingrese la cantidad: ")
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado correctamente.\n")


# Ejercicio 4: Buscar producto por nombre

def buscar_producto(productos):
    nombre_buscar = input("\nIngrese el nombre del producto a buscar: ").capitalize()
    for p in productos:
        if p["nombre"].capitalize() == nombre_buscar:
            print(f"Producto encontrado:\n→ {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            return
    print("Producto no encontrado.")


# Ejercicio 5: Guardar lista actualizada (sobrescribe el archivo)

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo 'productos.txt' actualizado correctamente.\n")


# PROGRAMA PRINCIPAL

#crear_archivo_inicial()

productos = leer_productos()

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Guardar y salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
        productos = leer_productos()  # actualizo lista

    elif opcion == "2":
        buscar_producto(productos)

    elif opcion == "3":
        guardar_productos(productos)
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida. Intente nuevamente")

