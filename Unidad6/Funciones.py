#Imprimir "Hola Mundo"
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


#Saludo
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))


#Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


#Área y perímetro de un círculo
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


#Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas.")


#Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla: "))
tabla_multiplicar(numero)


#Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return suma, resta, producto, division

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
suma, resta, producto, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {producto}, División: {division}")


#Calcular IMC (Índice de Masa Corporal)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")


#Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Temperatura en °C: "))
print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F.")


#Calcular promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
