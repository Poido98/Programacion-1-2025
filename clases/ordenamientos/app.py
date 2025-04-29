from validaciones import validar_numero
from output import mostrar_menu
from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios
)




def aplicacion(lista_marcas, lista_modelos, lista_precios, lista_cantidades, lista_ganancias):

    corriendo = True

    while corriendo:

        mostrar_menu()
