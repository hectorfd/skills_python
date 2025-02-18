# el programa pedira numeros para promediarlos

suma = 0
numero = 1
contador = 0

while numero != 0:
    print("Puede ingresar 0 para terminar el programa y mostrar los resultados16")
    numero = int(input("Introduce un número: "))
    if numero == 0:
        break 
    suma += numero
    contador += 1
print(suma / contador)