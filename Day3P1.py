f = open("input.txt", "r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()

total = 0
temp = 0

def getNum(ind, curLine):
    num = curLine[ind]
    ind = ind + 1
    
    while curLine[ind].isnumeric() == True:
        num = num + curLine[ind]
        ind = ind + 1
    return(num)

def checkPos(ind, num):
    for i in range(ind-1,ind+len(num)):
        if line1[i] != '.' and line1[i] != '\n' and line1[i].isnumeric() == False:
            return True
        if line3[i] != '.' and line3[i] != '\n' and line3[i].isnumeric() == False:
            return True
    if line2[ind-1] != '.' and line2[ind-1] != '\n' and line2[ind-1].isnumeric() == False:
            return True
    if line2[ind+len(num)] != '.' and line2[ind+len(num)] != '\n' and line2[ind+len(num)].isnumeric() == False:
            return True 
    return False
    
for ind, val in enumerate(line2):
    if val.isnumeric() == True:
        temp = getNum(ind,line2)
        if checkPos(ind, temp) == True:
            total = total + int(temp)
    #ind = ind + len(str(temp))
        
