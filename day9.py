with open("./input9.txt") as fin:
    lecturaDatos = fin.read().strip().split("\n")
    map = [[int(i) for i in list(line)] 
           for line in lecturaDatos]

filas = len(map)
columnas = len(map[0])

resp = 0

for fila in range(filas):
    for col in range(columnas):
        low = True
        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            posR = fila + d[0]
            posC = col + d[1]

            if not ((0 <= posR and posR < filas) and (0 <= posC and posC < columnas)):
                continue

            if map[posR][posC] <= map[fila][col]:
                low = False
                break

        if low:
            resp += map[fila][col] + 1

print(resp)