"""1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne."""

# def devolver_nro_entero():
#     """
#     Solicita al usuario el ingreso de un numero entero y lo retorna
#     """
#     numero = int(input("Ingrese un numero: "))
#     return numero

# numero_entero = devolver_nro_entero()
# print(numero_entero)


"""2) Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne."""

# def devolver_nro_flotante():
#     """
#     Solicita al usuario el ingreso de un numero flotante y lo retorna
#     """
#     numero_float = float(input("Ingrese un numero: "))
#     return numero_float

# nro_float = devolver_nro_flotante()
# print(nro_float)

# numero = input("Ingrese un numero flotante: ")

# if numero.count(".") == 1:
#     print("Es flotante")
# else:
#     print("No es flotante")
"""3) Crear una función que le solicite al usuario el ingreso de una cadena y la retorne."""

# def devolver_cadena_texto():
#     """
#     Solicita al usuario el ingreso de una cadena de texto y lo retorna
#     """
#     ingreso_texto = input("Ingrese el texto: ")
#     return ingreso_texto

# texto = devolver_cadena_texto()
# print(texto)

#                                            DUDAS EN LA VALIDACION DE ESTE


"""4) Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. """

# def calcular_area_rectangulo(base, altura):
#     """Calcula el area de un rectangulo ingresando la base y su altura

#     Args:
#         base: base del rectangulo
#         altura: altura del rectangulo
#     """
#     area = base * altura
#     return area

# area_rectangulo = calcular_area_rectangulo(5, 3)
# print(area_rectangulo)

# SI RETORNA HAY QUE LLAMARLO POR EJEMPLO EN area_rectangulo PARA DESPUES IMPRIMIRLO, SI EN VEZ DE UN RETURN
# LE PONEMOS UN PRINT EN LA FUNCION DIRECTAMENTE SE PUEDE HACER ASI calcular_area_rectangulo(5, 3) Y MARCA EL RESULTADO


"""5) Escribe una función que calcule el área de un círculo. La función debe 
recibir el radio como parámetro y devolver el área."""

# def calcular_area_circulo(radio):
#     """Calcula el area de un circulo ingresando su radio

#     Args:
#         radio: el radio del circulo 
#     """
#     pi = 3.14
#     area = pi * radio ** 2
#     return area

# area_circulo = calcular_area_circulo(2)
# print(area_circulo)


"""6) Crea una función que verifique si un número dado es par o impar. La función 
debe imprimir un mensaje indicando si el número es par o impar."""

# def verificar_numero_par_impar(numero):
#     """Dado un numero imprime si es par o impar
#     """
#     if numero % 2 == 0:
#         print(f"{numero} es PAR")
#     else:
#         print(f"{numero} es IMPAR")

# verificar_numero_par_impar(2)


"""7) Crea una función que verifique si un número dado es par o impar. La función retorna
True si el número es par, False en caso contrario."""

# def verificar_numero_par_impar(numero):
#     """Dado un numero retorna TRUE si es par o FALSE impar
#     """
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# numero = verificar_numero_par_impar(5)
# print(numero)


"""8) Define una función que encuentre el máximo de tres números. La función debe
aceptar tres argumentos y devolver el número más grande."""

# def encontrar_numero_maximo(numero_1, numero_2, numero_3):
#     """Dados 3 numeros encuentra el numero mayor

#     Args:
#         numero_1:
#         numero_2:
#         numero_3:
#     """
#     if numero_1 >= numero_2 and numero_1 >= numero_3:
#         return numero_1
#     elif numero_2 >= numero_1 and numero_2 >= numero_3:
#         return numero_2
#     else:
#         return numero_3

# numero = encontrar_numero_maximo(240, 4, 100)
# print(f"El numero mayor es {numero}")


"""9) Diseña una función que calcule la potencia de un número. La función debe 
recibir la base y el exponente como argumentos y devolver el resultado."""

# def calcular_potencia_numero(nro_base, exponente):
#     """

#     Args:
#         nro_base (_type_): _description_
#         exponente (_type_): _description_
#     """
#     nro_a_calcular = nro_base ** exponente
#     return nro_a_calcular

# numero = calcular_potencia_numero(5, 3)
# print(numero)

"""10) Crear una función que reciba un número y retorne True si el número es primo, 
False en caso contrario."""