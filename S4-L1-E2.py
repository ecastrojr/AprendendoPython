n = int(input("Digite o valor de n: "))
i = n
print(n)
while i > 0:
    if (n % 2) != 0:
        print(n)
        i = i - 1
    n = n + 1
    