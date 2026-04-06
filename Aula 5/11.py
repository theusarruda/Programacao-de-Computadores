"""" Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par
negativo”; Caso contrário → “Ímpar” """

a = int(input("Informe o valor: "))

if a % 2 == 0:
    if a > 0:
        print("Par positivo")
    else:
        print("Par negativo")
else:
    print("Negativo")


