"""1) Mostrar 10 repeticiones de números ascendentes desde el 1 al 10."""

# contador = 0

# while contador < 10:
#     contador += 1
#     print(contador)


"""2) Mostrar 10 repeticiones de números descendentes desde el 10 al 1."""

# contador = 10

# while contador > 0:
#     print(contador)
#     contador -= 1


"""3) Mostrar la suma de los números desde el 1 hasta el 10."""

# contador = 0
# suma = 0

# while contador < 10:
#     contador += 1
#     suma += contador
#     print(contador)

# print(suma)


"""4) Mostrar la suma de los números pares desde el 1 hasta el 10."""

# contador = 0
# suma = 0

# while contador < 10:
#     contador += 1
#     print(contador)
    
#     if contador % 2 == 0:
#         suma += contador

# print(f"La suma de los numeros pares es: {suma}")


"""5) Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
Mostrar la suma y el promedio por pantalla."""

# contador = 0
# suma = 0

# while contador < 5:
#     ingreso_numero = int(input("Ingrese un numero: "))
#     suma += ingreso_numero
#     contador += 1

# promedio = suma / contador

# print(suma)
# print(promedio)


"""6) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma
de los números ingresados y el promedio de los mismos."""

# contador = 0
# suma = 0

# while True:
#     ingreso_numero = int(input("Ingrese un numero: "))
#     suma += ingreso_numero
#     contador += 1 
#     pregunta = input("Desea seguir ingresando numeros (s o n): ")

#     if pregunta == "n":
#         break

# promedio = suma / contador

# print(suma)
# print(promedio)


"""7) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
Calcular la suma de los números positivos y el producto de los negativos."""

# positivos = 0
# negativos = 1

# while True:
#     ingreso_numero = int(input("Ingrese un numero: "))
    
#     if ingreso_numero < 0:
#         negativos *= ingreso_numero
    
#     elif ingreso_numero > 0:
#         positivos += ingreso_numero
    
#     pregunta = input("Desea seguir ingresando numeros (s o n): ")

#     if pregunta == "n":
#         break

# print(f"La suma de numeros positivos es: {positivos}")
# print(f"El producto de los numeros negativos es: {negativos}")


"""8) Ingresar 10 números enteros. Determinar el máximo y el mínimo."""

# nro_maximo = None
# nro_minimo = None
# contador = 0

# while contador < 4:
#     numero = int(input("Ingrese un numero: "))
#     contador += 1

#     if (nro_minimo == None) or (numero < nro_minimo):
#         nro_minimo = numero
#     elif (nro_maximo == None) or (numero > nro_maximo):
#         nro_maximo = numero
    
# print(f"El numero minimo es: {nro_minimo}, y el numero maximo es: {nro_maximo}")

"""9) Solicitar al usuario que ingrese 5 números. Calcular la suma de los
números ingresados y el promedio de los mismos."""

# suma = 0
# contador = 0

# while contador < 5:
#     ingreso_numero = int(input("Ingrese un numero: "))
#     suma += ingreso_numero
#     contador += 1

# promedio = suma / contador

# print(f"La suma de los numeros es: {suma}")
# print(f"El promedio es: {promedio}")


"""10) Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma
de los números ingresados y el promedio de los mismos."""

# suma = 0
# contador = 0

# while contador < 10:
#     ingreso_numero = int(input("Ingrese un numero: "))
#     contador += 1
#     suma += ingreso_numero

#     if contador >= 5:
#         continuar = input("Desea seguir ingresando (s o n): ")

#         if continuar == "n":
#             break

# promedio = suma / contador

# print(f"La suma de los numeros es: {suma}")
# print(f"El promedio es: {promedio}")


"""11) Realizar un programa que permita que el usuario ingrese todos los números que desee. 
Una vez finalizada la carga determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos."""

contador_negativos = 0
contador_positivos = 0
mayor_nro_positivo = None
contador_total = 0
suma_negativos = 0
suma_positivos = 0

while True:
    ingreso_numero = int(input("Ingrese un numero: "))

    if ingreso_numero < 0:
        suma_negativos += ingreso_numero
        contador_negativos += 1
    
    elif ingreso_numero > 0:
        suma_positivos += ingreso_numero
        contador_positivos += 1

        if mayor_nro_positivo == None or ingreso_numero > mayor_nro_positivo:
            mayor_nro_positivo = ingreso_numero

    contador_total += 1

    pregunta = input("Desea seguir ingresando (s o n): ")
    if pregunta == "n":
        break

promedio_positivos = suma_positivos / contador_positivos
porcentaje_negativos = (contador_negativos / contador_total) * 100


print(f"La suma de los negativos es: {suma_negativos}")
print(f"La suma de los positivos es: {suma_positivos}")
print(f"La cantidad de nros negativos es de: {contador_negativos} numeros")
print(f"El promedio de los nros positivos es: {promedio_positivos}")
print(f"El mayor numero positivo es: {mayor_nro_positivo}")
print(f"El porcentaje de los nros negativos respecto del total de ingresos es: {porcentaje_negativos}")

