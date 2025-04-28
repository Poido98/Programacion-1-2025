"""Facturación del Servicio de Agua Potable
El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar 
un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes 
tarifas y ajustes según el consumo y el tipo de cliente.
Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro 
cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. 
En algunos casos especiales, también pueden otorgarse descuentos adicionales.
A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el 
monto final a pagar.

-Tarifa base:
#Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
#El costo por metro cúbico (m³) de agua es de $200/m³.

Bonificaciones y Recargos según tipo de cliente:
-Cliente Residencial:
#Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
#Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

-Cliente Comercial:
#Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
#Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
#Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

-Cliente Industrial:
#Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
#Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
#Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

-Casos especiales:
#Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, 
se aplica un descuento adicional del 5%.
#En todos los casos, se aplica el IVA del 21% sobre el total.

Requerimientos del programa:
Solicitar al usuario:
1) Cantidad de metros consumidos
2) Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
Calcular:
3) Subtotal de consumo.
4) Bonificaciones, si corresponde
5) Recargos, si corresponde
6) Subtotal, con recargos y bonificaciones.
7) IVA aplicado (21%), si corresponde.
8) Total final a pagar.
9) Mostrar en pantalla el desglose de los cálculos.
"""

print("Hola buenos dias, le damos la bienvenida al portal de facturacion del servicio de agua potable Gotita S.A.")

tipo_cliente = input("Ingrese el tipo de cliente (residencial-comercial-industrial): ")
agua_consumida = float(input("Ingrese la cantidad de m3 consumidos: "))
tarifa_base = 7000
costo_metro_cubico = 200
costo_total = (agua_consumida * costo_metro_cubico) + tarifa_base

print(f"Tipo de cliente: {tipo_cliente}")
match tipo_cliente:

    case "residencial":
        if costo_total < 35000:
            print(f" A {costo_total} se le aplica un descuento del 5%")
            costo_total *= 0.95
            print(f"Nuevo costo con el descuento del 5% aplicado: {costo_total}")
        if agua_consumida < 30:
            print(f" A {costo_total} se le aplica un descuento del 5% adicional")
            costo_total *= 0.90
            print(f"Nuevo costo con el descuento de 10% aplicado: {costo_total}")
        elif agua_consumida > 80:
            print(f" A {costo_total} se le aplica un recargo del 15%")
            costo_total *= 1.15
            print(f"Nuevo costo con un recargo del 15% aplicado: {costo_total}")
    case "comercial":
        if agua_consumida > 150:
            print(f" A {costo_total} se le aplica un descuento del 8%")
            costo_total *= 0.92
            print(f"Nuevo costo con el descuento del 8% aplicado: {costo_total}")
        elif agua_consumida > 300:
            print(f" A {costo_total} se le aplica un descuento del 12%")
            costo_total *= 0.88
            print(f"Nuevo costo con el descuento del 12% aplicado: {costo_total}")
        elif agua_consumida < 50:
            print(f" A {costo_total} se le aplica un recargo del 5%")
            costo_total *= 1.05
            print(f"Nuevo costo con un recargo del 5% aplicado: {costo_total}")
    case "industrial":
        if agua_consumida > 500:
            print(f" A {costo_total} se le aplica un descuento del 20%")
            costo_total *= 0.80
            print(f"Nuevo costo con el descuento del 20% aplicado: {costo_total}")
        elif agua_consumida > 1000:
            print(f" A {costo_total} se le aplica un descuento del 30%")
            costo_total *= 0.70
            print(f"Nuevo costo con el descuento del 30% aplicado: {costo_total}")
        elif agua_consumida < 200:
            print(f" A {costo_total} se le aplica un recargo del 10%")
            costo_total *= 1.10
            print(f"Nuevo costo con un recargo del 10% aplicado: {costo_total}")

costo_total += tarifa_base
iva = costo_total * 21 / 100
costo_total_con_iva = costo_total + iva


print(f"El subtotal de consumo es: {costo_total}")
print(f"El costo final + 21% del IVA es: {costo_total_con_iva}")