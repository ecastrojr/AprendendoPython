x = int(input("digite a largura: "))
y = int(input("digite a altura: "))
largura = x
altura = y
while altura > 0:
    while largura > 0:
        if largura == x or largura == 1:
            print("#",end="")
        elif altura == y or altura == 1:
            print("#",end="")
        else:
            print(" ",end="")
        largura = largura -1
    print()
    largura = x
    altura = altura - 1

