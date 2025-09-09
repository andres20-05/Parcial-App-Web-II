#Ejercicio 1
#Cree un programa que pida al usuario un número entero positivo y:
#● Imprima todos los números primos menores o iguales a ese número.
#● Al final, indique cuántos primos se encontraron. 
# (Debe usarse ciclo for o while, no librerías externas)


def es_primo(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un numero entero positivo: "))
contador = 0

print (f"Numero primos menores o iguales a {numero}:")
for i in range (2, numero + 1):
    if es_primo(i):
        print(i, end=" ")
        contador += 1

print(f"\nCantidad total de primos encontrados: {contador}")
