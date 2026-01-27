aluno1 = []
nome=input("Digite o nome do aluno1: ")
nota=input("Digite uma nota de (0 a 10) para o aluno1: ")
aluno1.extend([nome, nota])

aluno2 = []
nome=input("Digite o nome do aluno2: ")
nota=input("Digite uma nota de (0 a 10) para o aluno2: ")
aluno2.extend([nome, nota])

aluno3 = []
nome=input("Digite o nome do aluno3: ")
nota=input("Digite uma nota de (0 a 10) para o aluno3: ")
aluno3.extend([nome, nota])


if nota >=7:
    situacao = "Aprovado"
elif nota >= 5 and nota < 7:
    situacao= "Recuperação"
else:
    situacao =" "
