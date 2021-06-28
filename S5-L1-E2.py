def eh_primo(n):
    i = n
    x = 0
    while i > 1:
        if (n % i) == 0:
            x = x + 1
        i = i - 1
    return x

def maior_primo(p):
    while eh_primo(p) != 1:
        p = p - 1
    return p