salario_por_mes= float(input("qunto você ganha por mês?: "))
horas_trabalhadas= float(input("quntas horas você trabalha por semana?:"))

horas_trabalhadas_mes = (horas_trabalhadas*4) - 8
true
salario_por_hora = salario_por_mes/horas_trabalhadas_mes

print(f"o seu salario por hora é: {salario_por_hora:.2f}")