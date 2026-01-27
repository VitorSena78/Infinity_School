# dicionarios
# colecoes
# objetos iteraveis
# "super variaveis"
# armazenam mais de um dado por vez
# a ordem de insercao nao importa
# mutaveis
# sao posicionados atraves de chaves nomeadas
# par chave: valor
# as chaves sao identificadores unicos
# chave - strings,numeros ou tuplas
# valor - qualquer coisa
diciVazio = {}
diciVazio2 = dict()
dados = {
    "nome": "antonio",
    "idade": 30,
    "altura": 1.73,
    "cnh": True
}
print(dados)
# busca nao segura
print(dados["nome"])
# busca segura com condicional if
if "nome" in dados:
    print(dados["nome"])
else:
    print("Chave não encontrada")
# busca segura com funcao get()
print(dados.get("nome", "Chave não encontrada!"))
dados["cnh"] = False
print(dados)
#add
dados["genero"] = "Masculino"
print(dados)
dados.update(estado_civil="Solteiro", nacionalidade="Brasileiro")
print(dados)
#del
del dados["cnh"]
print(dados)
print(dados.pop("estado_civil"))
print(dados)

print("-"*30)

#carrega o dicionario todo mas só mostra as chaves
for d in dados:
    print(d)

print("-"*30)

#carrega somente as chaves e só mostra elas
for d in dados.keys():
    print(d)

print("-"*30)

#carrega somente os valores e só mostra eles
for d in dados.values():
    print(d)

print("-"*30)

#carrega tudo e mostra tudo
for c,v in dados.items():
    print(c,"-",v)


print(dados.keys())