'''interface = [[0 for x in range(25)]for x in range(13)]

interface[0][0] = "+"

for a in range(1,7):
    interface[a][0] = "|"
    interface[0][a] = "-"
    #for b in range(1,7):
       # interface[a][b] = "-"
                                        ERROERROERROERROERROERROERRO
for a in range(8,15):
    #interface[a][0] = "|"
    interface[0][a] = "-"

for a in range(16,23):
    #interface[a][0] = "|"
    interface[0][a] = "-"


for a in range(0,25):
    print(interface[a])'''
num = 1
linha1 = []
linh_num = []
tab2 = [[0 for x in range(25)]for x in range(3)]

for a in range(0,25,8):
    tab2[0][a] = "|"
    tab2[1][a] = "|"
    tab2[2][a] = "|"

linha1 = tab2[0]
linha_num = linha1[:]

for a in range(4,len(linha1),8):
    linha_num[a] = num
    num += 1

'''print(linha1)
print()
print(linha_num)'''


'''print(linha1)
print(linha_num)
print(linha1)'''



l1 = str(linha1)
ln = str(linha_num)

l1 = l1.replace("0, ", " ")
ln = ln.replace("0, ", " ")

l1 = l1.replace("'|'","|")
ln = ln.replace("'|'","|")

l1 = l1.replace("|,","|")
ln = ln.replace("|,","|")

l1 = l1.replace(",","")
ln = ln.replace(",","")

l1 = l1.replace("]","")
ln = ln.replace("]","")

l1 = l1.replace("[","")
ln = ln.replace("[","")


print(l1)
print(ln)
print(l1)

 #                                       ERROERROERROERROERROERROERRO