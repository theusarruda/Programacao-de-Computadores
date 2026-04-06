""" Leia um número e: Se estiver entre 10 e 20 → “Dentro”; Caso contrário → “Fora”. """

a = int(input("Informe o número: "))

if a >= 10 and a <= 20:
    print("O número está Dentro")
else:
    print("O número está fora")