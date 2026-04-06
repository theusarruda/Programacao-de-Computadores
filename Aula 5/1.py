""" Leia um número inteiro e informe se ele é positivo ou negativo """

a = int(input("Informe o número: "))

if a > 0:
    print("O número é positivo")
elif a == 0:
    print("O número é neutro")
else:
    print("O número é negativo")