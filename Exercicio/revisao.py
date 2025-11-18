# Crie um sistema que ajude um caixa de loja a registrar vendas até que o cliente finalize a compra: Pergunte ao usuário o preço de cada item. Use um loop while para continuar somando os valores enquanto o usuário não digitar 0, que indica o fim da compra. Após o término, exiba o total da compra no formato: "Total da compra: R$ X". A cada item adicionado, exiba também o valor acumulado até o momento. Dica: use uma variável para acumular o total e outra para armazenar o valor do item informado pelo usuário.
preco_do_item="$"
total=0
while preco_do_item != 0:
    print("digite o valor do item para adicionalo ao montante")
    print("0 - digite o valor 'o' para sair\n")
    preco_do_item=float(input("Digite o valor do item: "))
    total=preco_do_item+total
    print(f"valor acumulado: R$ {total}\n")

print(f"\nTotal da compra: R$ {total}")
