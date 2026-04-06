a = int(input("Escreva o primeiro número:"))
b = int(input("Escreva o segundo número: "))
c = int(input("Escreva o terceiro número:"))

numbers = [a,b,c]
numbers = sorted(numbers)

print(f"A ordem crescen dos número é {numbers[0], numbers[1], numbers[2]}")