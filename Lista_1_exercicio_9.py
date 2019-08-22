# -*- coding: utf-8 -*-
"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
"""

km_percorridos = int(input("Quantos kms foram percorridos? "))
dias = int(input("Quantos dias foi usado? "))

preço = (km_percorridos*0.15)+(dias*60)

print("O valor a pagar é %d" %preço)