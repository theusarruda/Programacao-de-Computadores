""" Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário,
informe “Número inválido """

a = int(input("Informe o valor: "))

if a > 0:
    raiz = (a**0.5)
    print(f"A Raiz aproximada é {raiz:.2f}")
else:
    print("Número invalido")