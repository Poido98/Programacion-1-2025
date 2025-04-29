def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    """
        Funcion para pedir un numero entero por consola
    Args:
        mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola
        mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido
        minimo: valor mínimo admitido (inclusive)
        maximo: valor máximo admitido (inclusive)
        reintentos: cantidad de veces que se volverá a pedir el dato en caso de error

    Returns:
        Retorna None en caso de no ingresar un numero valido
    """
    intentos = 0

    while intentos < reintentos:
        entrada = input(mensaje)
        if entrada.isdigit():
            
            numero = int(entrada)
            if minimo <= numero <= maximo:
                print("Numero validado correctamente.")
                return numero
            
            print(f"Intento: {intentos + 1}")
            intentos += 1
            print(mensaje_error)
        
    print("Error de validacion, reintente mas tarde")
    return None


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:
    """
        Funcion para pedir un numero flotante por consola
    Args:
        mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola
        mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido
        minimo: valor mínimo admitido (inclusive)
        maximo: valor máximo admitido (inclusive)
        reintentos: cantidad de veces que se volverá a pedir el dato en caso de error

    Returns:
        Retorna None en caso de no ingresar un numero valido
    """
    intentos = 0

    while intentos < reintentos:
        entrada = input(mensaje)
        if entrada.count(".") <= 1 and entrada.replace(".", "", 1).isdigit():
            
            numero = float(entrada)
            if minimo <= numero <= maximo:
                print(f"El numero {numero} ha sido validado correctamente")
                return numero
            
            print(f"Intento: {intentos + 1}")
            intentos += 1
            print(mensaje_error)
        
    print("Error de validacion, reintente mas tarde")
    return None


def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str|None:
    
    intentos = 0

    while intentos < reintentos:
        entrada = input(mensaje)
        if len(entrada) < longitud:
            
            print(f"Intento: {intentos + 1}")
            intentos += 1
            print(mensaje_error)

        else:
            texto_validado = entrada
            print(f"El texto {texto_validado} ha sido validado correctamente")
            return texto_validado
            
        
    print("Error de validacion, reintente mas tarde")
    return None