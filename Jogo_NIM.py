def computador_escolhe_jogada(n, m):
    #x = input("")
    if n % (m+1) == 0:
        if m > n:
            return n
        else:
            return m
    else:
        if m  > n:
            return n
        else:
            return n % (m+1)

def usuario_escolhe_jogada(n, m):
    x = int(input("Quantas peças você vai tirar? "))
    while (x <= 0 or x > m):
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        x = int(input("Quantas peças você vai tirar? "))
    return x

def partida():
    n = int(input("Quantas peças? "))
    while n < 0:
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m < 0 or m > n:
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        m = int(input("Limite de peças por jogada? "))
    if n % (m+1) != 0:
        print("")
        print("Computador começa!")
        print("")
        while n != 0:
            pc = computador_escolhe_jogada(n, m)
            n = n - pc
            if pc == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", pc, " peças.")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "computador"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
                print("")
            else:
                print("Agora restam",n,"peças no tabuleiro.")
                print("")
            u = usuario_escolhe_jogada(n, m)
            n = n - u
            print("")
            if u == 1:
                print("Voce tirou uma peça.")
            else:
                print("Voce tirou", u, "peças.")
            if u == 0:
                print("Fim do jogo! O usuario ganhou!")
                return "usuario"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
                print("")
            else:
                print("Agora restam", n,"peças no tabuleiro.")
                print("")
    else:
        print("")
        print("Voce começa!")
        print("")
        while n != 0:
            u = usuario_escolhe_jogada(n, m)
            n = n - u
            if u == 1:
                print("Voce tirou uma peça.")
            else:
                print("Voce tirou", u, "peças.")
            if n == 0:
                print("Fim do jogo! O usuário ganhou!")
                return "usuario"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
                print("")
            else:
                print("Agora restam", n,"peças no tabuleiro.")
                print("")
            pc = computador_escolhe_jogada(n, m)
            n = n - pc
            if pc == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", pc, "peças.")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "computador"
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n,"peças no tabuleiro.")

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
    print("Placar: Você",u," X",pc," Computador")
    print("") 
    return u

def inicio():        
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

def teste():
    print(usuario_escolhe_jogada(5,3))
    print(usuario_escolhe_jogada(5,3))
    print(usuario_escolhe_jogada(3,5))
    print(usuario_escolhe_jogada(3,5))
    print(computador_escolhe_jogada(13,4))
    print(computador_escolhe_jogada(11,4))
    print(computador_escolhe_jogada(6,2))
    print(computador_escolhe_jogada(4,1))
    print(computador_escolhe_jogada(15,4))

inicio()