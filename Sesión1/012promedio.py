#el programa calcula y muestra el prmedio de calificaciones de un alumno

print('el programa muestra el promedio de 3 calificaicones\n')
nombre = str(input('Introduce tu nombre: '))
mat = float(input('Escribe tu calificación de matemáticas: '))
fis = float(input('Escribe tu calificación de física: '))
qui = float(input('Escribe tu calificación de química: '))

promedio = (mat + fis + qui) / 3

print(f'El promedio de {nombre} es: {round(promedio)}')