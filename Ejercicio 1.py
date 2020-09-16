import math

def suma(numero1 , numero2):
    print('\n El total de la suma es: ', numero1+numero2)

def resta(numero1 , numero2):
    print('\n El total de la resta es: ', numero1-numero2)

def multiplicacion(numero1 , numero2):
    print('\n El total de la multiplicacion es: ', numero1*numero2)

def division(numero1 , numero2):
    print('\n El total de la division es: ', numero1/numero2)

def seno(numero1):
    print('\n El Seno es: ', math.sin(math.radians(numero1)))

def coseno(numero1):
    print('\n El Coseno es: ', math.cos(math.radians(numero1)))

def tangente(numero1):
    print('\n La Tangente es: ', math.tan(math.radians(numero1)))

def potencia(numero1 , numero2):
    print('\n El total es: ', pow(numero1,numero2))

def raiz_cuadrada(numero1):
    print('\n La raiz cuadrada es : ', math.sqrt(numero1))

#menu de la calculadora
def menu_calculadora():
    print("\n CUALES DE LAS SIGUIENTES OPCIONES QUIERE OCUPAR")
    print("1. OPERACIONES BASICAS")
    print("2. FUNCIONES TRIGONOMETRICAS")
    print("3. POTENCIA")
    print("4. RAIZ CUADRADA")
    print("5. SALIR")

def menu_Basicas():
    print("\n CUALES DE LAS OPERACIONES BASICAS QUIERE OCUPAR")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. VOLVER AL MENU PRINCIPAL")

def menu_Trigonometricas():
    print("\n CUALES DE LAS FUNCIONES TRIGONOMETRICAS QUIERE OCUPAR")
    print("1. SENO")
    print("2. COSENO")
    print("3. TANGENTE")
    print("4. VOLVER AL MENU PRINCIPAL")

#Procedimiento
def calculadoraglobal():
    menu_calculadora()
    opcion = int(input("Ingrese una opcion: "))
    while True:
        if (opcion == 1):
            menu_Basicas()
            opcio = int(input("Ingrese una opcion: "))
            if (opcio == 1):
                numero1 = int(input("Ingrese un numero:  "))
                numero2 = int(input("Ingrese un segundo numero:  "))
                suma(numero1,numero2)
            elif (opcio == 2):
                numero1 = int(input("Ingrese un numero:  "))
                numero2 = int(input("Ingrese un segundo numero:  "))
                resta(numero1,numero2)
            elif (opcio == 3):
                numero1 = int(input("Ingrese un numero:  "))
                numero2 = int(input("Ingrese un segundo numero:  "))
                multiplicacion(numero1,numero2)
            elif (opcio == 4):
                numero1 = int(input("Ingrese un numero:  "))
                numero2 = int(input("Ingrese un segundo numero:  "))
                division(numero1,numero2)
            elif (opcio == 5):
                return calculadoraglobal()
        elif (opcion == 2):
            menu_Trigonometricas()
            opcio = int(input("Ingrese una opcion: "))
            if (opcio == 1):
                numero1 = int(input("Ingrese un numero:  "))
                seno(numero1)
            elif (opcio == 2):
                numero1 = int(input("Ingrese un numero:  "))
                coseno(numero1)
            elif (opcio == 3):
                numero1 = int(input("Ingrese un numero:  "))
                tangente(numero1)
            elif (opcio == 4):
                return calculadoraglobal()
        elif ( opcion == 3):
            numero1 = int(input("Ingrese un numero:  "))
            numero2 = int(input("Elevado a :  "))
            potencia(numero1,numero2)
            return calculadoraglobal()
        elif ( opcion == 4):
            numero1 = int(input("Ingrese un numero:  "))
            raiz_cuadrada(numero1)
            return calculadoraglobal()
        elif (opcion == 5):
            break
        else:
            print("\nEsta opcion no existe")
            return calculadoraglobal()
print(calculadoraglobal())

                
            


