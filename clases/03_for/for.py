# for i in range(3, -10, -1):
#     print(i)


#FOR ANIDADO
# for i in range(3):
#     for j in range(2):
#         print(f"i vale {i} y j vale {j}")


# suma = 0
# for inicial in range(2):
#     print(f"VUELTA FOR 1: {inicial + 1}")
#     for jota in range(3):
#         print(f"FOR 2: {jota + 1}")


numero_usuario = None
while numero_usuario == None or (not numero_usuario.isdigit()):
    numero_usuario = input("Ingrese un numero: ")

numero_usuario_int = int(numero_usuario)

cantidad_divisores = 0

for posible_divisor in range(1, numero_usuario_int + 1, 1):
    if numero_usuario_int % posible_divisor == 0:
        cantidad_divisores += 1
        print(f"El {posible_divisor} es divisor de {numero_usuario_int}")
    
if cantidad_divisores == 2:
    print(f"El {numero_usuario_int} es PRIMO")

else:
    print(f"El {numero_usuario_int} NO es PRIMO")