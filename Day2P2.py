import re

f = open("input.txt", "r")
line = f.readline()

total = 0

for n in range(100):
    greenMatches = re.findall("[0-9]+\sgreen+", line)
    redMatches = re.findall("[0-9]+\sred+", line)
    blueMatches = re.findall("[0-9]+\sblue+", line)
    
    gMax = 0
    bMax = 0
    rMax = 0

    for g in greenMatches:
        if int(g[:-6]) > gMax:
            gMax = int(g[:-6])
            
    for r in redMatches:
        if int(r[:-4]) > rMax:
            rMax = int(r[:-4])
            
    for b in blueMatches:
        if int(b[:-5]) > bMax:
            bMax = int(b[:-5])
 
    total = total + (gMax*bMax*rMax)
    line = f.readline()

print(total)
