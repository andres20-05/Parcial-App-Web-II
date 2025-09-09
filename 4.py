#Ejercicio 4
#Implemente un programa que use try–except para:
#1. Pedir al usuario dos números enteros.
#2. Calcular la división entre ellos.
#3. Si el usuario ingresa un valor no numérico → mostrar "Error: Debe ingresar números enteros".
#4. Si intenta dividir entre cero → mostrar "Error: No se puede dividir entre cero".
#(Debe hacerse con al menos dos bloques except diferentes).

try:
    num1 = int(input("Ingrese el primer numero entero: "))
    num2 = int(input("Ingrese el segundo numero entero: ")) 
    resultado = num1/num2
    print (f"El resultado de la division es: {resultado}")

except ValueError:
    print("Error: Ingrese primero los numeros")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

