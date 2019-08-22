# -*- coding: utf-8 -*-
"""
Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a porcentagem do aumento. 
Exiba o valor do aumento e do novo salário.
"""
#eu escolhi não colocar float, e sim inteiro para o salário
salario = int(input("Digite seu salário: "))
aumento_percentual = int(input("Digite a porcentagem de aumento: ")) 

aumento_salarial = (salario*aumento_percentual)/100

novo_salario = salario+aumento_salarial

print("Seu aumento foi: %d" %aumento_salarial)
print("Seu novo salário é: %d" %novo_salario)