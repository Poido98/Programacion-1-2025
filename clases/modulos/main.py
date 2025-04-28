"""


"""
from console_output import mostrar_menu
from validar_datos import validar_numero_entre, validar_nombre_o_apellido
import os


def aplicacion():

    ejecutando = True
    nombre = None
    apellido = None


    while ejecutando:
        mostrar_menu()
        numero = input("Ingrese una opcion: ")
        opcion_int = validar_numero_entre(numero, 1, 4)

        match opcion_int:
            case 1:
                nombre = input("Ingrese su nombre: ")
                nombre = validar_nombre_o_apellido(nombre, "Incorrecto, excriba su apellido de nuevo: ")

                apellido = input("Ingrese su apellido: ")
                apellido = validar_nombre_o_apellido(apellido, "Incorrecto, excriba su apellido de nuevo: ")
            case 2:
                if nombre != None and apellido != None:
                    print(f"Hola {nombre} {apellido}")
                else:
                    print("Primero debe ir a la opcion 1")
            case 3:
                print("Aho va el genio, golazooooooo")
            case 4:
                ejecutando = False
                print("Saliendo del programa")
        os.system("pause")
        os.system("cls")

aplicacion()