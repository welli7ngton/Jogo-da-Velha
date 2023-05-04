import random

tabuleiro = [[0 for x in range(3)] for x in range(3)]

tabuleiro[1][1] = "X"
numeros = ["5"]

l1 = "|"+(" "*3)+"1"+(" "*3)+"|"+(" "*3)+"2"+(" "*3)+"|"+(" "*3)+"3"+(" "*3)+"|"
l2 = "|"+(" "*3)+"4"+(" "*3)+"|"+(" "*3)+"X"+(" "*3)+"|"+(" "*3)+"6"+(" "*3)+"|"
l3 = "|"+(" "*3)+"7"+(" "*3)+"|"+(" "*3)+"8"+(" "*3)+"|"+(" "*3)+"9"+(" "*3)+"|"


def interfacetabuleiro(tabuleiro):
    print("+"+("-------+"*3))
    for a in range(0,3):
        print("|"+(" "*7)+"|"+(" "*7)+"|"+(" "*7)+"|")
        if a == 0:
            print(l1) 
        elif a == 1:
            print(l2)
        elif a == 2:
            print(l3)        
        print("|"+(" "*7)+"|"+(" "*7)+"|"+(" "*7)+"|")
        print("+"+("-------+"*3))

def verifica_movimento(movimento):
    global numeros
    if movimento in numeros:
        return False
    else:
        numeros.append(movimento)
        return True

def movimentação(tabuleiro, movimento, tip):
    l, c = 0, 0
    if movimento == "1":
        l, c = 0, 0
    elif movimento == "2":
        l, c = 0, 1
    elif movimento == "3":
        l, c = 0, 2
    elif movimento == "4":
        l, c = 1, 0
    elif movimento == "5":
        l, c = 1, 1
    elif movimento == "6":
        l, c = 1, 2
    elif movimento == "7":
        l, c = 2, 0
    elif movimento == "8":
        l, c = 2, 1
    elif movimento == "9":
        l, c = 2, 2
    tabuleiro[l][c] = tip

    return tabuleiro

def verifica_vitoria(tabuleiro, t):

    for i in range(3):
        if t == "X":

            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == "X":
                return True
            elif tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == "X":
                return True
            if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "X":
                return True
            elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "X":
                return True
            else:
                return False

        else:

            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == "O":
                return True
            elif tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == "O":
                return True
            if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "O":
                return True
            elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "O":
                return True 
            else:
                return False       

   
interfacetabuleiro(tabuleiro)

for i in range(0,8):

    if str(i) in "02468":
        tO = "O"
        while True:
            move = str(input("Digite seu movimento: "))
            okounao = verifica_movimento(move)
            if okounao == True:
                interfacetabuleiro(movimentação(tabuleiro, move,tO))
                print("1111111111111111111111111")
                for c in range(3):
                    print(tabuleiro[c])
            tipo = "O"
            resultado = verifica_vitoria(tabuleiro, tipo)
            if resultado == True:
                print("voce venceu")
                break                                    

            else:
                print("movimento inválido")
    elif str(i) in "13579":
        tX = "X"
        while True:
            
            while True:
                num = random.randrange(0,9)
                if num %2 != 0:
                    break
            move = str(num)
            okounao = verifica_movimento(move)
            if okounao == True:
                interfacetabuleiro(movimentação(tabuleiro, move,tX)) 

                for b in range(3):
                    print(tabuleiro[b])
                break
        tipo = "X"
        resultado = verifica_vitoria(tabuleiro, tipo)
        if resultado == True:
            print("voce perdeu")
            break    
                  
        elif 0 not in tabuleiro[:][:]:
            print("empate")
            break

for z in range(3):
    print(tabuleiro[z])