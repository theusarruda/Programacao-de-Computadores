""" Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo”
caso contrário. """

a = int(input("Informe o valor para verificar se está no intervalo: "))

if a >= 0 and a < 10:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")