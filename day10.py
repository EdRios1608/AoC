with open("./input10.txt") as fin:
    lecturaDatos = fin.read().strip()
datos = lecturaDatos.split("\n")

pares = ["()", "[]", "<>", "{}"]
puntuacion = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
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
            return puntuacion[char]

    return 0


resp = 0
for line in datos:
    resp += parse(line)

print(resp)