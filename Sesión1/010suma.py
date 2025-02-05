#sumaremos dos numeros introducidos desde el teclado

#todos los grandes programas se dividen en tres partes
#? Entrada de datos
n1 = int(input('Introduce el primer número: ')) #!int es una función que convierte una cadena de texto en un número entero
n2 = int(input('Introduce el segundo número: '))#! si no indicamos int el programa considera que es una cadena de texto
#!esta es una lista de tipo de datos 
#* int -> entero
#* float -> decimal
#* str -> cadena de texto
#* bool -> booleano
#* list -> lista
#* tuple -> tupla
#* dict -> diccionario
#* set -> conjunto
#* None -> nulo
#? procesamiento de datos
resultado = n1 + n2
#? salida de datos
print('La suma de los números es:', resultado)
