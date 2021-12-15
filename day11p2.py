import numpy as np
from itertools import product

with open("./input11.txt") as fin:
    lecturaDatos = fin.read().strip()
datos = np.array([[int(x) for x in list(i)]
                for i in lecturaDatos.split("\n")], dtype=int)

resp = 0

N = len(datos)

octos = datos

pasos = 1

while True:
    flashed = np.zeros((N, N), dtype=bool)

    for i, j in product(range(N), repeticiones=2):
        octos[i, j] += 1

    while True:
        continuacion = False

        # Make octos flash!
        cambio = np.zeros((N, N), dtype=int)

        for i, j in product(range(N), repeticiones=2):
            if not flashed[i, j] and octos[i, j] > 9:

                resp += 1
                flashed[i, j] = True
                continuacion = True

                for di, dj in product(range(-1, 2), repeticiones=2):
                    if di == dj == 0:
                        continue

                    posI = i + di
                    posJ = j + dj

                    if not (0 <= posI < N and 0 <= posJ < N):
                        continue

                    cambio[posI, posJ] += 1

        octos += cambio

        if not continuacion:
            break
    conteo = 0
    for i, j in product(range(N), repeticiones=2):
        if flashed[i, j]:
            conteo += 1
            octos[i, j] = 0

    if conteo == N * N:
        break

    pasos += 1

print(pasos)