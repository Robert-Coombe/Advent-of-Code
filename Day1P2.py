f = open("input.txt", "r")
line = f.readline()

n = [[3,'one','1'],[3,'two','2'],[5,'three','3'],[4,'four','4'],[4,'five','5'],[3,'six','6'],[5,'seven','7'],[5,'eight','8'],[4,'nine','9']]
total = 0

def checkList():
    for num in n:
        if line[start:start+num[0]] == num[1]:
            return(num[2])
            
    return(None)

while line != '':
    num1 = None
    num2 = None
    end = len(line)
    
    start = 0
    while num1 == None and start < end:
        if line[start].isnumeric() == True:
            num1 = line[start]
            break
    
        num1 = checkList()
    
        start = start +1
    
    start = 0
    while start < end:
        if line[start].isnumeric() == True:
            num2 = line[start]
    
        temp = checkList()
    
        if temp != None:
            num2 = temp
    
        start = start +1
        
    total = total + int(num1+num2)
    line = f.readline()
    
print(total)
