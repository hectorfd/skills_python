#si estatura es menor a 1.60 eres bajo
#si estatura es mayor a 1.60 y menor a 1.75 eres mediano
#si estatura es mayor a 1.75 eres alto

nombre = str(input("Introduce tu nombre: "))
estatura = float(input("Introduce tu estatura: "))

if estatura < 1.60:
    print(f"{nombre}: eres bajo, tu estatura es: {estatura}")
elif estatura >= 1.60 and estatura < 1.75:
    print(f"{nombre}: eres mediano, tu estatura es: {estatura}")
elif estatura >= 1.75:
    print(f"{nombre}: eres alto, tu estatura es: {estatura}")