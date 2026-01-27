# contador = 0
# while contador < 5:
#     print("olá")
#     contador += 1

# print("-"*30)

# for i in range(11):
#     print(i)

# print("-"*30)

# for i in range(1, 11):
#     print(i)

# print("-"*30)

# for i in range(1, 11, 2):
#     print(i)

# print("-"*30)

# for i in range(10, 0, -2):
#     print(i)

# nome = "Antonio"
# for letra in nome:
#     print(letra)
'''
vogais = "aeiouáéíóúãõ"
totalVogais = 0
palavra = input("Digite um palavra: ")
for letra in palavra:
    if letra.isalpha():
        if letra.lower() in vogais:
            totalVogais += 1
print(f"O total de vogais é: {totalVogais}")
'''

# r=range(5)
# o = 0
# print(r.count)
# for i in range(5):
#     print(o)
#     o += 1

# listaVazia = []
# nomes = ["Antonio", "João", "Luan"]
# nomes[2] = "Caio"
# print(nomes)
# nomes.append("Matheus") #add no final da lista
# print(nomes)
# nomes.insert(1, "Tiago") #add no indice escolhido
# print(nomes)
# nomes.remove("Antonio") #remove o valor indicado e nao tem retorno
# print(nomes)
# print(nomes.pop(2)) #remove o valor indicado e retorna o valor que foi removido
# print(nomes)
# print(nomes.index("Tiago"))
# print(nomes.count("Tiago"))
# novosNomes = nomes.copy()
# nomes.clear()
# print(nomes)
# print(novosNomes)
# novosNomes.sort()
# print(novosNomes)
# novosNomes.reverse()
# print(novosNomes)
# numeros = [1,2,3]
# mista = ["antonio", 30, 1.73, True, numeros]

numeros = [1,2,3,4,5,6,7,8,9]
soma = 0
for n in numeros:
    soma += n    
media = soma/len(numeros)
# media = sum(numeros)/len(numeros)
print(media)