media = 0
temperaturas = [30, 32, 31, 28, 29]

for temp in temperaturas:
    media += temp

media /= len(temperaturas)
print("Média das temperaturas: ", media)