alunos = {}


while True:
    print("-"*30)
    print("Digite o nome do aluno ou sair para sair")
    nome=input("Nome: ").strip()
    if nome.lower() == "sair":
        break
    materias = {}
    while True:
        print("-"*30)
        print("Digite o nome da materia ou fim para sair")
        materia=input("Materia: ").strip()
        if materia.lower() == "fim":
            break
        print(f"Digite a nota da materia {materia}")
        nota=float(input("Nota: "))
        materias[materia] = nota
    alunos[nome] = materias

print("--- Cadastro de Alunos ---")
for k,v in alunos.items():
    print(f"Aluno: {k}")
    for m,n in v.items():
        print(f"{m}: {n}")