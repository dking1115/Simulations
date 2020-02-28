from Deck import Deck
import random
import sys
def shuffle(cards,discard):
        for q in discard:
            cards.append(q)
        n = len(cards)
        for i in range(n-1,0,-1): 
            j = random.randint(0,i+1) 
            c=cards[i]
            cards[i]=cards[j]
            cards[j]=c
            #cards[i],cards[j] = cards[j],cards[i]
        return(cards,discard)
def Deal(deck,tab):
    tab.append(deck[0])
    del deck[0]
    return deck,tab
def Burn(deck,discard):
    discard.append(deck[0])
    del deck[0]
    return(deck,discard)
def clear_table(tab,dis):
    for h in tab:
        dis.append(h)
    tab=[]
    return(tab,dis)

decks=[]
car=[]
on_table=[]
num_decks=1
order=[1,0,1,0,1,0,1,4,3,0,1,0,1,0,1,0,1,0,1,4,3]
dis=[]
for i in range(num_decks):
    decks.append(Deck())
for i in decks:
    i.shuffle()
    for j in i.cards:
        car.append(str(j))
car,dis=shuffle(car,dis)
for i in order:
    if(i==1):
        print("Deal")
        car,on_table=Deal(car,on_table)
        print(f"On Table{on_table}")
    elif(i==0):
        print("Burn")
        car,dis=Burn(car,dis)
    elif(i==3):
        print("Shuffle")
        car,dis=shuffle(car,dis)
    elif(i==4):
        print("Clear The Table")
        on_table,dis=clear_table(on_table,dis)