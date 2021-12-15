import string
from collections import defaultdict
import copy

with open("./input14.txt") as fin:
    lecturaDatos = fin.read().strip().split("\n")

copia = lecturaDatos[0]
reglas = [line.split(" -> ") for line in lecturaDatos[2:]]

# Modify the copia
frecuencias = defaultdict(int)
for i in range(len(copia) - 1):
    frecuencias[copia[i:i + 2]] += 1

elementos = string.ascii_uppercase


def replace(frecuencias):
    nuevas_frecuencias = copy.copy(frecuencias)
    for pares in frecuencias:
        for start, end in reglas:
            if pares == start:
                occs = frecuencias[pares]
                nuevas_frecuencias[pares] -= occs
                nuevas_frecuencias[pares[0] + end] += occs
                nuevas_frecuencias[end + pares[1]] += occs
                break

    return nuevas_frecuencias


for i in range(40):
    frecuencias = replace(frecuencias)

# conteo each element
conteo = defaultdict(int)
for pares in frecuencias:
    conteo[pares[0]] += frecuencias[pares]
    conteo[pares[1]] += frecuencias[pares]

conteo[copia[0]] += 1
conteo[copia[-1]] += 1

conteo_vals = [c[1] // 2 for c in conteo.items()]

resp = max(conteo_vals) - min(conteo_vals)
print(resp)