#El cliente pide un programa que pida al usuario su nombre y su edad
#el programa debe evaluar su edad y si es mayor de 18 años debe mostrar un mensaje que puede votar

nombre = str(input("Introduce tu nombre: "))
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print(f"{nombre}: puede votar")
else:
    print(f"{nombre}: no puede votar")