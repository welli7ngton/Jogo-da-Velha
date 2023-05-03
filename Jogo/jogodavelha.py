from random import randrange

tabuleiro = [[0 for x in range(3)]for x in range(3)]

tabuleiro[1][1] = "X"

def interfacetabuleiro(tabuleiro):

    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9","O", "X"]   
    linha3 = ("|"+(" "*3)+num[0]+(" "*3)+"|"+(" "*3)+num[1]+(" "*3)+"|"+(" "*3)+num[2]+(" "*3)+"|")

    print("+"+("-------+"*3))

    for a in range(0,3):

        print("|"+(" "*7)+"|"+(" "*7)+"|"+(" "*7)+"|")
        if a == 0:
            print("|"+(" "*3)+num[0]+(" "*3)+"|"+(" "*3)+num[1]+(" "*3)+"|"+(" "*3)+num[2]+(" "*3)+"|") 
        elif a == 1:
            print("|"+(" "*3)+num[3]+(" "*3)+"|"+(" "*3)+num[10]+(" "*3)+"|"+(" "*3)+num[5]+(" "*3)+"|")
        elif a == 2:
            print("|"+(" "*3)+num[6]+(" "*3)+"|"+(" "*3)+num[7]+(" "*3)+"|"+(" "*3)+num[8]+(" "*3)+"|")        
        
        print("|"+(" "*7)+"|"+(" "*7)+"|"+(" "*7)+"|")
        print("+"+("-------+"*3))











interfacetabuleiro(tabuleiro)