import re

f = open("input.txt", "r")
line = f.readline()

total = 0

for n in range(1,100):
    greenMatches = re.findall("[0-9]+\sgreen+", line)
    redMatches = re.findall("[0-9]+\sred+", line)
    blueMatches = re.findall("[0-9]+\sblue+", line)
    big = False
    
    for g in greenMatches:
        if int(g[:-6]) > 13:
            big = True
            break
    for r in redMatches:
        if int(r[:-4]) > 12:
            big = True
            break
    for b in blueMatches:
        if int(b[:-5]) > 14:
            big = True
            break
    
    if big != True:
        total = total + n
        
    line = f.readline()

print(total)
