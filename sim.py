import random
one=0
two=0
three=0
four=0
five=0
six=0
rolls=int(input("howmany rolls"))
for roll in range(0,rolls):
    num=random.randint(1,6)
    if(num==1):
        one+=1
    elif(num==2):
        two+=1
    elif(num==3):
        three+=1
    elif(num==4):
        four+=1
    elif(num==5):
        five+=1
    elif(num==6):
        six+=1
print(f"1:{one}/{rolls}={100*(one/rolls)}%")
print(f"2:{two}/{rolls}={100*(two/rolls)}%")
print(f"3:{three}/{rolls}={100*(three/rolls)}%")
print(f"4:{four}/{rolls}={100*(four/rolls)}%")
print(f"5:{five}/{rolls}={100*(five/rolls)}%")
print(f"6:{six}/{rolls}={100*(six/rolls)}%")