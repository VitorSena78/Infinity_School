soma = 0
contador = 0
media = 0
while contador < 5:
    contador += 1
    soma += int(input(f"digite o {contador}º numero inteiro: "))
    media = soma / contador
    print(f"a soma: {soma}")
print(f"a media é: {media}")