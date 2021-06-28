def fatorial(n):
    x = 1   
    while (n > 1):
        x = n * x
        n = n - 1
    return x

def testa_fatorial():
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
    if fatorial(10) == 3628800:
        print("Funciona para 10")
    else:
        print("Não funciona para 10")

def numero_binomial(n,k):
    return fatorial(n) / (fatorial(k) / fatorial(n-k))

testa_fatorial()