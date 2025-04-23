
#2. Verificar si un número está en una lista Crea una lista con 5 números.
#Pide un número al usuario y verifica si está en la lista usando in.

Numeros = [10, 25, 42, 67, 90]

print("Lista de números:", Numeros)

NumeroUsuario = int(input("Ingresa un número para verificar si está en la lista: "))

if NumeroUsuario in Numeros:
    print(f"El número {NumeroUsuario} SÍ está en la lista.")
else:
    print(f"El número {NumeroUsuario} NO está en la lista.")