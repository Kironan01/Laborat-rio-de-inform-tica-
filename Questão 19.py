import math

valor = int(input("Valor: ")) 
if valor < 0:
    print("Valor invalido!")
else:
    print("Resultado: ",math.factorial(valor))