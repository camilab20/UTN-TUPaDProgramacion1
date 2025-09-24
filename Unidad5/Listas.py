#Ejercicio 1: crear una lista con las notas de 10 estudiantes. Calcular promedio y nota mas alta y mas baja.

notas = [7, 8, 9, 6, 10, 5, 7, 9, 4, 10]

print("Nota de los estudiantes: ")
for n in notas:
    print(n, end= " ")
print()

promedio = sum (notas) / len(notas)
print("Promedio: ", promedio)

print("Nota mas alta:", max(notas))
print("Nota más baja:", min(notas))


#Ejercicio 2:  pedir al usuario que cargue 5 productos en una lista, ordenarlos alfabeticamente y preguntar cual desea eliminar

productos = []
for i in range (5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

print("Productos ordenados: ", sorted(productos))

eliminar = input("¿Que producto quiere eliminar?: ")
if eliminar in productos:
    productos.remove(eliminar)
else:
    print("Ese producto no estaba en la lista")

print("Lista actualizada:", productos)


#Ejercicio 3: lista con 15 números enteros al azar entre 1 y 100. Cuales son pares e impares y cuantos num tiene cada lista

import random
numeros = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Números:", numeros)
print("Pares:", pares, "- Cantidad:", len(pares))
print("Impares:", impares, "- Cantidad:", len(impares))


#Ejercicio 4: lista con valores repetidos
lista = [1, 3, 5, 3, 7, 1, 9, 5, 3]

#Eliminar repetidos usando set y volver a lista
sin_repetidos = list(set(lista))

print("Original:", lista)
print("Sin repetidos:", sin_repetidos)


#Ejercicio 5: lista con los nombres de 8 estudiantes presentes en clase,
#Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.

lista = ["Juan", "Pedro", "Felipe", "Camila", "Sofia", "Nicolas", "Macarena", "Renata"]

estud = input ("Quiere agregar o eliminar un estudiante? (agregar/eliminar")
if estud == "agregar":
    nuevo = input("Ingrese el nombre: ")
    lista.append(nuevo)
elif op == "eliminar":
    borrar = input("Ingrese el nombre: ")
    if borrar in lista:
        lista.remove(borrar)

print("Lista final:", lista)


#Ejercicio 6: lista con 7 números, rotar todos los elementos una posición hacia la derecha
lista = [1, 2, 3, 4, 5, 6, 7]

# Rotar una posición a la derecha
rotada = [lista[-1]] + lista[:-1]

print("Lista original:", lista)
print("Lista rotada:", rotada)


#Ejercicio 7: matriz 7x2 (mín y máx)
temperaturas = [
    [10, 20],
    [12, 22],
    [8, 25],
    [15, 30],
    [11, 28],
    [9, 18],
    [14, 27]
]

minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)
      

#Ejercicio 8: matriz con las notas de 5 estudiantes en 3 materias. Mostrar promedio de cada estudiante y materia.
notas = [
    [10, 8, 6]
    [9, 7, 8]
    [6, 7, 4]
    [9, 8, 10]
    [7, 5, 9]
]

#Promedio de cada estudiante
for i, fila in enumerate(notas):
    prom = sum(fila) / len(fila)
    print(f"Promedio estudiante {i+1}: {prom}")

#Promedio de cada materia
for j in range(3):
    materia = [notas[i][j] for i in range(5)]
    prom = sum(materia) / len(materia)
    print(f"Promedio materia {j+1}: {prom}")


#Ejercicio 10:
ventas = [
    [10, 20, 30, 40, 50, 60, 70],
    [5, 15, 25, 35, 45, 55, 65],
    [8, 18, 28, 38, 48, 58, 68],
    [12, 22, 32, 42, 52, 62, 72]
]

for i, fila in enumerate(ventas):
    total = sum(fila)
    print(f"Producto {i+1}: {total}")

# Día con mayores ventas
dias = [sum([ventas[i][j] for i in range(4)]) for j in range(7)]
print("Día con más ventas:", dias.index(max(dias)) + 1)

# Producto más vendido
totales = [sum(fila) for fila in ventas]
print("Producto más vendido:", totales.index(max(totales)) + 1)