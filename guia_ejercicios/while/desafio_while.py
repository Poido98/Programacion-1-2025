"""Desafío: Encuesta Tecnológica en UTN Technologies
UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su 
próximo desarrollo en Python, con el objetivo de revolucionar el mercado.
Las tecnologías en evaluación son:
Inteligencia Artificial (IA)
Realidad Virtual/Aumentada (RV/RA)
Internet de las Cosas (IOT)

Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el 
propósito de analizar ciertas métricas.
🔹 Recolección de Datos
Cada empleado encuestado deberá proporcionar la siguiente información:
    Nombre
    Edad (debe ser 18 años o más)
    Género (Masculino, Femenino, Otro)
    Tecnología elegida (IA, RV/RA, IOT)

El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
🔹 Análisis de Datos
A partir de las respuestas, se deben calcular las siguientes métricas:
1) Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
2) Porcentaje de empleados que NO votaron por IA, siempre y cuando:
    Su género no sea Femenino 
    Su edad está entre los 33 y 40 años.
3) Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.

🔹 Requisitos del Programa
Los datos deben solicitarse y validarse correctamente.
Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
Presentar los resultados de manera clara y organizada.
"""

encuestados = 0
metrica_uno = 0
metrica_dos = 0
nombre_empleado_mayor_edad = None
edad_empleado_mayor = 0
tecnologia_mayor_edad = None



while encuestados < 2:

    nombre = input("Ingrese su nombre: ")
    while not nombre.isalpha():
        nombre = input("Nombre incorrecto, ingrese un numbre correcto: ")
    
    edad = int(input("Edad (18 o +): "))
    while edad < 18:
        edad = int(input("Edad incorrecta, ingrese una edad valida (18 o +): "))

    genero = input("Genero (masculino, femenino, otro): ")
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input("Genero incorrecto, seleccione un genero valido (masculino, femenino, otro): ")

    tecnologia = input("Seleccione una tecnologia (IA, RV/RA, IOT): ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("Error, seleccione una tecnologia valida (IA, RV/RA, IOT): ")

    if (genero == "masculino") and (edad > 24 and edad < 51) and (tecnologia == "IA" or tecnologia == "IOT"):
        metrica_uno += 1
    
    if (tecnologia != "IA") and (genero != "femenino") and (edad > 32 and edad < 40):
        metrica_dos += 1
    
    if nombre_empleado_mayor_edad == None or edad > edad_empleado_mayor:
        nombre_empleado_mayor_edad = nombre
        edad_empleado_mayor = edad
        tecnologia_mayor_edad = tecnologia
    
    encuestados += 1
    
porcentaje_metrica_dos = (metrica_dos / encuestados) * 100

print(f"Hay {metrica_uno} empleados masculinos que votaron por IOT o IA y tiene entre 25 y 50 años")
print(f"El porcentaje de empleados masculinos que no votaron por IA y tienen entre 33 y 40 años es de {metrica_dos}%")
print(f"El empleado masculino de mayor edad es {nombre_empleado_mayor_edad} con {edad_empleado_mayor} años\
 y votó por {tecnologia_mayor_edad}")