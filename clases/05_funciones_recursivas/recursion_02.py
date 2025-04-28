def validar_edad_recursiva(edad_min: int, edad_max: int) -> int:
    edad_str = input(f"Ingrese su edad [{edad_min}-{edad_max}]: ")

    if not edad_str.isdigit() or not (edad_min <= int(edad_str) <= edad_max):
        print(f"Error, la edad {edad_str} es invalida.")
        edad_str = validar_edad_recursiva(edad_min, edad_max)

        if type(edad_str) == int:
            return edad_str
        else: 
            edad_int = int(edad_str)
        return edad_int
        
validar_edad_recursiva(18, 90)