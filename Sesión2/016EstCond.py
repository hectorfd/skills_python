#el programa pedira una cantidad de pesos y mostrara un menu de opciones para convertir a dolares o soles peruanos

pesos = float(input("Introduce la cantidad de pesos: "))
opcion = int(input("\n Cual moneda deseas convertir?"
                    "\n 1. Dólares"
                    "\n 2. Soles peruanos"
                    ))

if opcion == 1:
    dolares = pesos / 20
    print(f"{pesos} pesos son {dolares} dólares")
elif opcion == 2:
    soles = pesos / 5
    print(f"{pesos} pesos son {soles} soles peruanos")
else:
    print("Opción no válida")