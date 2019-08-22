# -*- coding: utf-8 -*-
"""
Converta uma temperatura digitada em Celsius para Fahrenheit.
F = 9*C/5 + 32
"""

temperatura_C = int(input("Digite a temperatura: "))

temperatura_F = (9*(temperatura_C/5)+32)

print("Sua temperatura em Fahrenheint é: %d" %temperatura_F)