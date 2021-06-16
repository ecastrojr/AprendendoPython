def main():
    n = int(input("Digite o valor de n: "))
    k = int(input("Digite o valor de k: "))
    i = 0
    pot = 1
    while i < k:
        pot = pot * n
        i   = i + 1
    print("a potencia é", i)
    print("O valor de %d^%d é %d" %(n, k, pot))

main()