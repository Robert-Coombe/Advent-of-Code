f = open("input.txt", "r")
line1 = '.'+f.readline()[:-1]+'.'
line2 = '.'+f.readline()[:-1]+'.'
line3 = '.'+f.readline()[:-1]+'.'

def checkPos(ind):
    numList = []
    if line1[ind].isnumeric() == True:
        numList.append([line1,ind])
    else:
        if line1[ind-1].isnumeric() == True:
            numList.append([line1,ind-1])
        if line1[ind+1].isnumeric() == True:
            numList.append([line1,ind+1])
    
    if line2[ind-1].isnumeric() == True:
        numList.append([line2,ind-1])
    if line2[ind+1].isnumeric() == True:
        numList.append([line2,ind+1])

    if line3[ind].isnumeric() == True:
        numList.append([line3,ind])
    else:
        if line3[ind-1].isnumeric() == True:
            numList.append([line3,ind-1])
        if line3[ind+1].isnumeric() == True:
            numList.append([line3,ind+1])

    return(numList)

def getNums(nums):
    gearNums = []
    
    for n in nums:
        line = n[0]
        lineNum = line[n[1]]
        if line[n[1]-1].isnumeric() == True:
            lineNum = line[n[1]-1] + lineNum
            if line[n[1]-2].isnumeric() == True:
                lineNum = line[n[1]-2] + lineNum
                
        if line[n[1]+1].isnumeric() == True:
            lineNum = lineNum + line[n[1]+1]
            if line[n[1]+2].isnumeric() == True:
                lineNum = lineNum + line[n[1]+2]
            
        gearNums.append(lineNum)

    return(gearNums)

total = 0

for i in range(140):
    for ind, val in enumerate(line2):
        if val == '*':
            numList = checkPos(ind)
            if len(numList) == 2:
                gearNums = getNums(numList)
                total = total + (int(gearNums[0]) * int(gearNums[1]))

    line1 = line2
    line2 = line3
    line3 = '.'+f.readline()[:-1]+'.'

print(total)
