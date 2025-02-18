# el programa contiene un numero secretos y el usuario debe adivinarlo
# tendra 3 oportunidades para adivinarlo

numero_secreto = 9
adivinado = False
intentos = 0
quedan = 3

while not adivinado and quedan > 0:
    numero = int(input("Adivina el número: "))
    intentos += 1
    quedan -= 1

    if numero == numero_secreto:
        adivinado = True
        print(f"Has adivinado el número en {intentos} intentos")
    else:
        print(f"El número secreto no es {numero}")
        
        print(f"Te quedan {quedan} intentos")
        if quedan == 0:
            print(f"El número secreto era {numero_secreto}")
            break
        