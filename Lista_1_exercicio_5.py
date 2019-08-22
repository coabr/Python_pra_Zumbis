# -*- coding: utf-8 -*-
"""
Solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço a pagar.
"""
valor_mercadoria = int(input("Digite o valor da mercadoria: "))
percentual_desconto = int(input("Qual o percentual de deconto? "))

valor_desconto = (valor_mercadoria*percentual_desconto)//100 
#coloquei // para ser um valor inteiro no resultado da divisão e não um float
print("O valor a pagar é ", (valor_mercadoria-valor_desconto))