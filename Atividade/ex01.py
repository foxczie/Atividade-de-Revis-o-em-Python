# 1. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# • até 20 litros: desconto de 3% por litro
# • acima de 20 litros: desconto de 5% por litro
# Gasolina:
# • até 20 litros: desconto de 4% por litro
# • acima de 20 litros: desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado
# da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = int(input('Quantos litros de gasolina foram comprados? '))
tipo = input('Qual o tipo do combustível, sendo "A" para Álcool e "G" para Gasolina? ')
gasolina = 2.5
alcool = 1.9

if tipo == 'A':
    valor = litros * alcool
    if litros > 20:
        desconto = valor * (5/100)
        valorfinal = valor - desconto
        print(f'O valor a ser pago é de R${valorfinal}')
    else:
        desconto = valor * (3/100)
        valorfinal = valor - desconto
        print(f'O valor a ser pago é de R${valorfinal}')

if tipo == 'G':
    valor = litros * gasolina
    if litros > 20:
        desconto = valor * (6/100)
        valorfinal = valor - desconto
        print(f'O valor a ser pago é de R${valorfinal}')
    else:
        desconto = valor * (4/100)
        valorfinal = valor - desconto
        print(f'O valor a ser pago é de R${valorfinal}')


