# Crie um programa que cadastre alguns produtos e suas quantidades. Primeiro, pergunte quantos produtos o usuário deseja cadastrar. Em seguida, use um laço for para repetir o pedido do nome e da quantidade do produto o número de vezes informado. Durante o laço, mostre na tela cada produto cadastrado no formato: Produto: X | Quantidade: Y
quantidade_de_produtos = int(input("Digite quantos produtos serão cadastrados: "))

for i in range(quantidade_de_produtos):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    print(f"Produto: {nome} | Quantidade: {quantidade}")