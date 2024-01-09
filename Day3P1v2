f = open("input2.txt", "r")
line1 = f.readline()[:-1]
line2 = f.readline()[:-1]
line3 = f.readline()[:-1]

total = 0
temp = 0

print([line1,line2,line3])
def getNum(ind, curLine):
    num = curLine[ind]
    ind = ind + 1
    
    while curLine[ind].isnumeric() == True:
        num = num + curLine[ind]
        ind = ind + 1
    return(num)

def checkPos(ind, num):
    for i in range(ind-1,ind+len(num)+1):
        print(line2[i])
        #print(line1[i],end='')
        #print(line2[i],end='')
        #print(line3[i],end='')

        print([num, line1[i]])
        if line1[i] != '.' and line1[i].isnumeric() == False:
            return True
        
        print([num, line3[i]])
        if line3[i] != '.' and line3[i].isnumeric() == False:
            return True
            
    if line2[ind-1] != '.' and line2[ind-1].isnumeric() == False:
            return True
    if line2[ind+len(num)] != '.' and line2[ind+len(num)].isnumeric() == False:
            return True 
    return False
    
skip = 0

for ind, val in enumerate(line2):
    if val.isnumeric() == True and skip == 0:
        temp = getNum(ind,line2)
        
        if checkPos(ind, temp) == True:
          
            total = total + int(temp)
            print(['total',total])
            skip = len(temp)
    
    if skip > 0:
        skip = skip - 1
        
    #ind = ind + len(str(temp))
print(total)
