from collections import defaultdict, deque
from pprint import pprint


def is_small(cave):
    return cave.islower()


with open("./input12.txt") as fin:
    lecturaDatos = fin.read().strip()
datos = [i.split("-") for i in lecturaDatos.split("\n")]


arr = defaultdict(list)

for a, b in datos:
    arr[a].append(b)
    arr[b].append(a)

global resp
resp = 0

visitado = set()


def dfs(cave):
    global resp
    if cave == "end":
        resp += 1
        return

    if is_small(cave) and cave in visitado:
        return

    if is_small(cave):
        visitado.add(cave)

    for nbr in arr[cave]:
        if nbr == "start":

            continue
        dfs(nbr)

    if is_small(cave):
        visitado.remove(cave)


dfs("start")


print(resp)