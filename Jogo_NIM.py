def computador_escolhe_jogada(n, m):
    if n % (m+1) == 0:
        if m > n:
            return n
        else:
            return m - 1
    else:
        return m

def usuario_escolhe_jogada(n, m):
    x = int(input("Quantas peças você vai tirar? "))
    while x > m:
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        x = int(input("Quantas peças você vai tirar? "))
    return x

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m+1) != 0:
        print("")
        print("Computador começa!")
        print("")
        while n != 0:
            pc = computador_escolhe_jogada(n, m)
            n = n - pc
            print("O computador tirou", pc, " peças.")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "computador"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n," peças no tabuleiro.")
            u = usuario_escolhe_jogada(n, m)
            n = n - u
            print("Voce tirou", u, " peças.")
            if n == 0:
                print("Fim do jogo! O usuario ganhou!")
                return "usuario"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n," peças no tabuleiro.")
    else:
        print("Voce começa!")
        while n != 0:
            u = usuario_escolhe_jogada(n, m)
            n = n - u
            print("Voce tirou", u, " peças.")
            if n == 0:
                print("Fim do jogo! O usuário ganhou!")
                return "usuario"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n," peças no tabuleiro.")
            pc = computador_escolhe_jogada(n, m)
            n = n - pc
            print("O computador tirou", pc, " peças.")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "computador"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n," peças no tabuleiro.")

def campeonato():
    i = 1
    pc = 0
    u = 0
    print("Voce escolheu um campeonato!")
    while i <= 3:
        print("")
        print("**** Rodada", i,"**** ")
        print("")
        i = i + 1
        if partida() == "computador":
            pc = pc + 1
        else:
            u = u + 1
        
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você", u," X", 3," Computador")   
    return u

print("")
print("Bem-vindo ao jogo do NIM! Escolha:")
print("")
print("1 - para jogar uma partida isolada")
t = input("2 - para jogar um campeonato ")
print("")

if t == 1:
    partida()
else:
    campeonato()

