import random

tabuleiro = [[0 for x in range(3)]for x in range(3)]

tabuleiro[1][1] = "X"


num = ["1", "2", "3", "4", "5", "6", "7", "8", "9","O", "X"]

l1 = "|"+(" "*3)+num[0]+(" "*3)+"|"+(" "*3)+num[1]+(" "*3)+"|"+(" "*3)+num[2]+(" "*3)+"|"
l2 = "|"+(" "*3)+num[3]+(" "*3)+"|"+(" "*3)+num[10]+(" "*3)+"|"+(" "*3)+num[5]+(" "*3)+"|"
l3 = "|"+(" "*3)+num[6]+(" "*3)+"|"+(" "*3)+num[7]+(" "*3)+"|"+(" "*3)+num[8]+(" "*3)+"|"



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

    if movimento >= 1 and movimento < 10:
        return True
    else: 
        return False




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
    if l1[4] == tipo and l1[12] == tipo or l1[20] == tipo:
        return True
    elif l2[4] == tipo and l2[12] == tipo or l2[20] == tipo:
        return True
    elif l3[4] == tipo and l3[12] == tipo or l3[20] == tipo:
        return True
    
    #verificação vertical
    elif l1[4] == tipo and l2[4] == tipo and l3[4] == tipo:
        return True
    elif l1[12] == tipo and l2[12] == tipo and l3[12] == tipo:
        return True
    elif l1[20] == tipo and l2[20] == tipo and l3[20] == tipo:
        return True

    #verificação diagonal
    elif l1[4] == tipo and l2[12] == tipo and l3[20] == tipo:
        return True
    elif l1[20] == tipo and l2[12] == tipo and l3[4] == tipo:
        return True    
    else:
        return False
    







interfacetabuleiro(tabuleiro)
texto = ""
for i in range(0,8):
    if str(i) in "02468":
        tO = "0"
        move = input("Digite seu movimento: ")
        interfacetabuleiro(movimentação(tabuleiro, move,tO))
    if str(i) in "1357":
        tX = "X"
        numpc = None
        while numpc is None:
            num = random.randrange(1,8)
            if num %2 != 0:
                numpc = num
        move = num
        interfacetabuleiro(movimentação(tabuleiro, move,tX)) 
    
    if i %2 == 0:
        t = "O"
        resultado = verifica_vitoria(t)
        if resultado == True:
            print("voce venceu")
            break
    
    else:
        t = "X"
        resultado = verifica_vitoria(t)
        if resultado == True:
            print("voce perdeu")
            break

print(   )
print(   )
print(   )
print("ultimo tabuleiro")
interfacetabuleiro(tabuleiro)        