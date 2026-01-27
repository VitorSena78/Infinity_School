'''
Você vai criar um programa que solicita ao usuário uma nota de 0 a 10 e informa a classificação dessa nota. O programa deve: Pedir ao usuário a digitação de uma nota (use input() e converta para float). Verificar a classificação 
da nota usando estruturas condicionais if/elif/else: Nota maior ou igual a 9 → "Excelente" Nota maior ou igual a 7 → "Bom" Nota maior ou igual a 5 → "Regular" Nota menor que 5 → "Reprovado" Exibir a classificação correspondente.
'''
nota=float(input("digite a nota: "))

if nota>=9:
    print("sua nota foi Exelente")
elif nota>=7:
    print("sua nota foi Boa")
elif nota>=5:
    print("sua nota foi Regular")
else:
    print("Reprovado")