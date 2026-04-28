from calculator import suma, resta, multiplicacion, division
from app.resources import obtener_numero_positivo

def main():
    print("Calculadora de números positivos")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División \n")

    opcion = input("Ingresa el número de la operación: ")

    try:    
        num1 = obtener_numero_positivo(float(input("Ingresa el primer número: ")))
        num2 = obtener_numero_positivo(float(input("Ingresa el segundo número: ")))
    
    except ValueError as e:
        print(f"Error: {e}")
        return

    if opcion == "1":
        resultado = suma(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
        resultado = resta(num1, num2)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
        resultado = multiplicacion(num1, num2)
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == "4":
        try:
            resultado = division(num1, num2)
            print(f"El resultado de la división es: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()