

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def calcular_circulo(radio):
    import math
    area = math.pi * radio ** 2
    return area

def calcular_promedio(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return promedio

def calcular_promedio_avanzado(numeros):
    import statistics
    promedio = statistics.mean(numeros)
    return promedio


def generar_numeros_aleatorios(cantidad, limite):
    import random
    numeros_aleatorios = [random.randint(1, limite) for _ in range(cantidad)]
    return numeros_aleatorios

def validanumero(tipo,mensaje):
    while True:
        try:
            if tipo == "int":
              numero = int(input(mensaje))
            elif tipo == "float":
              numero = float(input(mensaje))
            break  # Salir del bucle si el input es válido
        except ValueError:
            print("Error: Debes ingresar un número válido.")
    return numero


#area triangulo
print("Area de triángulo")
print("-----------------")
base = validanumero("float","Ingrese la base del rectángulo: ")
altura = validanumero("float","Ingrese la altura del rectángulo: ")
area = calcular_area_rectangulo(base, altura)
print("El área del rectángulo es:", area)

print("\n")

#area circulo
print("Area de círculo")
print("---------------")
radio = validanumero("float","Ingrese el radio del círculo: ")
area = calcular_circulo(radio)
print("El área del círculo es:", area)

print("\n")


#calculo promedio
print("Cálculo de Promedio")
print("-------------------")
numero="0"
while numero != 0:
    numeros = []
    while True:
        numero = validanumero("float","Ingrese un número (0 para finalizar): ")
        if numero == 0:
            break
        numeros.append(numero)
promedio = calcular_promedio(numeros)
promedio_avanzado = calcular_promedio_avanzado(numeros)
print("El promedio de los números ingresados es:", promedio)
print("El promedio avanzado de los números ingresados es:", promedio_avanzado)

print("\n")

#numeros aleatorios
print("Generar número aleatorios")
print("-------------------------")
limite = validanumero("int","Ingrese el límite: ")
cantidad = validanumero("int","Ingrese la cantidad a generar: ")
numeros_aleatorios = generar_numeros_aleatorios(cantidad, limite)
print("Números aleatorios generados:", numeros_aleatorios)

print("\n")
