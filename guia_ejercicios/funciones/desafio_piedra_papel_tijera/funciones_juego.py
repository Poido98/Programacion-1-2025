import random


def obtener_eleccion_usuario() -> None:
    """
    Obtiene la eleccion del jugador para que elija entre Piedra, Papel o Tijera

    Returns:
        Retorna lo que eligió el usuario
    """
    eleccion = int(input("Elija (1: Piedra, 2: Papel o 3: Tijera): "))
    while (eleccion != 1) and (eleccion != 2) and (eleccion != 3):
        eleccion = int(input("Error, ingrese nuevamente (1: Piedra, 2: Papel y 3: Tijera): "))
    return eleccion

def obtener_eleccion_maquina() -> None:
    """
        Usando la funcion random, hace que la maquina elija entre 1 de las 3 opciones

    Returns:
        Retorna lo que eligió la maquina
    """
    return random.randint(1, 3)

# DUDA SI SE PODRIA HACER UNA FUNCION SOLA PARA QUE OBTENGA LA ELECCION EL USUARIO Y LA MAQUINA


def verificar_ganador_ronda(jugador, maquina) -> str:
    """
        Determina quien gano la ronda entre el jugador y la maquina
    Args:
        jugador (int): elección del jugador (1 para Piedra, 2 para Papel o 3 para Tijera)
        maquina (int): elección de la maquina (1 para Piedra, 2 para Papel o 3 para Tijera)

    Returns:
        Retorna si en esa ronda gana el jugador, gana la maquina o hay empate
    """

    if jugador == maquina:
        return "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        return "Jugador"
    else:
        return "Maquina"


def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) -> bool:
    """
    Determina si la partida sigue o terminó

    Args:
        aciertos_jugador (int): numero de rondas ganadas por el jugador
        aciertos_maquina (int): numero de rondas ganadas por la maquina
        ronda_actual (int): numero de ronda actual

    Returns:
        Retorna True si la partida sigue, False si alguien ganó dos veces seguidas o se jugaron las 3 rondas
    """

    if aciertos_jugador >= 2 or aciertos_maquina >= 2:
        return False
    
    if ronda_actual >= 3:
        return False

    return True


def verificar_ganador_partida(aciertos_jugador, aciertos_maquina) -> str:
    """
        Determina quien ganó la partida según los aciertos finales

    Args:
        aciertos_jugador (int): numero de rondas ganadas por el jugador
        aciertos_maquina (int): numero de rondas ganadas por la maquina

    Returns:
        Retorna si gano el jugador, la máquina o hay empate
    """

    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        return "Maquina"
    else:
        return "Empate"
    

def mostrar_elemento(eleccion) -> str:
    """
        Muestra el elemento que se eligió en formato string

    Args:
        eleccion (int): numero de elección (1 para Piedra, 2 para Papel o 3 para Tijera)

    Returns:
        Retorna según el numero que se eligió Piedra, Papel o Tijera según corresponda
    """

    if eleccion == 1:
        return "Piedra"
    elif eleccion == 2:
        return "Papel"
    elif eleccion == 3:
        return "Tijera"
    else:
        return "Eleccion inválida"
