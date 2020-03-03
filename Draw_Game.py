import pygame
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
suits=["Spades","Hearts","Diamonds","Clubs"]
suitss=["♠","♥","♦","♣"]
faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
facess = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
def suitf (card):
    for i in range(len(suitss)):
        if suitss[i] in str(card):
            suit=suits[i]
    return(suit)
    
def facef (card):
    face=""
    for i in range(len(faces)):
        if faces[i] in str(card):
            face=facess[i]
    return(face)

def draw_card(w,h,x,y,card,screen):
    rect=pygame.Rect(x,y,w,h)
    pygame.draw.rect(screen,WHITE,rect)
    font = pygame.font.Font(None, int(w/5))
    face=facef(card)
    suit=suitf(card)
    text = font.render(f"{face} of {suit}", True,RED,WHITE)
    textRect = text.get_rect()
    textRect.center = (x+(w/2),y+(h/2))
    screen.blit(text, textRect)
    