lista_nombres = [
    "Pepe", "Fatiga", "Moni", "Mario Bross", "El Luigi"
]

# indice = 4
# while indice >= 0:
#     print(lista_nombres[indice])
#     indice -= 1


# largo_de_lista = len(lista_nombres)
for indice in range(len(lista_nombres)):

    texto = \
        f"Valor actual del indice: {lista_nombres[indice]}"
    print(texto)


for nombre in lista_nombres:
    print(nombre)
