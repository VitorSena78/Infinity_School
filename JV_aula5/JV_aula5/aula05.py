# nome = "Antonio"

# listaVazia = []
# nomes = ["Antonio", "Gabriel", "João"]
# #           0           1         2
# #           -3         -2        -1
# print(nomes)
# print(nomes[0])
# nomes[1] = "Abel"
# print(nomes[-1])
# print(nomes[0::2])
# print(nomes)
# # metodos de manipulacao
# nomes.append("Matheus") # add ao final da lista
# print(nomes)
# nomes.insert(2, "Felipe") # add no indice escolhido
# print(nomes)
# nomes.extend(["Ana", "Camila"])
# print(nomes)
# nomes.remove("Antonio") # remove atraves do valor
# print(nomes)
# print(nomes.pop(1)) # remove atraves do indice e retorna o valor
# print(nomes)
# nomes.sort()
# print(nomes)
# nomes.reverse()
# print(nomes)
# print(nomes.index("Ana"))

# for n in nomes:
#     print(n)
    
# print("-"*30)
    
# for n in range(len(nomes)):
#     print(n, "-", nomes[n])
    
# print("-"*30)

# for i, v in enumerate(nomes):
#     print(i, "-", v)
    
# tuplaVazia = ()
# frutas = ("uva", "kiwi", "banana")
# numeros = (1,)
# print(frutas)
# print(frutas[0])

# fruta1, *resto = frutas
# print(resto)

# for f in frutas:
#     print(f)

alunos = ["Antonio", "Aquiles", "João"]
notas = [5,8,9]
for a, n in zip(alunos, notas):
    print(a, n)

# for a in range(len(alunos)):
#     for n in range(len(notas)):
#         if a == n:
#             print(alunos[a], "-", notas[n])