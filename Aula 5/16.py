""" Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado. """

a = input("Informe o valor: ")
print(type(a))

try:
    a =int(a)
    print("O valor quadrado do valor informado é: ", (a**2))
except:
    print("O tipo de varíavel não é inteira")