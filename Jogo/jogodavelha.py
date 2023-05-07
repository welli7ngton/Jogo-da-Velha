import random

import time

# Criando a matriz para o tabuleiro
tabuleiro = [[0 for x in range(3)] for x in range(3)]

# Incluindo "X" na posição (1,1) da matriz como primeira jogada do computador
tabuleiro[1][1] = "X"

# Colocando o caractere 5 na lista de números para não poder ser mais usado
# Essa lista será usada em uma função para não repedir jogadas
numeros = ["5"]

# Criando as linhas alteraveis da inferface do jogo
l1 = "|"+(" "*3)+"1"+(" "*3)+"|"+(" "*3)+"2"+(" "*3)+"|"+(" "*3)+"3"+(" "*3)+"|"
l2 = "|"+(" "*3)+"4"+(" "*3)+"|"+(" "*3)+"X"+(" "*3)+"|"+(" "*3)+"6"+(" "*3)+"|"
l3 = "|"+(" "*3)+"7"+(" "*3)+"|"+(" "*3)+"8"+(" "*3)+"|"+(" "*3)+"9"+(" "*3)+"|"

# Função pra printar a interface atualizada
def interfacetabuleiro(tabuleiro):

    global l1,l2,l3

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

# Função para verificar se o movimento é válido
def verifica_movimento(movimento):
    global numeros
    # A lógica é basica, se o movimento ja estiver na lista numeros retorna falso
    # senão numeros recebe o movimento e retorna true
    if movimento in numeros:
        return False
    else:
        numeros.append(movimento)
        return True

# Função para alterar a matriz do jogo e as linhas alteraveis da interface
def movimentação(tabuleiro, movimento, tip):
    # Altera a matriz de acordo com o numero digitado pelo jogador ou pelo pc
    global l1,l2,l3
    # l para linha e c para coluna
    l, c = 0, 0

    # tip é o tipo de signo, X ou O
    if movimento == "1":
        l, c = 0, 0
        l1 = l1.replace("1", tip)
    elif movimento == "2":
        l, c = 0, 1
        l1 = l1.replace("2", tip)
    elif movimento == "3":
        l, c = 0, 2
        l1 = l1.replace("3", tip)
    elif movimento == "4":
        l, c = 1, 0
        l2 = l2.replace("4", tip)
    elif movimento == "5":
        l, c = 1, 1
        l2 = l2.replace("5", tip)
    elif movimento == "6":
        l, c = 1, 2
        l2 = l2.replace("6", tip)
    elif movimento == "7":
        l, c = 2, 0
        l3 = l3.replace("7", tip)
    elif movimento == "8":
        l, c = 2, 1
        l3 = l3.replace("8", tip)
    elif movimento == "9":
        l, c = 2, 2
        l3 = l3.replace("9", tip)
    tabuleiro[l][c] = tip

    return tabuleiro

# Função para verificar a vitoria de X ou O
def verifica_vitoria(tabuleiro, t):

    if t == "X":
                            # Verificação se X ganhou
        # verifica linha                    
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == "X":
            return True
        elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == "X":
            return True
        elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == "X":
            return True

        # verifica colunas
        if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == "X":
            return True
        elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == "X":
            return True
        elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == "X":
            return True


        #verifica diagonais
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "X":
            return True
        elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "X":
            return True

        else:
            return False

    else:

                            # Verificação se O ganhou        
        # verifica linhas
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == "O":
            return True
        elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == "O":
            return True
        elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == "O":
            return True

        # verifica colunas
        if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == "O":
            return True
        elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == "O":
            return True
        elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == "O":
            return True

        # verifca diagonais
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "O":
            return True
        elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "O":
            return True 
            
        else:
            return False       

# Chamada da função para mostrar a interface depois da primeira jogada com X já na posição (1,1)  
interfacetabuleiro(tabuleiro)


# for para indicar as rodadas do jogo, de 0 à 8 pois o computador sempre começa na posição (1,1)(vou mudar isso 
# futuramente)
for i in range(0,8):
    # Se i estiver presente em "02468" quer dizer que é a vez do jogador
    if str(i) in "02468":
        # tO é a variavel pra definir qual é o signo 
        tO = "O"

        # while que só encerra quando o movimento é válido, se ja tiver um X ou O no campo digitado o while não 
        # acaba e pede pro digitar um movimento válido
        while True:

            # variável para verificar se o movimento é válido ou não
            okounao = None

            move = str(input("Digite seu movimento: "))

            okounao = verifica_movimento(move)

            if okounao == True:
                interfacetabuleiro(movimentação(tabuleiro, move,tO))
                
                break
            else:
                print("movimento inválido")

        #verificação de resultado
        resultado = verifica_vitoria(tabuleiro, tO)
        if resultado == True:
            print("voce venceu")
            break 
        elif len(numeros) == 9:
            print("empate.")
            break                                    
    # Se i estiver presente em "13579" quer dizer que é a vez do jogador
    elif str(i) in "13579":
        # tX é a variavel pra definir qual é o signo
        tX = "X"
        # Mesmo bloco de código para verificar se o movimento do pc é válido
        while True:
            okounao = None

            num = random.randrange(1,10)


            
            move = str(num)
            okounao = verifica_movimento(move)
            if okounao == True:
                print("Aguradando jogada do jogador 'X'...")
                time.sleep(2)               
                interfacetabuleiro(movimentação(tabuleiro, move,tX)) 
                break

        #verificação de resultado    
        resultado = verifica_vitoria(tabuleiro, tX)
        if resultado == True:
            print("voce perdeu")
            break    
        elif len(numeros) == 9 and tabuleiro[:][:]!= "0":
            print("empate.")
            break 
