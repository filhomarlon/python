"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

valorhora = int(input("Digite o valor da hora trabalhada: "))
numero_hora = int(input("Digite a quantidade de horas trabalhadas: "))

sal_mes = valorhora*numero_hora

print("Salario do mes corrente é: ", sal_mes)
