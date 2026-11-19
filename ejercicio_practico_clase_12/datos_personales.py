# Importación de módulos
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Título del programa.
print('\n' + Fore.BLACK + Back.YELLOW + "=== Registro de Clientes ===")
print("\n#--- Ingresá los datos del cliente ---#\n")

# Se piden los tres datos personales: Nombre, Apellido y Dirección de Correo.
#--------------------NOMBRE-----------------------------#
# Se utiliza el ValueError porque describe mejor el tipo de error que se quiere atrapar, en este caso un campo vacío.
try:
    nombre = input("Ingresá el nombre del cliente: ").capitalize().strip()

    if nombre == "":
        raise ValueError() # Se lanza la excepción con ValueError sin argumentos.
    
except ValueError:
    while nombre == "":
        print(Fore.WHITE + Back.RED + "[ERROR] ¡No podes dejar el campo vacío!") 
        nombre = input("Volvé a ingresar el nombre del cliente: ").capitalize().strip() 

#--------------------APELLIDO---------------------------#
try:
    apellido = input("Ingresá su apellido: ").capitalize().strip()
    if apellido == "":
        raise ValueError() # Se lanza la excepción con ValueError sin argumentos.

except ValueError:
    while apellido == "":
        print(Fore.WHITE + Back.RED + "[ERROR] ¡No podes dejar el campo vacío!")
        apellido = input("Volvé a ingresar el apellido del cliente: ").capitalize().strip()
 
#---------------CORREO ELECTRÓNICO----------------------#
try:
    correo_Electronico = input("ingresá su correo electrónico: ").strip()

    if correo_Electronico == "" or not "@" in correo_Electronico:
        raise ValueError() # Se lanza la excepción forzada de ValueError porque es un error de valor no de type.

except ValueError:
    while correo_Electronico == "" or not "@" in correo_Electronico:
        if correo_Electronico == "":
            print(Fore.WHITE + Back.RED + "[ERROR] ¡El campo Correo Electrónico no puede estar vacío!")
            correo_Electronico = input("Volvé a ingresar el correo electrónico del cliente: ").strip()

        elif not "@" in correo_Electronico:
            print(Fore.WHITE + Back.RED + "[ERROR] ¡Tu formato de correo es inválido!")
            correo_Electronico = input("Volvé a ingresar un correo válido. (Ej: nombre@example.com): ").strip()


# Creación y guardado de los datos ingresados en un archivo clientes.txt
try:
    # Crear y agregar texto a un archivo clientes.txt
    clientes = open("clientes.txt", "a")
    clientes.write(f'{nombre}, ')
    clientes.write(f'{apellido}, ')
    clientes.write(f'{correo_Electronico}\n')
    clientes.close()

    # Mostrar los datos almacenados.
    print(Fore.BLACK + Back.GREEN + f'\nNombre: {nombre}')
    print(Fore.BLACK + Back.GREEN + f'\nApellido: {apellido}')
    print(Fore.BLACK + Back.GREEN + f'\nCorreo: {correo_Electronico}') 

    print("\nCliente registrado con éxito en clientes.txt\n")

    #Leer y mostrar el contenido del archivo.
    # clientes = open("clientes.txt", "r")
    
    # for linea in clientes:
    #     print(Fore.BLACK + Back.GREEN + linea)
    # clientes.close()

except PermissionError:
    print("\n[ERROR] No se pudo guardar la información.")