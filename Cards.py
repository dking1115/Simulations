import random
deck =[]
suits=["Spades","Hearts","Diamonds","Clubs"]
cards=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
for i in suits:
    for j in cards:
        deck.append(f"{j} of {i}")

for a in range(len(deck)-2):
    g=random.randint(a,(len(deck)-1))
    b=deck[a]
    deck[a]=deck[g]
    deck[g]=b
print(deck)
    