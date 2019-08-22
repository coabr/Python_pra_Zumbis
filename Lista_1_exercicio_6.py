# -*- coding: utf-8 -*-
"""
Calcule o tempo de uma viagem de carro. 
Pergunte a distância a percorrer e a velocidade média esperada para a viagem
"""

distancia = int(input("Qual a distância? ")) 
velocidade = int(input("Qual a velocidade média? "))

tempo = distancia//velocidade
#é um programa simples, não aceitando horas quebradas e tempos de viagem com menos de "horas"
print("Sua viagem terá a duração de %d horas" %tempo)