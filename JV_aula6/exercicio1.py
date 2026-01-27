vendas = {"Ana": 10, "Bruno": 15, "Carla": 8} 
vendas["Pedro"] = 12
print(vendas)
vendas.pop("Carla")
print(vendas)

soma=sum(vendas.values())
print(f"soma das vendas: {soma}")