senha = "" 
while senha!="1234":
    senha = input("Digite a senha:")
    if senha == "1234":
        print("Acesso liberado!")
        break
    else:
        print("Acesso Negado!")
        continue