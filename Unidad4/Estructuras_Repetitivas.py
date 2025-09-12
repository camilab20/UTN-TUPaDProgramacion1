#Ejercicio 1: imprimir los numeros enteros del 0 al 100, mostrando un numero por linea

for i in range (101):
    print (i)



#Ejercicio 2: solicitar al usuario un numero entero y determinar la cantidad de digitos que contiene

numero = int(input("Ingrese un numero entero: "))
n_abs = abs(numero)             #transforma negativos en positivos

if n_abs == 0:
    contador = 1
else:
    contador = 0
    while n_abs > 0:
        n_abs //= 10        #elimina el último dígito
        contador += 1       #sumamos 1 al contador

print("Cantidad de dígitos:", contador)



#Ejercicio 3: sumar enteros entre dos valores (sin incluirlos)

a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))

menor = min(a, b)
mayor = max(a, b)

suma = 0
for i in range(menor + 1, mayor):  # desde menor+1 hasta mayor-1
    suma += i

print("La suma (sin incluir extremos) es:", suma)



#Ejercicio 4: sumar números enteros en secuencia hasta que el usuario ingrese 0

total = 0

while True:      #bucle infinito, lo cortamos con break
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break   
    total += num

print("La suma total es:", total)



#Ejercicio 5: adivinar un número entre 0 y 9

import random
numero_secreto = random.randint(0, 9)  #generar un número aleatorio
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! El número era", numero_secreto)
        break  #sale del bucle
    else:
        print("Incorrecto, intenta de nuevo.")

print("Número de intentos:", intentos)



#Ejercicio 6: imprimir números pares entre 0 y 100 en orden decreciente

for i in range(100, -1, -2):  #va desde 100 hasta 0, bajando de 2 en 2
    print(i)



#Ejercicio 7

numero = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(numero + 1):  # de 0 hasta n
    suma += i

print("La suma desde 0 hasta", numero, "es:", suma)



#Ejercicio 8: pares, impares, negativos y positivos (100 números)

cantidad = 100  
num = 0
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    #par o impar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    #positivo o negativo
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)



#Ejercicio 9: calcular la media de 100 numeros

cantidad = 100
suma = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

media = suma / cantidad
print("La media de los números es:", media)



#Ejercicio 10: invertir los digitos de un numero

n = input("Ingrese un número: ")  
invertido = n[::-1] 

print("Número invertido:", invertido)