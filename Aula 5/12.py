""" Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais """

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo valor: "))

soma = a + b
print("A soma dos valores é ", soma)

if a > b:
    print("O primeiro valor valor é maior: ",a)
elif a < b:
    print("O segundo valor é maior: ",b)
else:
    print("Os valores são iguais")