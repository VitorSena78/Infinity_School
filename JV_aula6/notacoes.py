dados = {
    "chave5": 89,
    "chave2": 19,
    "chave3": 16,
    "chave4": 15,
    "chave1": 10
}
#print(list(dados.items())[2])

print(max(dados.values()))

frutas = {"uva", "kiwi", "pera", "banana"}
frutas2 = {"abacaxi", "melao", "uva"}
frutas3 = frutas - frutas2
frutas4 = frutas.difference(frutas2)
print(frutas3)
print(frutas4)