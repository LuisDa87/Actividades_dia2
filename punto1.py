
#1. Menor de tres números Pide tres números al usuario. Usa condicionales (if) para decir cuál es el más pequeño.


num1=int(input("Ingresa el num uno: "))
num2=int(input("Ingresa el num dos: "))
num3=int(input("Ingresa el num tres: "))

if num1>num2 and num1>num3:
    print("el numero 1 es mayor -> ", num1)
elif num2>num1 and num2>num3:
    print("el numero 2 es mayor ->", num2)
else:
    print("el numero 3 es mayor ->", num3)

