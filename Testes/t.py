tabuleiro = [[0 for x in range(3)] for x in range(3)]
tabuleiro[1][1] = "X"


def mostra_tabuleiro(tabuleiro):
    print("+-------" * 3 + "+")
    for linha in range(3):
        print("|", end="")
        for coluna in range(3):
            print("       |", end="") if coluna != 2 else print("       |", end="\n")
        print("|", end="")
        for coluna in range(3):
            print("   " + str(tabuleiro[linha][coluna]) + "   |", end="") if coluna != 2 else print("   " + str(tabuleiro[linha][coluna]) + "   |", end="\n")
        print("|", end="")
        for coluna in range(3):
            print("       |", end="") if coluna != 2 else print("       |", end="\n")
        print("+-------" * 3 + "+")

def movimento(tabuleiro):
    ok = False

    while not ok:
        m = input("Digite seu movimento: ")
        ok = len(m) == 1 and m >= "1" and m <= "9"
        
        if not ok:
            print("Movimento inválido, entre com um valor válido: ")
            m = int(m) - 1
            l = m //3 #l inha da matriz
            c = m % 3 # coluna da matriz
            tipo = tabuleiro[l][c]
            ok = tipo not in ["O", "X"]
            if not ok:
                print("Lugar ocupado")
                continue
            tabuleiro[l][c] = "O"
            return(tabuleiro)





mostra_tabuleiro(tabuleiro)
tabuleiro = movimento(tabuleiro)
mostra_tabuleiro(tabuleiro)