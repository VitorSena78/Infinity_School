quantidade_de_itens=int(input("Quantos itens deseja adicionar: "))
lista = []
for i in range(quantidade_de_itens):
    lista.append(input("Digite o item: "))

print(f"Lista completa: {lista}")
resposta=""
while resposta != "n":
    resposta = input("Deseja remover algum item (y/n): ")
    if resposta == "y":
        item_a_ser_removido= input("Digite o item a ser removido: ")
        if item_a_ser_removido in lista:
            lista.remove(item_a_ser_removido)
            print(f"lista atual: {lista}")
        else:  
            print("O item não existe na lista")
   
print()    
print("="*30)
print(f"lista final: {lista}")