"""Construa um algoritmo que receba a quantidade de horas trabalhadas por um funcionário e o valor
da hora trabalhada, calculando o salário total."""

horas = float(input("Informe a quantidade de horas trabalhadas:"))
minutos = float(input("Informe quantos minutos trabalho, caso haja:"))
valor_hora = float(input("Informe o valor da sua hora trabalhada: "))

horas_totais = horas + (minutos/60)
salario = valor_hora * horas_totais

print("O valor do seu salário total é: ", salario)



