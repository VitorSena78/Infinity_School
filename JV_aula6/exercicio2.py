populacoes = {
    "Brasil": 215_000_000, 
    "China": 1_400_000_000,
    "EUA": 333_000_000,
    "Índia": 1_220_000_000
}

pais_maior_pop ="" 
maior_pop=0

for k,v in populacoes.items():
    if v > maior_pop:
        maior_pop = v
        pais_maior_pop = k

print(f"O país com a maior população é: {pais_maior_pop} com {maior_pop} habitantes.")