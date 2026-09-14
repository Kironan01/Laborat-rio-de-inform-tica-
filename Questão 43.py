registros = [
    [-50, -89],
    [-78, -44],
    [-88, -22],
    [-12, -90]
    ]
aux = max(registros[0])
for i in registros:
    if aux < max(i):
        aux = max(i)

print(aux)