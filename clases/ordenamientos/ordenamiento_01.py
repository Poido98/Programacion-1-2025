# lista numeros
# [4,8,3,1,0] # DESCENDENTE


def ordenar_bubble_sort(mi_lista: list) -> list:
    
    largo_lista = len(mi_lista)
    for indice in range(largo_lista - 1):

        for sub_indice in range(indice + 1, largo_lista):

            if mi_lista[indice] < mi_lista[sub_indice]:
                auxiliar = mi_lista[indice]
                mi_lista[indice] = mi_lista[sub_indice]
                mi_lista[sub_indice] = auxiliar
    return mi_lista

# ======================================
import random

cantidad = 10000
mi_lista_test = list(range(cantidad))
print(f"Lista original: {mi_lista_test}")

random.shuffle(mi_lista_test)
print(f"Lista desordenada: {mi_lista_test}")

nueva_lista = ordenar_bubble_sort(mi_lista_test)
print(f"Lista ordenada: {nueva_lista}")