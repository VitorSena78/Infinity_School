print("Calculadora de IMC")
print("-"*20, "\n")

nome = input("Digite o seu nome: ")
idade = int(input("Digite o seu idade: "))
cidade = input("Digite o seu cidade: ")
altura = float(input("Digite o seu altura: "))
peso = float(input("Digite o seu peso: "))

print(f"Bemvindo a {cidade}")


if  (0 < altura < 4) and (0 < peso < 700):
    imc = peso / (altura * altura)
    if imc > 30:
        print(f"{nome}, idade: {idade}, IMC: {imc}, com obesidade")
    elif imc > 25:
        print(f"{nome}, idade: {idade}, IMC: {imc}, com sobrepeso")
    elif imc > 18.5:
        print(f"{nome}, idade: {idade}, IMC: {imc}, com peso normal")
    elif imc < 18.5:
        print(f"{nome}, idade: {idade}, IMC: {imc}, com baixo peso")
else:
    print("peso ou altura incoretos")


