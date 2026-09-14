import random

resultado = random.randrange(1, 11)
resposta = int(input('Resposta: '))
if resposta == resultado:
    print('Você acertou!')
else:
    print("Você errou, tente de novo!")