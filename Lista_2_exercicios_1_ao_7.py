def quest1():
       
    """
    Faça um Programa que peça os três lados de um triângulo. 
    O programa deverá informar se os valores podem ser um triângulo. 
    Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    """

    ladoA = int(input("Digite o valor do lado A: "))
    ladoB = int(input("Digite o valor do lado B: "))
    ladoC = int(input("Digite o valor do lado C: "))

    if abs(ladoA-ladoB) < ladoC < ladoA+ladoB and abs(ladoB-ladoC) < ladoA < ladoB+ladoC and abs(ladoA-ladoC) < ladoB < ladoA+ladoC:
        if ladoA == ladoB and ladoB==ladoC and ladoC==ladoA:
            print ("O triângulo é equilátero!")
        elif ladoA == ladoB or ladoB==ladoC or ladoA==ladoC:
                print ("O triângulo é isósceles!")
        elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
            print ("O triângulo é escaleno!")
        
    else:
        print ("Com esses valores não é possível formar um triângulo")




def quest2():
    """
    Determine se um ano é bissexto. Verifique no Google como fazer isso...
    """
    ano = int(input("Digite um ano: "))
    if ano % 4 == 0:
        if ano % 100 != 0:
            print ("O ano é bissexto")
        else:
            if ano % 400 == 0:
                print("O ano é bissexto")
           
    else:
        print("O ano não é bissexto")




def quest3():
    """
    João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
    seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
    estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
    faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
    variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
    variáveis com o conteúdo ZERO.
    """
    peso_max = 50
    excesso = 0
    multa = 0
    
    peso_peixe = int(input("Digite o peso de peixe comprado: "))
    if peso_peixe > peso_max:
        excesso = peso_peixe - peso_max
        multa = excesso*4
    else:
        print("Não há excesso")
    print("A multa é %d." %multa)
       


def quest4():
    """
    Faça um Programa que leia três números e mostre o maior deles.
    """
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    
    maior = 0
    
    if num1>maior:
        maior = num1
        if num2>maior:
            maior = num2
            if num3>maior:
                maior= num3
    print ("O maior número é o: %d" %maior)
    
    
    
    
def quest5():
    """
    Faça um Programa que leia três números e mostre o maior e o menor deles.
    """
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    
    my_list = [num1, num2, num3]

    my_list.sort()
    
    print ("O menor número é o:", my_list[0])
    print ("O maior número é o:", my_list[2])
    
    
    
    
def quest6():
    """
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
    8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
    quanto pagou ao sindicato e o salário líquido. 
    Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido,
    """
    hour_price = int(input("Quanto você ganha por hora? "))
    hours_worked = int(input("Quantas horas você trabalhou esse mês? "))

    salario_bruto = hour_price * hours_worked
    
    iR = (11*salario_bruto)//100
    
    iNSS = (8*salario_bruto)//100
    
    sindicato = (5*salario_bruto)//100
    
    salario_liquido = salario_bruto - iR - iNSS - sindicato
    
    print ("O salário é: R$ %.2f" %salario_liquido)
    
    
    
    
def quest7():
    """
    Faça um programa para uma loja de tintas. 
    O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
    Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
    em latas de 18 litros, que custam R$ 80,00.
    Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
    Obs. : somente são vendidos um número inteiro de latas.
    """
    import math 
    
    area = int(input("Qual o tamanho em metros da área a ser pintada? "))
    
    paint = area/3
    
    gallons = math.ceil(paint/18)     
            
    price = gallons*80
    
    print("Você irá precisar de %d galões de tinta." %gallons)
    print("Você irá gastar R$ %d." %price)

        
if __name__ == '__main__':
    #quest1()
    #quest2()
    #quest3()
    #quest4()
    #quest5()
    #quest6()
    #quest7()
