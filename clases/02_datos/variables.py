"""
Necesito tomar el nombre y la edad de una persona y poder saber si la persona esta en edad de cobrar la jubilacion

En caso de estar en esa edad, cobrara un premio de $2000000
Caso contrario cobrara $500000
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su genero: ")

premio = 2000000

if genero == "m" and edad >= 65:
    pass
elif edad >= 60 and genero == "f":
    pass
else:
    premio = 500000



if genero == "m" and edad < 65 or genero == "f" and edad < 60:
    premio = 500000


texto = f"Su nombre es {nombre}, tu genero es {genero} y tu edad es {edad}. "
texto += f"Te corresponde el premio de {premio}"

print(texto)