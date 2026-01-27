vogais = "aeiouáéíóúàèìòùâêîôûãẽĩõũ"
contador = 0
palavra = input("Digite uma palavra: ")
for i in palavra:
     if i.lower() in vogais:
        contador += 1
        print(i)
print(f"o total de vogais na palavra é: {contador}")