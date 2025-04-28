"""1) Mostrar los números ascendentes desde el 1 al 10"""

# for numero in range(1, 11, 1):
#     print(numero)


"""2) Mostrar los números descendentes desde el 10 al 1"""

# for numero in range(10, 0, -1):
#     print(numero)


"""3) Ingresar un número. Mostrar los números desde 0 hasta el número ingresado."""

# ingreso_numero = int(input("Ingrese un numero: "))
# for numero in range(0, ingreso_numero + 1, 1):
#     print(numero)


"""4) Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:
5 x 0 = 0
5 x 1  = 5
5 x 2 = 10
5 x 3  = 15
"""

# ingreso_numero = int(input("Ingrese un numero: "))
# for numero in range(0, ingreso_numero + 1,):
#     resultado = ingreso_numero * numero
#     print(f"{ingreso_numero} * {numero} = {resultado}")


"""5) Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
Mostrar la suma y el promedio de todos los números."""

# suma = 0
# cantidad_numeros = 0

# for numero in range(10):
#     ingreso_numero = int(input("Ingrese un numero: "))

#     if ingreso_numero == 0:
#         break

#     suma += ingreso_numero
#     cantidad_numeros += 1

# if cantidad_numeros > 0:
#     promedio = suma / cantidad_numeros
# else:
#     promedio = 0

# print(f"La suma es: {suma} \n"
#     f"El promedio es: {promedio}")


"""6) Imprimir los números múltiplos de 3 entre el 1 y el 10."""

# for i in range(1, 11):
#     if i % 3 == 0:
#         print(i)


"""7) Mostrar los números pares que hay desde la unidad hasta el número 50."""

# for i in range(51):
#     if i % 2 == 0:
#         print(i)


"""8) Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa 
el numero 5, la salida del programa será la siguiente:
1
12
123
1234
12345
"""

# ingreso_numero = int(input("Ingrese un numero: "))

# for i in range(1, ingreso_numero + 1):
#     for j in range(1, i + 1):
#         print(j, end = "")
#     print()

                                                            # DUDAS CON ESTE


"""9) Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado.
Mostrar la cantidad de divisores encontrados."""

# cant_divisores = 0
# ingreso_numero = int(input("Ingrese un numero: "))

# for i in range(1 , ingreso_numero + 1):

#     if ingreso_numero % i == 0:
#         print(i)
#         cant_divisores += 1

# print(f"La cantidad de divisores es: {cant_divisores}")


"""10) Ingresar un número. Determinar si el número es primo o no."""

# cant_divisores = 0
# ingreso_numero = int(input("Ingrese un numero: "))

# for i in range(1, ingreso_numero + 1):

#     if ingreso_numero % i == 0:
#         cant_divisores += 1

# if cant_divisores == 2:
#     print(f"{ingreso_numero} ES PRIMO")
# else:
#     print(f"{ingreso_numero} NO ES PRIMO")


"""11) Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado.
Informar cuántos números primos se encontraron."""

contador_primos = 0
numero_usuario = int(input("Ingrese un numero: "))

for posible_primo in range(1, numero_usuario + 1, 1):

    cant_divisores = 0

    for posible_divisor in range(1, posible_primo + 1, 1):

        if posible_primo % posible_divisor == 0:
            cant_divisores += 1
    
            if cant_divisores > 2:
                break # ESTO AGREGADO ULTIMAMENTE VER SI FUNCIONA

    if cant_divisores == 2:
        print(f"{posible_primo} ES PRIMO")
        contador_primos += 1
print(f"Se encontraron {contador_primos} numeros primos")
