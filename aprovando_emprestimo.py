#!/usr/bin/env python3

# regras:
# O valor da parcela não pode ser maiior que 30% do sálario
# A quantidade de parcelas não pode ser maior que 360

salario = float(input("Informe o sálario do comprador:  ").replace(',' , '.'))
parcelas = int(input("Informe a quantidade de parcelas:  "))
valor_imovel = int(input("Informe o valor do imóvel desejado:  "))

parcela_maxima = salario * 30 / 100
parcela_mensal = valor_imovel / parcelas

if (parcela_mensal <= parcela_maxima) & (parcelas <= 360):
    print("Aprovado")
elif (parcela_mensal <= parcela_maxima) & (parcelas > 360):
    print("Reprovado: a quantidade de parcelas é maior que 360")
elif (parcela_mensal > parcela_maxima) &  (parcelas < 360):
    print("Reprovado: o valor da mensalidade é maior que 30% do salário")