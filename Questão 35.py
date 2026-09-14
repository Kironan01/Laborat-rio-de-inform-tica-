produtos = {}

for i in range(3):
    nome = input('Nome do produto: ')
    quantidade = int(input('Quantidade do produto: '))

    produtos.update({nome:quantidade}) 
print(produtos)