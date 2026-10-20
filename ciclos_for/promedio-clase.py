"""

Ejemplo:
un profesor necesita crear un programa que le ayude a calcular el
promedio de notas de un salon de clases.
El ingresa el nombre y el valor de nota final de cada estudiante.
Al final necesita saber cual es el mejor estudiante y el promedio de
todo el curso.
Cada nota es de 0 a 5.0.
"""

cantidad_est = int(input("Cantidad de estudiantes"))

mejor_est = ""
nota_mayor = 0.0
suma = 0.0
promedio = 0.0

for veces in range(1, cantidad_est+1):
    nombre = input("ingrese nombre del estudiante " )
    nota = float(input("ingrese nota del estudiante "))

    suma = suma + nota 

    if nota > nota_mayor:
        nota_mayor = nota
        mejor_est = nombre


promedio = suma / cantidad_est

print(" rl promedio del curso es: ", promedio,
      "\nEl mejor estudiante es ", mejor_est,
      "\ncon la nota ", nota_mayor)