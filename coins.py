import random
flips=[]
numflips=int(input("How many flips"))
c=0
r=[]
hr=0
tr=0
for i in range(0,numflips):
    flips.append(random.randint(0,1))
    
for j in range(0,len(flips)):
    c+=flips[j]
    if(flips[j]==flips[j-1]):
        if(flips[j]==0):
            tr+=1
        else:
            hr+=1
print(f"heads:{c} {100*c/numflips}")
print(f"tails:{numflips-c} {100*(numflips-c)/numflips}")
print(f"{hr} runs of Heads")
print(f"{tr} runs of Tails")