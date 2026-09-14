notas = []

while True:
    
    nota = (float(input("Nota: ")))
    if nota > 10:
        break
    notas.append(nota) 
print("Maior nota: ", max(notas))