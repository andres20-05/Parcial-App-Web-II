#Ejercicio 5
#Sistema de gestión de estudiantes (mini-proyecto parcial). Cree un programa que:
#1. Permita ingresar estudiantes con su nombre y nota (usando ciclo while, hasta que el usuario escriba "fin").
#2. Guarde los datos en una lista de diccionarios. Ejemplo: [{"nombre": "Ana", "nota": 4.5}, {"nombre": "Luis", "nota": 3.2}]
#3. Defina funciones para:
#○ promedio_notas(estudiantes) → retorna el promedio.
#○ mejor_estudiante(estudiantes) → retorna el nombre y nota del mejor.
#○ peor_estudiante(estudiantes) → retorna el nombre y nota del peor.
#4. Imprima un reporte final: número de estudiantes, promedio, mejor y peor estudiante.
#Extra (5% bonus): ordenar los estudiantes de menor a mayor nota y mostrarlos en pantalla.

def promedio_notas(estudiantes):
    return sum(e["nota"] for e in estudiantes) / len(estudiantes)

def mejor_estudiante(estudiantes):
    return max(estudiantes, key=lambda e: e["nota"])

def peor_estudiante(estudiantes):
    return min(estudiantes, key=lambda e: e["nota"])

estudiantes = []

while True:
    nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes.append({"nombre": nombre, "nota": nota})

if estudiantes:
    print("\n Reporte Final")
    print(f"Número de estudiantes: {len(estudiantes)}")
    print(f"Promedio de notas: {promedio_notas(estudiantes):.2f}")

    mejor = mejor_estudiante(estudiantes)
    peor = peor_estudiante(estudiantes)
    print(f"Mejor estudiante: {mejor['nombre']} con nota {mejor['nota']}")
    print(f"Peor estudiante: {peor['nombre']} con nota {peor['nota']}")

    # Ordenar de menor a mayor
    print("\nEstudiantes ordenados por nota (menor a mayor):")
    for est in sorted(estudiantes, key=lambda e: e["nota"]):
        print(f"{est['nombre']} - {est['nota']}")
else:
    print("No se ingresaron estudiantes.")
