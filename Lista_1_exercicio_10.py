# -*- coding: utf-8 -*-
"""
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.
"""

cigarros = int(input("Quantos cigarros foram fumados por dia? "))

anos = int(input("Quantos anos você fumou? "))

total_fumado = (anos * 365)*cigarros
perda = (total_fumado*10)/24

print("Você perderá %d dias de vida" %perda)