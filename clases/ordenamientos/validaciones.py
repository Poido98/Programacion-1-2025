def validar_numero(num_min: int, num_max: int):
    """
        Recibe una edad en formato string, valida que esté formada por numeros y que
        numericamente sea mayor o igual a 18. En caso de cumplir, retorna la edad 
        parseada a entero.
    """
    while not edad.isdigit() or (int(edad) < 18):
        edad = input(f"Ingrese la edad del cliente [solo mayores de 18 años]: ")
    edad_int = int(edad)
    return edad_int