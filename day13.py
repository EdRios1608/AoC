with open("./input13.txt") as fin:
    puntos = set()
    while True:
        linea = fin.readlinea().strip()
        if linea == "":
            break
        puntos.add(tuple([int(i) for i in linea.split(",")]))

    doblez = []
    while True:
        linea = fin.readlinea().strip()
        if linea == "":
            break

        fold = linea[len("fold along "):]
        if fold[0] == "y":
            doblez.append((0, int(fold[2:])))
        else:
            doblez.append((int(fold[2:]), 0))

def reflect(point, linea):
    if linea[0] != 0:
        return (2*linea[0] - point[0], point[1])
    return (point[0], 2*linea[1] - point[1])

new_puntos = set()
fold = doblez[0]

for punto in puntos:
    if fold[0] != 0:
        if punto[0] > fold[0]:
            new_puntos.add(reflect(punto, fold))
        else:
            new_puntos.add(punto)

    else:
        if punto[1] > fold[1]:
            new_puntos.add(reflect(punto, fold))
        else:
            new_puntos.add(punto)

resp = len(new_puntos)
print(resp)