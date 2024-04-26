import math

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def producto(a,b):
    return a*b
def division(a,b):
    if b !=0:
        return a/b
    else:
        print("Porfavor introduce un valor valido para b que no sea 0")
def potencia(a,b):
    return a**b
def raiz_cuadrada(a):
    return math.sqrt(a)
def seno(a):
    return math.sin(a)
def coseno(a):
    return math.cos(a)
def tangente(a):
    return math.tan(a)
def arseno(a):
    return math.asin(a)
def arcoseno(a):
    return math.acos(a)
def arctangente(a):
    return math.atan(a)
def factorial(a):
    #max num1=1558
    return math.factorial(a)
def g_r(a):
    return math.radians(a)
def r_g(a):
    return math.degrees(a)
def tetra(a,b):
    result = 1
    for _ in range(int(b)):
        result = math.pow(a,result)
    return result



def calculadora():
    print("Calculadora cientifica: \nEscoge una de las siguientes opciones:")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.Division")
    print("5.Potencia")
    print("6.Raiz Cuadrada")
    print("7.Seno")
    print("8.Coseno")
    print("9.Tangente")
    print("10.Arcseno")
    print("11.Arccoseno")
    print("12.Arctangente")
    print("13.Factorial")
    print("14.Passar de radiantes a grados")
    print("15.Passar de grados a radiantes")
    print("16.Tetracion")
    print("17.Salir")

    while True:
        opcion = input("Introduce una opcion del (1-17): ")
        if opcion in ['1', '2', '3', '4', '5', '16']:
            num1 = float(input("Ingrese el primero número: "))
            num2 = float(input("Ingrese el segundo número: "))
        elif opcion not in ['1', '2', '3', '4', '5', '16', '17']:
            num1 = float(input("Ingrese el número: "))

        if opcion == '1':
            print("Resultado de la suma:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado de la resta:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado de la multiplicación:", producto(num1, num2))
        elif opcion == '4':
            print("Resultado de la división:", division(num1, num2))
        elif opcion == '5':
            print("Resultado de la potencia:", potencia(num1, num2))
        elif opcion == '6':
            print("Resultado de la raiz cuadrada:", raiz_cuadrada(num1))
        elif opcion == '7':
            print("Resultado del seno:", seno(num1))
        elif opcion == '8':
            print("Resultado del coseno:", coseno(num1))
        elif opcion == '9':
            print("Resultado de la tangente:", tangente(num1))
        elif opcion == '10':
            print("Resultado del arcseno:", arseno(num1))
        elif opcion == '11':
            print("Resultado del arcoseno:", arcoseno(num1))
        elif opcion == '12':
            print("Resultado de la arctangente:", arctangente(num1))
        elif opcion == '13':
            print("Resultado del factorial:", factorial(num1))
        elif opcion == '14':
            print(num1, "radiantes son", r_g(num1), "grados")
        elif opcion == '15':
            print(num1, "grados son", g_r(num1), "radiantes")
        elif opcion == '16':
            print("Resultado de la tetracion:", tetra(num1, num2))
        elif opcion == '17':
            print("Hasta luego.")
            break
        else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

calculadora()
