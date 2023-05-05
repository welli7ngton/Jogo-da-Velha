import random

# Creating the matrix for the board
tabuleiro = [[0 for x in range(3)] for x in range(3)]

# Including "X" in matrix position (1,1) as the computer's first move
tabuleiro[1][1] = "X"

# Putting the character 5 in the list of numbers so it can no longer be used
# This list will be used in a function to not reorder moves
numeros = ["5"]

# Creating the changeable lines of the game interface
l1 = "|"+(" "*3)+"1"+(" "*3)+"|"+(" "*3)+"2"+(" "*3)+"|"+(" "*3)+"3"+(" "*3)+"|"
l2 = "|"+(" "*3)+"4"+(" "*3)+"|"+(" "*3)+"X"+(" "*3)+"|"+(" "*3)+"6"+(" "*3)+"|"
l3 = "|"+(" "*3)+"7"+(" "*3)+"|"+(" "*3)+"8"+(" "*3)+"|"+(" "*3)+"9"+(" "*3)+"|"

# Function to print the updated interface
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

# Function to check if the move is valid
def verifica_movimento(movimento):
    # The logic is basic, if the movement is already in the list of numbers it returns false
    # otherwise numbers receive the movement and return true
    global numeros
    if movimento in numeros:
        return False
    else:
        numeros.append(movimento)
        return True

# Function to change the game matrix and changeable lines of the interface
def movimentação(tabuleiro, movimento, tip):
    # Changes the matrix according to the number entered by the player or the pc
    global l1,l2,l3
    # l for row and c for column
    l, c = 0, 0

    # tip is the type of sign, X or O
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

# Function to check the victory of X or O
def verifica_vitoria(tabuleiro, t):


    if t == "X":
                            # Check if X won
        
        # check line                  
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == "X":
            return True
        elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == "X":
            return True
        elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == "X":
            return True

        
        # check columns
        if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == "X":
            return True
        elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == "X":
            return True
        elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == "X":
            return True


        
        # check diagonals
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "X":
            return True
        elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "X":
            return True

        else:
            return False

    else:
                            # Check if O won       
        # check line
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == "O":
            return True
        elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == "O":
            return True
        elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == "O":
            return True

        # check columns
        if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == "O":
            return True
        elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == "O":
            return True
        elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == "O":
            return True

       # check diagonals
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "O":
            return True
        elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "O":
            return True 
            
        else:
            return False       

# Function call to show the interface after the first move with X already in position (1,1)   
interfacetabuleiro(tabuleiro)

# for to indicate the rounds of the game, from 0 to 8 because the computer always starts at position (1,1)(I'll 
# change that in the future)
for i in range(0,8):
   
    # If i is present in "02468" it means that it is the player's turn
    if str(i) in "02468":
        # tO is the variable to define the sign
        tO = "O"

        # while that only ends when the movement is valid, if there is already an X or O in the typed field, the 
        # while does not ends and asks pro to type a valid movement
        while True:

            # variable to check if the move is valid or not
            okounao = None

            move = str(input("Yor move: "))

            okounao = verifica_movimento(move)

            if okounao == True:
                interfacetabuleiro(movimentação(tabuleiro, move,tO))
                
                break
            else:
                print("Invalid move")
        
        # result check
        resultado = verifica_vitoria(tabuleiro, tO)
        if resultado == True:
            print("You won!")
            break 
        # if the size of numeros is equal to 9 it is a tie
        elif len(numeros) == 9:
            print("Tie.")
            break    

    # If i is present in "13579" it means that it is the player's turn
    elif str(i) in "13579":
        
        # tX is the variable to define what the sign is
        tX = "X"
        
        # Same block of code to check if pc move is valid
        while True:
            okounao = None

            num = random.randrange(1,9)

            move = str(num)
            okounao = verifica_movimento(move)
            if okounao == True:
                interfacetabuleiro(movimentação(tabuleiro, move,tX)) 
                break
        resultado = verifica_vitoria(tabuleiro, tX)
        if resultado == True:
            print("You lost!")
            break    
        elif len(numeros) == 9:
            print("Tie.")
            break         
