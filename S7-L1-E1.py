x = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
largura = x
while altura > 0:
    while largura > 0:
        print("#",end="")
        largura = largura -1
    print()
    largura = x
    altura = altura - 1

