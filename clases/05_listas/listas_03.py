mi_lista = ["Zero", "Uno", 2, 3, 4, "Cinco", "Zeis", "Goku", "008", "Nueve", 10]

print(mi_lista)

for indice in range(10):
    texto = \
        f"""
        Indice actual: {indice}
        Valor actual del indice: {mi_lista[indice]}
        """
    print(texto)

    mi_lista[indice] = 1

print(mi_lista)