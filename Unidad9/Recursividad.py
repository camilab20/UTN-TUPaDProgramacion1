
# Ejercicio 1

def factorial(n):
    
    ## Calcula el factorial de n de forma recursiva
    ## n debe ser entero >= 0
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Programa principal
numero = int(input("Ingresá un número entero positivo: "))

if numero < 1:
    print("El número debe ser mayor o igual a 1")
else:
    print(f"Factoriales desde 1 hasta {numero}:")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")



# Ejercicio 2

def fibonacci(pos):
    
    ## Devuelve el número de Fibonacci en la posición 'pos' de forma recursiva
  
    F(0) = 0
    F(1) = 1
    
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)


# Programa principal
n = int(input("Ingresá la posición máxima de la serie de Fibonacci (entero >= 0): "))

if n < 0:
    print("La posición debe ser mayor o igual a 0")
else:
    print(f"Serie de Fibonacci hasta la posición {n}:")
    for i in range(n + 1):
        print(f"F({i}) = {fibonacci(i)}")



# Ejercicio 3

def potencia(base, exponente):
    
    ## Calcula base^exponente de forma recursiva
    ## Suponemos exponente entero >= 0
    
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


# Programa principal
base = float(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente (entero >= 0): "))

if exponente < 0:
    print("El exponente debe ser mayor o igual a 0")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado}")



# Ejercicio 4

def decimal_a_binario(n):

   ## Convierte un entero decimal n (>= 0) a su representación binaria (string) de forma recursiva

    if n < 2:  # 0 o 1
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


# Programa principal
numero = int(input("Ingresá un número entero positivo para convertir a binario: "))

if numero < 0:
    print("El número debe ser mayor o igual a 0.")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")



# Ejercicio 5 

def es_palindromo(palabra, inicio=0, fin=None):
    
    ## Devuelve True si 'palabra' es un palíndromo, False en caso contrario.
    
    if fin is None:
        fin = len(palabra) - 1

    # Caso base: índices se cruzan o se tocan
    if inicio >= fin:
        return True

    # Si los caracteres no coinciden, no es palíndromo
    if palabra[inicio] != palabra[fin]:
        return False

    # Llamada recursiva hacia el centro
    return es_palindromo(palabra, inicio + 1, fin - 1)


# Programa principal
texto = input("Ingresá una palabra (sin espacios ni tildes): ")
if es_palindromo(texto):
    print(f'"{texto}" ES un palíndromo')
else:
    print(f'"{texto}" NO es un palíndromo')




# Ejercicio 6 

def suma_digitos(n):
    
    ## Suma los dígitos de un número entero positivo de forma recursiva
    
    if n < 10:
        return n
    else:
        ultimo = n % 10
        resto = n // 10
        return ultimo + suma_digitos(resto)


# Programa principal
numero = int(input("Ingresá un número entero positivo: "))

if numero < 0:
    print("El número debe ser mayor o igual a 0")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")




# Ejercicio 7 

def contar_bloques(n):
    
    ## Devuelve el total de bloques necesarios para una pirámide cuya base tiene n bloques,
    ## el siguiente nivel n-1, y así sucesivamente hasta 1.
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


# Programa principal
nivel_base = int(input("Ingresá la cantidad de bloques en el nivel más bajo: "))

if nivel_base <= 0:
    print("La cantidad de bloques debe ser mayor o igual a 1")
else:
    total = contar_bloques(nivel_base)
    print(f"Para una pirámide con base {nivel_base} se necesitan {total} bloques en total")
    