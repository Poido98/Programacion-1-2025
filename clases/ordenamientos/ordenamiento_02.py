

# DESCENDENTE
def ordenar_selection_sort(mi_lista: list) -> list:

    largo_lista = len(mi_lista)
    for indice in range(largo_lista - 1):
        indice_de_elemento_mayor = indice

        for sub_indice in range(indice + 1, largo_lista):

            if mi_lista[indice_de_elemento_mayor] < mi_lista[sub_indice]:
                indice_de_elemento_mayor = sub_indice
        
        if indice_de_elemento_mayor != indice:
            auxiliar = mi_lista[indice_de_elemento_mayor]
            mi_lista[indice_de_elemento_mayor] = mi_lista[indice]
            mi_lista[indice] = auxiliar
    
    return mi_lista



import random
cantidad = 100
mi_lista_test = list(range(cantidad))
print(f"Lista original: {mi_lista_test}")

random.shuffle(mi_lista_test)
print(f"Lista desordenada: {mi_lista_test}")

nueva_lista = ordenar_selection_sort(mi_lista_test)
print(f"Lista ordenada: {nueva_lista}")