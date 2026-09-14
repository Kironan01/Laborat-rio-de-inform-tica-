custos = [
    [89, 50],
    [78, 44],
    [88, 22]
    ]
aux = min(custos[0]) 
for i in custos: 
    if aux > min(i):
        aux = min(i)
print(aux)