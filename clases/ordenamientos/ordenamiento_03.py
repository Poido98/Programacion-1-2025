def ordenar_quick_sort(mi_lista : list) -> list:

    if len(mi_lista) < 2:
        return mi_lista
    
    else:
        pivot = mi_lista.pop()
        mas_chicos = []
        mas_grandes = []

        for numero in mi_lista:

            if numero <= pivot:
                mas_chicos.append(numero)
            
            else:
                mas_grandes.append(numero)
        
    return ordenar_quick_sort(mas_grandes) + [pivot] + ordenar_quick_sort(mas_chicos)

import random

cantidad = 150
mi_lista_test = list(range(cantidad))
# print(f"Lista original: {mi_lista_test}")

# random.shuffle(mi_lista_test)
# print(f"Lista desordenada: {mi_lista_test}")

nueva_lista = ordenar_quick_sort(mi_lista_test)
print(f"Lista ordenada: {nueva_lista}")
