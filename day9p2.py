import numpy as np

with open("./input9.txt") as fin:
    lecturaDatos = fin.read().strip().split("\n")
    map = [[int(i) for i in list(line)] 
           for line in lecturaDatos]

filas = len(map)
columnas = len(map[0])

low = []
cur_id = 1
ids = np.zeros((filas, columnas), dtype=int)

# Find low points
for fila in range(filas):
    for col in range(columnas):
        is_low = True
        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            posR = fila + d[0]
            posC = col + d[1]

            if not ((0 <= posR and posR < filas) and (0 <= posC and posC < columnas)):
                continue

            if map[posR][posC] <= map[fila][col]:
                is_low = False
                break

        if is_low:
            low.append((fila, col))

#DFS
for fila, col in low:
    stack = [(fila, col)]
    visitado = set()
    while len(stack) > 0:
        fila, col = stack.pop()

        if (fila, col) in visitado:
            continue
        visitado.add((fila, col))

        ids[fila, col] = cur_id

        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            posR = fila + d[0]
            posC = col + d[1]

            if not ((0 <= posR and posR < filas) and (0 <= posC and posC < columnas)):
                continue

            if map[posR][posC] == 9:
                continue

            stack.append((posR, posC))

    cur_id += 1

sizes = [0] * cur_id

for x in ids.flatten():
    sizes[x] += 1
sizes = sizes[1:]

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])