flag = True
senha = input("Digite a senha:") 
while flag:
    if senha == "senha123":
        print("Acesso concedido!")
        flag=False
    else:
        print("Acesso Negado!")
        senha = input("Digite a senha:") 