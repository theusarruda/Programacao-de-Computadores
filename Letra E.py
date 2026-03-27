"""Construa um algoritmo que receba a altura e o peso de uma pessoa e calcule o Índice de Massa
Corporal (IMC)"""

p = float(input("Informe o seu peso: "))
h = float(input("Informe sua altura: "))

imc = p / h ** 2
print(f"O seu IMC é {imc:.2f}")