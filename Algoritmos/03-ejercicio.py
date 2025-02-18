#Escriba un programa en Python que acepte un país (como «string») y muestre por pantalla su bandera
#(como «emoji»). Puede   restringirlo   a   un   conjunto   limitado   de   países
#(por   ejemplo,   España,   Francia,   Alemania, Italia, México, Argentina, Brasil, Colombia, Chile, Perú, Venezuela).
from emoji import emojize
print ("\U0001F600")
snake = emojize(":snake:")
peru = emojize(":flag_pe:")
print("\U0001F1E6\U0001F1F7")
print(snake, peru)
def obtener_bandera(pais):
    banderas = {
        "España": "\U0001F1EA\U0001F1F8",
        "Francia": "\U0001F1EB\U0001F1F7",
        "Alemania": "\U0001F1E9\U0001F1EA",
        "Italia": "\U0001F1EE\U0001F1F9",
        "México": "\U0001F1F2\U0001F1FD",
        "Argentina": "\U0001F1E6\U0001F1F7",
        "Brasil": "\U0001F1E7\U0001F1F7",
        "Colombia": "\U0001F1E8\U0001F1F4",
        "Chile": "\U0001F1E8\U0001F1F1",
        "Perú": "\U0001F1F5\U0001F1EA",
        "Venezuela": "\U0001F1FB\U0001F1EA"
    }
    return banderas.get(pais, "Bandera no disponible")

pais = input("Introduce el nombre de un país: ")
print(obtener_bandera(pais))