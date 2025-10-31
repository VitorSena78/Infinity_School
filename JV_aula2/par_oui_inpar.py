numero = int(input("digite um numero inteiro: "))

if numero>0:
        print("numero é positivo e ")
        if  numero%2==0:
                print("numero é par")
        else:
                print("é inpar")
elif numero>0:
        print ("numero é negativo e ")
        if  numero%2==0:
                print("numero é par")
        else:
                print("é inpar")
else:
        print("o numero é 0")