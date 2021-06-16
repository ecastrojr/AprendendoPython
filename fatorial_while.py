def main():
    n = int(input("Digite o valor de n: "))
    x = n
    i = n - 1   
    while i > 0:
        n = n * i
        i = i - 1
    print("O valor de %d! é %d" %(x, n))

main()