
f = open("input.txt", "r")
nums = ['1','2','3','4','5','6','7','8','9','0']
line = f.readline()
total = 0

for j in range(1000):
    num1 = None
    num2 = None
    
    for ind, val in enumerate(line):
        
        if val in nums:
            if num1 == None:
                num1 = val
            num2 = val
            
    total = total + int(num1+num2)
    line = f.readline()

print(total)
