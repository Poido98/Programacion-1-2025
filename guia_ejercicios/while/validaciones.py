"""1) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto.
Tendrá intentos indeterminados."""

# clave = "utn"
# ingreso = input("Ingrese una clave: ")

# while ingreso != "utn":
#     ingreso = input("La clave es incorrecta, vuelva a intentarlo: ")

# print("Usted ha ingresado correctamente!!!")


"""2) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos. """

# clave = "1234"
# intentos = 0

# while intentos < 3:
#     ingreso = input("Ingrese la clave: ")

#     if ingreso == clave:
#         print("Usted ha ingresado correctamente")
#         break

#     else:
#         intentos += 1

#         if intentos < 3:
#             print("Clave incorrecta, vuelva a intentarlo")
#         else:
#             print("Error, su clave ha caducado contacte a soporte")


"""3) Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive."""

# while True:
#     ingreso_nota = int(input("Ingrese la nota del alumno (1-10): "))

#     while ingreso_nota < 1 or ingreso_nota > 10:
#         ingreso_nota = int(input("Nota fuera de rango (1-10): "))
    
#     print("Nota ingresada")
#     pregunta = input("Desea seguir ingresando (s o n): ")

#     while pregunta != "s" and pregunta != "n":
#         pregunta = input("Respuesta incorrecta, elija la opcion correspondiente (s o n): ")

#     if pregunta == "n":
#         break


"""4) Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul."""

# ingreso = input("Ingrese un color (rojo, verde, azul): ")

# while ingreso != "rojo" and ingreso != "verde" and ingreso != "azul":
#     ingreso = input("Color equivocado, vuelva a ingresar el color (rojo, verde, azul): ")

# print("El color ingresado es correcto")


"""5) Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.
"""

# while True:
#     apellido = input("Ingrese su apellido: ")
#     while not apellido.isalpha():
#         apellido = input("Ingrese un apellido valido: ")

#     edad = int(input("Ingrese su edad (18-90): "))
#     while edad < 18 or edad > 90:
#         edad = int(input("Edad incorrecta, vuelva a ingresar su edad (18-90): "))
    
#     estado_civil = input("Estado civil (“soltero/a”, ”casado/a”, “divorciado/a” o “viudo/a”): ")
#     while (estado_civil != "soltero" and estado_civil != "soltera") and \
#         (estado_civil != "casado" and estado_civil != "casada") and \
#         (estado_civil != "divorciado" and estado_civil != "divorciada") and \
#         (estado_civil != "viudo" and estado_civil != "viuda"):
#         estado_civil = input("Estado civil incorrecto, coloque nuevamente (“soltero/a”, ”casado/a”, “divorciado/a” o “viudo/a”): ")
    
#     legajo = int(input("N° de legajo (4 cifras, sin 0 a la izquierda): "))
#     while legajo < 1000 or legajo > 9999:
#         legajo = int(input("Error, ingrese nuevamente su legajo (4 cifras, sin 0 a la izquierda): "))

#     break
    
# print(f"Apellido: {apellido}")
# print(f"Edad: {edad}")
# print(f"Estado civil: {estado_civil}")
# print(f"N° de legajo: {legajo}")
