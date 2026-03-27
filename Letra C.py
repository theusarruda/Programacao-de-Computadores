"""Construa um algoritmo que receba o valor de um produto e calcule o preço final considerando um
acréscimo de 8% de imposto"""

produto = float(input("Digite o valor do produto: "))
imposto = 0.08

valor_final = produto + (produto * imposto)
print("O valor final do seu produto é ", valor_final)