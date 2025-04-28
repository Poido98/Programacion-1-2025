# """1) A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
# el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot
# """

# altura = float(input("Ingrese la altura del jugador: "))

# if altura < 160:
#     print("El jugador es base")
# elif altura >= 160 and altura <= 179:
#     print("El jugador es escolta")
# elif altura >=180 and altura <= 199:
#     print("El jugador es alero")
# else:
#     print("EL jugador es pivot")

"""2) Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
4 y 5 ---> Aprobado, la nota es ...
1, 2 y 3 ---> Desaprobado, la nota es ...
"""

nota_alumno = int(input("Ingrese la nota del alumno: "))

if nota_alumno >= 6 and nota_alumno <= 10:
    print(f"El alumno promociona, la nota es: {nota_alumno}")
elif nota_alumno >= 4 and nota_alumno <= 5:
    print(f"El alumno aprueba, la nota es: {nota_alumno}")
else:
    print(f"El alumno desaprueba, la nota es: {nota_alumno}")