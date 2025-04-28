encuestas = 0
contador_a = 0
contador_b = 0
contador_invalido = 0

while encuestas < 6:
    respuesta = input("Que producto prefiere (a o b)?: ")
    match respuesta:
        case "a":
            contador_a += 1
        case "b":
            contador_b += 1
        case _:
            contador_invalido = contador_invalido + 1
            print("Respuesta no valida")
    encuestas += 1

porcentaje_a = (contador_a * 100) / encuestas
porcentaje_b = (contador_b * 100) / encuestas

print(f"Porcentaje de personas que elijen el producto A: {porcentaje_a}")
print(f"Porcentaje de personas que elijen el producto B: {porcentaje_b}")
print(f"Porcentaje de personas que elijen una respuesta incorrecta: {contador_invalido}")