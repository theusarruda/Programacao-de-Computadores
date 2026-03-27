"""Desenvolva um algoritmo que receba cinco números, calcule a média aritmética e apresente o
resultado final """

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))
d = float(input("Digite o quarto valor: "))
e = float(input("Digite o quinto valor: "))

media = (a + b + c + d + e) / 5
print(f"A média aritmética é {media:.2f}")