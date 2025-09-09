#Ejercicio 2
#Defina una función con parámetros por omisión llamada calcular_descuento(precio, descuento=10) que:
#● Reciba el precio de un producto y un descuento (por defecto 10%).
#● Retorne el precio final después del descuento.
#● El programa debe pedir al usuario al menos 3 precios de productos y mostrar el valor total a pagar.


def calcular_descuento(precio, descuento=10):
    return precio - (precio * descuento / 100)

total = 0
for i in range (3):
    precio = float(input(f"Ingrese el precio del producto {i+1}: "))
    precio_final = calcular_descuento(precio) # Se usa por defecto el descuento del 10%
    print(f"Precio con descuento: {precio_final}")
    total += precio_final

print(f"Total a pagar por los 3 productos: {total}")