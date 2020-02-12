import random
flips=[]
numflips=int(input("How many flips"))
c=0
for i in range(0,numflips):
    flips.append(random.randint(0,1))
    
for j in range(0,len(flips)):
    c+=flips[j]
print(f"heads:{c} {100*c/numflips}")
print(f"tails:{numflips-c} {100*(numflips-c)/numflips}")