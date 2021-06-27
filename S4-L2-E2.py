n = int(input("Digite um número inteiro: "))
x = 0
while n > 0:
    if (n % 10) == ((n // 10)%10):
        x = x + 1
    n = n // 10
if x == 0:
    print("não")
else:
    print("sim")