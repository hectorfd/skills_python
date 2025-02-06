#Escriba un programa en Python que acepte 3 números y calcule el mínimo

intentos = 3
c = 0
while c < intentos:
    c+=1
    numero1 = int(input("Ingrese Numero: "))
    print(numero1)
    if c == 1:
        minimo = numero1
    else:
        if numero1 < minimo:
            minimo = numero1
            
print(f"El número mínimo es: {minimo}")