def calcular_fibonacci(numero: int) -> int:
    if numero == 0 or numero == 1:
        return numero
    else:
        ultimo = numero - 1
        penultimo = ultimo - 1
        return calcular_fibonacci(ultimo) + calcular_fibonacci(penultimo)

numero = 3
numero_fibonacci = calcular_fibonacci(numero)

print(f"El {numero}° numero de la sucesion fibonacci es: {numero_fibonacci}")
