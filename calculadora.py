# calculadora.py
# Calculadora basica en Python

def calculadora():
    print("=== Calculadora Basica ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    opcion = input("Seleccione una operacion (1-4): ")

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    if opcion == '1':
        resultado = num1 + num2
        operacion = "suma"
    elif opcion == '2':
        resultado = num1 - num2
        operacion = "resta"
    elif opcion == '3':
        resultado = num1 * num2
        operacion = "multiplicacion"
    elif opcion == '4':
        if num2 == 0:
            print("Error: no se puede dividir por cero.")
            return
        resultado = num1 / num2
        operacion = "division"
    else:
        print("Opcion no valida.")
        return

    print(f"El resultado de la {operacion} es: {resultado}")

calculadora()
