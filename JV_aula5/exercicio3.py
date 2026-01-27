tupla = ("banana", "uva", "maçã", "kiwi", "laranga")

print("Frutas disponives: ")
for f in tupla:
    print(f)
    
    
print()   
fruta = input("Digite o nome de uma fruta: ")

if fruta in tupla:
    print("A fruta esta disponivel na feira")
else:
    print("A fruta não esta disponivel na feira")
    
print(f"Existem: {len(tupla)} frutas na feira")