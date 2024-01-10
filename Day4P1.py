f = open("input2.txt", "r")
line = f.readline()

total = 0

def getScoreOld(winNums, ourNums):
    power = -1
    
    for n in ourNums:
        if n in winNums:
            power = power + 1
    
    if power >= 0:
        return(pow(2,power))
    else:
        return(0)

def getScore(winNums, ourNums):
    power = -1
    
    for ind1, val1 in enumerate(winNums):
        for ind2, val2 in enumerate(ourNums):
            if val2 == val1:
                winNums[ind1] = ''
                ourNums[ind2] = ''
                power = power+1
                break
    
    if power >= 0:
        return(pow(2,power))
    else:
        return(0)

for i in range(6):
    
    winNums = []
    ourNums = []
    temp = ''
    
    for ind, val in enumerate(line[7:]):
        
        if val.isnumeric() == True:
            if temp.isnumeric() == True:
                temp = temp + val
                ourNums.append(temp)
                temp = ''

            else:
                temp = val
                
        elif (val == ' ' or val == '\n') and temp.isnumeric() == True:
            ourNums.append(temp)
            temp = ''
                
        if val == '|':
            winNums = ourNums
            ourNums = []
    
    #print([winNums,ourNums, getScore(winNums,ourNums)])
            
    total = total + getScore(winNums, ourNums)
    
    line = f.readline()

print(total)
