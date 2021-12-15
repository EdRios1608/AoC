import numpy as np
from itertools import product

with open("./input11.txt") as fin:
    lecturaDatos = fin.read().strip()
datos = np.array([[int(x) for x in list(i)]
                for i in lecturaDatos.split("\n")], dtype=int)

ans = 0

N = len(datos)

octos = datos

for step in range(100):
    flashed = np.zeros((N, N), dtype=bool)

    for i, j in product(range(N), repeat=2):
        octos[i, j] += 1

    while True:
        continuacion = False

        cambio = np.zeros((N, N), dtype=int)

        for i, j in product(range(N), repeat=2):
            if not flashed[i, j] and octos[i, j] > 9:

                ans += 1
                flashed[i, j] = True
                continuacion = True

                for di, dj in product(range(-1, 2), repeat=2):
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

    for i, j in product(range(N), repeat=2):
        if flashed[i, j]:
            octos[i, j] = 0

print(ans)