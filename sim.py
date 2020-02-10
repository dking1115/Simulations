import random
vals=[]
outof=6
rolls=int(input("howmany rolls"))
for roll in range(0,rolls):
    vals.append(random.randint(1,outof))
for i in range(1,outof+1):
    c=0
    for j in range(0,len(vals)):
        if(vals[j]==i):
            c+=1
    print(f"{i}:{c}/{rolls}={100*(c/rolls)}%")