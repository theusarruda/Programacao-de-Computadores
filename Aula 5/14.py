"""  Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é
múltiplo”. """

a = input("Informe o valor: ")
a = int(a)

if a % 3 == 0:
    print("O valor é multiplo de 3")
else:
    print("O valor não é multiplo de 3")