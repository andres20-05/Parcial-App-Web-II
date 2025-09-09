#Ejercicio 3
#Cree una función llamada analizar_texto(*args, **kwargs) que:
#● Reciba múltiples cadenas de texto (usando *args).
#● Reciba parámetros opcionales (kwargs) como:
#○ contar_vocales=True/False
#○ contar_palabras=True/False
#● Según las opciones enviadas, imprima la cantidad total de vocales o palabras.
#Ejemplo:
#analizar_texto("Hola mundo", "Python es genial", contar_vocales=True)

def analizar_texto (*args, **kwargs):
    texto_unido = " ".join(args)
    if kwargs.get("contar_vocales", False):
        vocales = "aeiouAEIOU"
        cantidad_vocales = sum(1 for c in texto_unido if c in vocales)
        print (f"Cantidad total de vocales: {cantidad_vocales}")
    if kwargs.get("contar_palabras", False):
        cantidad_palabras = len(texto_unido.split())
        print (f"Cantidad total de palabras: {cantidad_palabras}")

#Ejemplo
analizar_texto("Hola mundo", "Python es genial", contar_vocales=True, contar_palabras=True)


