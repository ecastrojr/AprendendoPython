def ex1():
    x = 1
    cont = 0
    while x < 3:
        y = 0
        while y <= 4:
            cont = cont + 1
            print(cont, end=": ")
            print(y)
            y = y + 1
        print(x)
        x = x + 1

def ex2():
    fora = 5
    x=0
    while fora > 0:
        dentro = 0
        while dentro < fora:
            x = x + 1
            print(x, end=": ")
            print("oi")
            dentro = dentro + 1
        fora = fora - 1

def tabuada1():
    tab = 0
    while tab < 10:
        tab = tab + 1
        i = 0
        while i < 10:
            i = i + 1
            print(tab,"x",i,"=",tab*i)
        print()

def tabuada2():
    tab = 1
    while tab <= 10:
        print("Tabuada do", tab, ":", end="\t")
        i = 1
        while i <= 10:
            print(tab*i, end = "\t")
            i = i + 1
        print()
        tab = tab + 1

def tabuada3():
    tab = 1
    while tab <= 10:
        i = 1
        while i <= 10:
            print(tab,"x",i,"=",tab*i)
            i = i + 1
        tab = tab + 1
        print()


def loop1():
    x = 2
    cont = 0
    while x >= 0:
        print(x)
        y = 0
        while y <= 4:
            print("cont=",cont)
            cont = cont + 1
            print(y)
            y = y - 1
        x = x - 1

def ex6():
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            print(3 * i + j + 1, end=" ")
            j = j + 1
        i = i + 1

def fatorial(n):
    x = n
    fat = 1
    while n >= 1:
        fat = fat * n
        n = n - 1
    return fat


def perguntaFAT():
    n=int(input("Digite um número: "))
    while n != 0:
        print(fatorial(n))
        n=int(input("Digite um número: "))

def FatoresPrimos():
    n = int(input("Digite um número inteiro >1: "))
    fator = 2
    multiplicidade = 0

    while n > 1:
        while n % fator == 0:
            multiplicidade = multiplicidade + 1
            n = n / fator
        if multiplicidade > 0:
            print("fator", fator, "multiplicidade =", multiplicidade)
        fator = fator + 1
        multiplicidade = 0

def ehPrimo(n):
    i = n
    x = 0
    while i > 1:
        if (n % i) == 0:
            x = x + 1
        i = i - 1
    if x == 1:
        return "primo"
    else:
        return "não primo"

def éPrimo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

print(éPrimo(2))