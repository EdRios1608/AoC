from collections import defaultdict, deque
from pprint import pprint

def is_small(cave):
    return cave.islower()

with open("./input12.txt") as fin:
    lecturaDatos = fin.read().strip()
datos = [i.split("-") 
         for i in lecturaDatos.split("\n")]

list = defaultdict(list)

for a, b in datos:
    list[a].append(b)
    list[b].append(a)

global resp
resp = 0

visitado = defaultdict(int)

def dfs(cave):
    global resp

    if cave == "end":
        resp += 1
        return

    if is_small(cave):
        visitado[cave] += 1

        visitadoMasDeUnaVez = 0
        for small in visitado:
            visitadoMasDeUnaVez += visitado[small] > 1

            if visitado[small] > 2:
                visitado[cave] -= 1
                return

        if visitadoMasDeUnaVez > 1:
            visitado[cave] -= 1
            return

    for nbr in list[cave]:
        if nbr == "start":

            continue
        dfs(nbr)

    if is_small(cave):
        visitado[cave] -= 1

dfs("start")

print(resp)