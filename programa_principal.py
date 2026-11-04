# Importación de Colorama.
from colorama import init
init()

from colorama import Fore, Back, Style, init
# Resetea de manera automática los colores mostrados en la terminal.
init(autoreset=True)

# Importación de Datetime.
import datetime

# Crear una lista vacía para almacenar el nombre de los productos y su precio.
lista_productos = []

#------------------------------------------------------------------------------------
# Función para agregar productos.
def agregar_productos():
    nombre_producto = input("Ingresá el nombre del producto: ").capitalize().strip()
    precio_producto = (input("Ingresá su precio sin puntos, guiones ni comas: ")).strip()
    return nombre_producto, precio_producto
#------------------------------------------------------------------------------------
# Función para consultar(mostrar) todos los productos.
def consultar_productos():
  if lista_productos:
    return lista_productos
  else:
    return []
#------------------------------------------------------------------------------------
# Función para eliminar un producto por su nombre.
def eliminar_producto():
  """
  Elimina un producto de la lista de productos.

  Dato de entrada:
    Se pide el nombre del producto al usuario mediante un input.

  Retorna:
    Si el producto existe:
      sublista: con el "nombre del producto" y su precio.

  Retorna:
    Si el producto no existe en la lista_productos:
      None: Ninguno/nada.
  """
  producto_a_eliminar = input("Ingresá el nombre del producto a eliminar: ").capitalize().strip()

  for producto in lista_productos:
    if producto_a_eliminar == producto[0]:
      lista_productos.remove(producto)
      return producto

  return None
#------------------------------------------------------------------------------------
# Función para mostrar el menú de opciones.
def mostrar_menu():
  while True:
    print("\nMenú de opciones:")
    print("1. Agregar producto.")
    print("2. Mostrar productos.")
    print("3. Eliminar producto.")
    print("4. Salir")

    opcion_elegida = input("Ingrese un número del 1 al 4, según la opción requerida: ").strip()
    #----------------------------------------------------------------------------------------
    if opcion_elegida == "1":
      nombre_producto, precio_producto = agregar_productos()
      # Declaración e inicialización de la librería datetime con el horario actual del dispositivo.
      fecha_y_hora_actual = datetime.datetime.now()
      lista_productos.append([nombre_producto, precio_producto, fecha_y_hora_actual])
      agregado = f'\nProducto: {nombre_producto} y precio: ${precio_producto}, agregados con éxito el día {fecha_y_hora_actual.strftime("%d-%m-%Y")} a las {fecha_y_hora_actual.strftime("%H:%M:%S")}.'
      print(Fore.BLACK + Back.GREEN + agregado)
    #----------------------------------------------------------------------------------------
    elif opcion_elegida == "2":
      productos = consultar_productos()
      if productos:
        for indice, producto in enumerate(productos, start=1):
          consultados = f'\nProducto Nro: {indice}, Nombre: {producto[0]}, Precio: ${producto[1]}, Fecha: {producto[2].strftime("%d-%m-%Y")}, Hora: {producto[2].strftime("%H:%M:%S")}'
          print(Fore.BLACK + Back.GREEN + consultados)
      else:
        print(Fore.WHITE + Back.RED + "\n¡ERROR! No hay productos cargados en la lista para ser consultados.")
    #----------------------------------------------------------------------------------------
    elif opcion_elegida == "3":
      producto_eliminado = eliminar_producto()
      
      if producto_eliminado:
        eliminado = f'\nEl producto: {producto_eliminado[0]}, fue eliminado con éxito.'
        print(Fore.BLACK + Back.GREEN + eliminado)
      else:
        print(Fore.WHITE + Back.RED + "\n¡ERROR! El producto no está en la lista.")
    #----------------------------------------------------------------------------------------
    elif opcion_elegida == "4":
      print("¡Gracias por utilizar el programa! ¡Adiós!")
      break
    else:
      print(Fore.WHITE + Back.RED + "\n¡ERROR! ¡Opción inválida! Ingrese una de las opciones enumeradas en el menú de opciones.")

#------------------------------------------------------------------------------------
# Función que activa el menú de opciones.
mostrar_menu()

# help(eliminar_producto)