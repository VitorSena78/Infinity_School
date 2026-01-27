nomes = []
for i in range(3):
    nome=input(f"Digite o nome do aluno({i+1}): ")
    nomes.append(nome)


notas = []
for i in range(3):
    nota=int(input(f"Digite uma nota de (0 a 10) para o aluno({i+1}): "))
    notas.append(nota)



situacoes=[]
for nota in notas:
    if nota >=7:
        situacao = "Aprovado"
    elif nota >= 5 and nota < 7:
        situacao= "Recuperação"
    else:
        situacao ="Reprovado"

    situacoes.append(situacao)
    
print("\n","="*30)
print("Nome | Nota | Situação")
for nome, nota, situacao in zip(nomes, notas, situacoes):
    print(f"{nome} - {nota} - {situacao}")