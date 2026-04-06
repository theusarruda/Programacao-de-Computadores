a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))

if a < b and a < c:
    print("O menor número é a: ", a)
elif b < c:
    print("O menor número é b:", b)
elif c < b:
    print("O menor número é c: ", c)
else:
    print("Todos os número são iguais")
