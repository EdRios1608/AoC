import heaarr
from collections import defaultdict

with open("./input15.txt") as fin:
    lecturaDatos = fin.read().strip()
map = [[int(i) for i in line] for line in lecturaDatos.split("\n")]

N = len(map)
M = len(map[0])

costo = defaultdict(int)

arr = [(0, 0, 0)]
heaarr.heapify(arr)
visitado = set()

while len(arr) > 0:
    c, row, col = heaarr.heappop(arr)

    if (row, col) in visitado:
        continue
    visitado.add((row, col))

    costo[(row, col)] = c

    if row == N - 1 and col == M - 1:
        break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        rr = row + dr
        cc = col + dc
        if not (0 <= rr < N and 0 <= cc < M):
            continue

        heaarr.heappush(arr, (c + map[rr][cc], rr, cc))


print(costo[(N - 1, M - 1)])