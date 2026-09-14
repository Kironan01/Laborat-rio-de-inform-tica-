import random

resultado = random.randrange(1, 11)
resposta = int(input('Resposta: '))

while resultado != resposta:
    if resultado > resposta:
        print("Resultado é maior.")
    elif resultado < resposta:
        print('Resultado é menor.')
    resposta = int(input('Nova Respostta: '))    
   
print("Parabens você acertou!")