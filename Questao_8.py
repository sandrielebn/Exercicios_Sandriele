#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. ##
##Calcule e mostre o total do seu salário no referido mês.##

valor = float (input('Quanto você ganha por hora? '))
horas = float (input('Quantas horas você trabalha por mês? '))

salario = valor * horas
print('O valor do seu salário é de R$', salario, 'reais mensais.')