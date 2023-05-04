import random

tabuleiro = [[0 for x in range(3)]for x in range(3)]

tabuleiro[1][1] = "X"
l = ["5"]



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
    global l

    if movimento in l:

        return False
    else:
        l.append(movimento)
        return True

def movimentação(tabuleiro,movimento,tip):

    global l1
    global l2
    global l3

    if str(movimento) in "123":
        if str(movimento) == "1":
            l1 = l1.replace("1", tip)
        elif str(movimento) == "2":
            l1 = l1.replace("2", tip)
        elif str(movimento) == "3":
            l1 = l1.replace("3", tip)

    elif str(movimento) in "456":
        if str(movimento) == "4":
            l2 = l2.replace("4", tip)
        elif str(movimento) == "5":
            l2 = l2.replace("5", tip)
        elif str(movimento) == "6":
            l2 = l2.replace("6", tip)

    elif str(movimento) in "789":
        if str(movimento) == "7":
            l3 = l3.replace("7", tip)
        elif str(movimento) == "8":
            l3 = l3.replace("8", tip)
        elif str(movimento) == "9":
            l3 = l3.replace("9", tip)
   
    return tabuleiro

def verifica_vitoria(tipo):
    
    global l1
    global l2
    global l3

    #verificação horizontal
    if l1[4] == tipo and l1[12] == tipo and l1[20] == tipo:
        return True
    elif l2[4] == tipo and l2[12] == tipo and l2[20] == tipo:
        return True
    elif l3[4] == tipo and l3[12] == tipo and l3[20] == tipo:
        return True
    else:
        return False
    
    #verificação vertical
    if l1[4] == tipo and l2[4] == tipo and l3[4] == tipo:
        return True
    elif l1[12] == tipo and l2[12] == tipo and l3[12] == tipo:
        return True
    elif l1[20] == tipo and l2[20] == tipo and l3[20] == tipo:
        return True
    else:
        return False

    #verificação diagonal
    if l1[4] == tipo and l2[12] == tipo and l3[20] == tipo:
        return True
    elif l1[20] == tipo and l2[12] == tipo and l3[4] == tipo:
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
                print("0000000000000000000000000")
                break
            
            
    if i > 1 and i %2 == 0:
        t = "O"
        resultado = verifica_vitoria(t)
        if resultado == True:
            print("voce venceu")
            break
    
    elif i > 1 and i %2 != 0:
        t = "X"
        resultado = verifica_vitoria(t)
        if resultado == True:
            print("voce perdeu")
            break