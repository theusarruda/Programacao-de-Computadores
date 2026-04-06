a_str = input("Informe o valor do cateto A: ")
b_str = input("Informe o valor da cotato B: ")
a = float(a_str)
b = float(b_str)

c = ((a * a) + (b * b)) ** 0.5
print(f"O valor da hipotenusa do cateto A: {c:.2f}")


