with open("./input10.txt") as fin:
    lecturaDatos = fin.read().strip()
datos = lecturaDatos.split("\n")

pares = ["()", "[]", "<>", "{}"]
malasPuntuaciones= {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
buenasPuntuaciones = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def parse(line):
    pila = []
    for char in line:
        good = False
        for p in pares:
            if char == p[0]:
                pila.append(char)
                good = True
            elif char == p[1]:
                if pila[-1] == p[0]:
                    pila.pop()
                    good = True

        if not good:
            return bad_puntuaciones[char]

    return 0


def complete(line):
    pila = []
    resp = 0
    for char in line:
        for p in pares:
            if char == p[0]:
                pila.append(char)
            elif char == p[1]:
                if pila[-1] == p[0]:
                    pila.pop()

    for c in pila[::-1]:
        resp *= 5
        resp += buenasPuntuaciones[c]

    return resp



datos = [line for line in datos if parse(line) == 0]

puntuaciones = []
for line in datos:
    puntuaciones.append(complete(line))

puntuaciones.sort()
print(puntuaciones)
resp = puntuaciones[len(puntuaciones) // 2]
print(resp)