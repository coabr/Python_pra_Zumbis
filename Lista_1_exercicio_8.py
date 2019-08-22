# -*- coding: utf-8 -*-
"""
Converta uma temperatura digitada em Celsius para Fahrenheit.
F = 9*C/5 + 32
"""

temperatura_F = int(input("Digite a temperatura: "))

temperatura_C = ((temperatura_F-32)*5/9)

print("Sua temperatura em Celsius é: %d" %temperatura_C)