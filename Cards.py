import random
def Shuffle(array):
    for a in range(len(array)-2):
        g=random.randint(a,(len(array)-1))
        b=array[a]
        array[a]=array[g]
        array[g]=b
    return(array)
    
deck =[]
suits=["Spades","Hearts","Diamonds","Clubs"]
cards=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
for i in suits:
    for j in cards:
        deck.append(f"{j} of {i}")
for i in range(10):
    deck=Shuffle(deck)
    
for d in deck:
    print(d)