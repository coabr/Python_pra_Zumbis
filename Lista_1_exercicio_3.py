"""
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
o total em segundos.
"""

dias = int(input("Digite a qtd de dias: "))
horas = int(input("Digite a qtd de horas: "))
minutos = int(input("Digite a qtd de minutos: "))
segundos = int(input("Digite a qtd de segundos: "))

conversão = (dias*24*60*60)+(horas*60*60)+(minutos*60)+segundos

print(conversão)