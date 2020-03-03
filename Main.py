from Deck import Deck
import random
import sys
import pygame
import time
from Draw_Game import draw_card
size = [800, 400]
screen = pygame.display.set_mode(size)
def shuffle(cards,discard):
        for q in discard:
            cards.append(q)
        discard=[]
        n = len(cards)
        for i in range(n-1,0,-1): 
            j = random.randint(0,i) 
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

def disp(stack):
    screen.fill(GREEN)
    for g in range(len(stack)):
        draw_card((size[0]/(len(stack)+1)),100,(10+(size[0]/(len(stack)+1))*g),10,stack[g],screen)
    pygame.display.flip()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
decks=[]
car=[]
on_table=[]
num_decks=1
order=[1,0,1,0,1,0,1,4,3,0,1,0,1,0,1,0,1,0,1]
dis=[]
pygame.init()
pygame.display.set_caption("Card Dealing")

for i in range(num_decks):
    decks.append(Deck())
for i in decks:
    i.shuffle()
    for j in i.cards:
        car.append(j)
car,dis=shuffle(car,dis)
for i in order:
        
    if(i==1):
        print("Deal")
        cars=""
        for g in car:
            cars+=(str(g)+",")
        car,on_table=Deal(car,on_table)
        print("On Table:")
    elif(i==0):
        print("Burn")
        car,dis=Burn(car,dis)
    elif(i==3):
        print("Shuffle")
        car,dis=shuffle(car,dis)
    elif(i==4):
        print("Clear The Table")
        on_table,dis=clear_table(on_table,dis)
    disp(on_table)
done = False
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True
    screen.fill(GREEN)
    disp(on_table)
    car,dis=Burn(car,dis)
    car,on_table=Deal(car,on_table)
    if(len(on_table)>10):
        on_table,dis=clear_table(on_table,dis)
        car,dis=shuffle(car,dis)
    time.sleep(1)
    