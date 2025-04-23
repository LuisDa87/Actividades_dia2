#5. ¿Está en la lista de invitados? Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
# Pide al usuario su nombre. Usa if para decir si está en la lista de invitados o no.


invitados = ["Ana", "Luis", "Sofía", "Carlos", "Elena"]

print("Lista de invitados:", invitados)

nombre_usuario = input("Por favor, ingresa tu nombre: ")

if nombre_usuario in invitados:
    print(f"¡Bienvenido/a {nombre_usuario}! Estás en la lista de invitados.")
else:
    print(f"Lo siento {nombre_usuario}, no estás en la lista de invitados.")