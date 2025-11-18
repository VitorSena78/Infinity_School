nome_completo = input("Digite o nome do funcionario: ")
idade = int(input("Digite a idade do funcionario: "))
salario_mensal = float(input("Digite o salario do funcionario: "))
salario_anual = salario_mensal*12

print()
print("="*20)
print("Dados pessoais do funcionario:")
print(f"Nome: {nome_completo}")
print(f"Idade: {idade}")
if idade >= 18:
    print("O funcionario é maior de idade")
else:
    print("O funcionario é menor de idade")
print(f"Salario anual: {salario_anual}")

