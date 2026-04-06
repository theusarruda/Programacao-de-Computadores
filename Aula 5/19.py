""" Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença
entre eles. """

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))

if a == b:
    print("Os números são iguais")
elif a > b:
    dif1 = a - b
    print("A é maior que B e a é diferença é: ",dif1)
else:
    dif2 = b - a
    print("B é maior que A e a diferença é: ",dif2)