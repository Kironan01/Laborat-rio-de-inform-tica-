produtos = []

for _ in range(5):
    produto = (input("Adicione produto:"))
    produtos.append(produto) 
print("Lista de podutos: ")
for produto in produtos:
    print(produto)