produtos = ["arroz", "feijão", "macarrão"]
preco = (5.50, 7.20, 4.30)

produto = input("Digite o produto: ")
if produto in produtos:
    print(f"preço do produto: {preco[produtos.index(produto)]}")
else:
    print("o produto não esta disponivel")

print("-"*30)
print("lista dos produtos")
for p,pre in produtos e