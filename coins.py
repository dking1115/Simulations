import random
flips=[]
numflips=int(input("How many flips"))
c=0
r=[]
hr=0
tr=0
run=0
ser=int(input("Which side are you looking for (0-heads, 1-tails)?"))
numrun=int(input("How long is the run you're looking for?"))
for i in range(0,numflips):
    flips.append(random.randint(0,1))
    
for j in range(0,len(flips)):
    c+=flips[j]
    if(j>numrun-1):
        ru=0
        for g in range(j-numrun,j):
            if(flips[g]==ser):
                ru+=1
            if(ru>=numrun):
                run+=1
print(f"heads:{c} {100*c/numflips}")
print(f"tails:{numflips-c} {100*(numflips-c)/numflips}")
print(f"{run} runs of {numrun}")