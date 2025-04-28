from funciones_juego import (
    obtener_eleccion_usuario, obtener_eleccion_maquina,
    verificar_estado_partida, mostrar_elemento,
    verificar_ganador_ronda, verificar_ganador_partida
)

def jugar_piedra_papel_tijera() -> str:

    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 0

    print("¡¡¡Bienvenidos a Piedra, Papel o Tijera!!!")

    while verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
        print(f"Ronda {ronda_actual + 1}")

        jugador = obtener_eleccion_usuario()
        maquina = obtener_eleccion_maquina()

        print(f"Jugador eligió: {mostrar_elemento(jugador)}")
        print(f"Maquina eligió: {mostrar_elemento(maquina)}")

        resultado_ronda = verificar_ganador_ronda(jugador, maquina)
        if resultado_ronda == "Jugador":
            aciertos_jugador += 1
        elif resultado_ronda == "Maquina":
            aciertos_maquina += 1
        
        print(f"Ganador de la ronda: {resultado_ronda}")
        ronda_actual += 1

    ganador = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    print(f"Terminó la partida, ganador: {ganador}")
    return ganador