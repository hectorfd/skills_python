#simular el conteo regresivo del despegue
import time
contador = 10
while contador > 0:
    print(contador)
    time.sleep(1)
    contador -= 1
print("Despegue")