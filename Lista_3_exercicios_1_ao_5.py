# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:58:20 2019

@author: Carol
"""

def quest1():
    '''
    Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
    seja inválido e continue pedindo até que o usuário informe um valor válido.
    '''
    while True:
        nota = int(input("Digite uma nota de 0 a 10: "))
        if 0 <= nota <= 10:
            print("Nota correta, obrigada!")
            break
        else:
            print("Nota inválida")
               
def quest2():
    '''
    Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
    nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
    '''
    # pensar em formas de melhorar essa questão, uma avaliação melhor que compare senha e usuário
    
    usuario = input("Digite seu usuário: ").upper()
    while True:
        senha = input("Digite uma senha de 6 dígitos: ").upper()
        if senha != usuario:
            print("Credenciais salvas.")
            break
        else:
            print("Sua senha não pode conter seu nome, digite novamente.")

def quest3():
    '''
    Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
    anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
    crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
    necessários para que a população do país A ultrapasse ou iguale a população do país B,
    mantidas as taxas de crescimento
    '''
    paisA = 80000 
    taxa_crescimentoA = 1.030 
    paisB = 200000
    taxa_crescimentoB = 1.015
    
    contador = 0
    
    while True:
        if paisA < paisB:
            paisA *= taxa_crescimentoA      
            paisB *= taxa_crescimentoB
            contador+= 1
        else:
            print ("O número de anos necessários é", contador, "para que a população do país A ultrapasse \
                   ou iguale a população do país B.")
            print ("As populações serão---> País A:",(paisA),"e País B:",(paisB))
            break
        
def quest4():
    '''
    A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
    formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
    soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
    de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
    '''
    n = int(input("Número: "))
    a, b = 1, 1
    contador = 1
    
    while contador < n-2:
        a, b = b, a+b
        contador += 1
        
    print ("Fibonacci(%d): %d" %(n,b))
    
def quest5(): 
    '''
    Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
    o algoritmo de Euclides.
    '''
    num1 = int(input("Digite o valor de a: "))
    num2 = int(input("Digite o valor de b: "))

    
    while num1 % num2 != 0:
        num1, num2 = num2, num1%num2
        
    print("O MDC de a e b é %d" %num2)   
    
if __name__ == '__main__':
    #quest1()
    #quest2()
    #quest3()
    #quest4()
    #quest5()
