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

def filtrar_libros_por_precio(libros, rango_ini, rango_fin):
    libros_filtrados = [libro for libro in libros if rango_ini <= libro["precio"] <= rango_fin]
    return libros_filtrados

def filtrar_libros_por_disponibilidad(libros, cant):
    libros_filtrados = [libro for libro in libros if libro["cantidad_en_stock"] > cant]
    return libros_filtrados

# 2. y 3. Muestro todos los disonibles cuando ini == 0 y fin == 0

def mostrar_libros(ini, fin, libros, que_libros):
    print("\n")
    #filtra todos los libros (que_libros=T) o solo con stock>0  (que_libros=D)
    if que_libros.lower() == "d":
        libros_filtrados = filtrar_libros_por_disponibilidad(libros, 0)
        tipo = " disponibles "
    else:
        libros_filtrados = libros
        tipo = " "
#filtra por rango de precio (si ini y fin son 0, no filtra )
    if (ini==0 and fin==0):
        print("Libros"+tipo+":")
    else:
        print(f"Libros"+tipo+"con Precio entre $" + str(ini) + "y $" + str(fin) + ":")
        libros_filtrados = filtrar_libros_por_precio(libros_filtrados,ini,fin)

    #muestra listado
    if not libros_filtrados:
      print("No hay libros disponibles.")
    else:
      for libro in libros_filtrados:
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Precio: {libro['precio']}")
        print(f"Cantidad en stock: {libro['cantidad_en_stock']}")
        print("\n")


# funcion comprar
def comprar_libros(libros,titulo, cantidad):
  encontrado = False
  for libro in libros:
    if libro["titulo"] == titulo:
      encontrado = True
      break

  if not encontrado:
    print(f"No se encontró un libro con el título '{titulo}'.")
  else:
      if libro["cantidad_en_stock"] >= cantidad:
        libro["cantidad_en_stock"] -= cantidad
        valor_compra = libro["precio"] * cantidad
        print(f"Se han comprado {cantidad} unidades de '{titulo}' por un valor de $ " + str(valor_compra) + ".")
      else:
        print(f"Stock insuficiente.")



#1. Definir variables básicas y tipos de datos (1 punto):
#o Crea una lista que contenga al menos cinco libros, donde cada libro sea un diccionario con los atributos título (cadena de caracteres), autor (cadena de caracteres), precio (decimal) y cantidad en stock (entero)

libros = []
datos_libro = {}

while True:
    print("\n")
    print("\033[4mIngrese los datos del libro:\033[0m\n")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    precio = validanumero("float","Precio: ")
    cant = validanumero("int","Stock: ")
    salir = input("Desea continuar? (s/n): ")
    datos_libro = {"titulo": titulo, "autor": autor, "precio": precio, "cantidad_en_stock": cant}
    libros.append(datos_libro)
    if salir.lower() == "n":
        break
print("\n")
mostrar_libros(0,0, libros, "D")

while True:
  rango_ini = validanumero("int","Ingrese precio mas bajo: ")
  rango_fin = validanumero("int","Ingrese precio mas alto: ")
  if rango_ini > rango_fin:
    print("El precio mas bajo no puede ser mayor al mas alto.")
  else:
    break

print("\nQuieres una lista de todos los libros o solo los disponibles? ")
while True:
  que_libros = input("T: todos/ D:disponibles): ")
  if que_libros.lower() == "d" or que_libros.lower() == "t":
    break
  else:
    print("Por favor, ingrese 'T' o 'D'.")

mostrar_libros(rango_ini, rango_fin, libros, que_libros)

while True:
  print("\n")
  print("\033[4mComprar libros:\033[0m\n")
  titulo = input("Ingrese el título del libro a comprar: ")
  cantidad = validanumero("int","Ingrese la cantidad a comprar: ")
  comprar_libros(libros,titulo, cantidad)
  print("\n")
  mostrar_libros(0,0, libros, "D")
  salir = input("Desea continuar? (s/n): ")
  if salir.lower() == "n":
    break
