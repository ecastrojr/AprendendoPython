n = int(input("Digite um número inteiro: "))
i = n
x = 0
while i > 1:
    if (n % i) == 0:
        x = x + 1
    i = i - 1
if x == 1:
    print("primo")
else:
    print("não primo")