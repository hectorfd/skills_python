# Escriba un programa en Python que acepte la opción de dos jugadoras en Piedra-Papel
print("Juego Piedra, Papel y Tijeras")
jugador1 = input(str("jugador 1 escriba su elección Piedra, Papel o Tijeras: "))
jugador2 = input(str("jugador 2 escriba su elección Piedra, Papel o Tijeras: "))
if(jugador1 == jugador2):
    print("Empate")
elif(jugador1 != jugador2):
    if(jugador1 == "Piedra" and jugador2 == "Papel"):
        print("Gana jugador 2")
    elif(jugador1 == "Papel" and jugador2 == "Piedra"):
        print("Gana jugador 1")
    elif(jugador1 == "Papel" and jugador2 == "Tijeras"):
        print("Gana jugador 2")
    elif(jugador1 == "Tijeras" and jugador2 == "Papel"):
        print("Gana jugador 1")
    elif(jugador1 == "Piedra" and jugador2 == "Tijeras"):
        print("Gana jugador 1")
    elif(jugador1 == "Tijeras" and jugador2 == "Piedra"):
        print("Gana jugador 2")
    else:
        print(f"Error jugador 1 ingreso {jugador1} y el jugador 2 ingreso {jugador2}")