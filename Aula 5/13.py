""" Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro. """

a = int(input("Informe o valor a ser verificado: "))

if a > 100:
    print(" A metade do número informado: ", a/2)
else:
    print("O dobro do número informado é ", a*2)