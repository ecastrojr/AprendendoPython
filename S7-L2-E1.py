def n_primos(n):
    i = n
    x = 0
    count = 0
    while n > 0:
        while i > 1:
            if (n % i) == 0:
                x = x + 1
            i = i - 1
        if x == 1:
            count = count + 1
        x = 0
        n = n - 1
        i = n
    return count

print(n_primos(121))