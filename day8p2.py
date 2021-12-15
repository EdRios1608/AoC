import itertools
from pprint import pprint

with open("./input8.txt") as fin:
    lecturaDatos = fin.read().strip().split("\n")
    datos = [
        [
            sorted(line[:line.index("|") - 1].split(" ")),
            line[line.index("|") + 2:].split(" ")
        ] for line in lecturaDatos
    ]

claves = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
]
digitos = sorted(claves)
digitos = tuple(digitos)

ans = 0

for line in datos:
    clues = line[0]
    assert len(clues) == 10
    num = line[1]
    # Try all possible substitutions
    for sigma in itertools.permutations("abcdefg"):
        valor = {}
        for c in "abcdefg":
            valor[c] = sigma["abcdefg".index(c)]

        nuevasPistas = [] * 10
        for clue in clues:
            x = ""
            for char in clue:
                x += valor[char]
            x = "".join(sorted(x))
            nuevasPistas.append(x)

        nuevasPistas.sort()

        if tuple(nuevasPistas) == digitos:
            n = []
            for d in num:
                x = ""
                for char in d:
                    x += valor[char]
                x = "".join(sorted(x))
                n.append(claves.index(x))

            ans += int("".join([str(i) for i in n]))

            break

print(ans)