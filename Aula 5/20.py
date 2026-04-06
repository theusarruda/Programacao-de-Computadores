""" Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo,
mostre na tela o valor. """

a = int(input("Digite um valor: "))

if a < 0 and a > 100:
    print("Valor fora do intervalo: ", a)

else:
    print("O valor faz parte do intervalo")