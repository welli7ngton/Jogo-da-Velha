
def interfacetabuleiro():

    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9","O", "X"]
    linha1 = ("+"+("-------+"*3))
    linha2 = ("|"+(" "*7)+"|"+(" "*7)+"|"+(" "*7)+"|")
    linha3 = ("|"+(" "*3)+num[0]+(" "*3)+"|"+(" "*3)+num[1]+(" "*3)+"|"+(" "*3)+num[2]+(" "*3)+"|")

    print(linha1)
    for a in range(0,3):
        if a == 1:
            linha3 = ("|"+(" "*3)+num[3]+(" "*3)+"|"+(" "*3)+num[4]+(" "*3)+"|"+(" "*3)+num[5]+(" "*3)+"|")
        elif a == 2:
            linha3 = ("|"+(" "*3)+num[6]+(" "*3)+"|"+(" "*3)+num[7]+(" "*3)+"|"+(" "*3)+num[8]+(" "*3)+"|")        
        print(linha2)
        print(linha3)
        print(linha2)
        print(linha1)

interfacetabuleiro()
