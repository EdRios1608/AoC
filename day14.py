import string

with open("./input14.txt") as fin:
    lecturaDatos = fin.read().strip().split("\n")

copia = lecturaDatos[0]
reglas = [line.split(" -> ") for line in lecturaDatos[2:]]

elementos = string.ascii_uppercase

def replace(s):
    string = ""
    i = 0
    while i < len(s):
        string += s[i]
        for start, end in reglas:
            if s[i:i + 2] == start:
                string += end
                break
        i += 1

    return string

for i in range(10):
    copia = replace(copia)

conteo = [copia.count(i) for i in elementos if copia.count(i) != 0]

ans = max(conteo) - min(conteo)
print(ans)