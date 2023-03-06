import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((1470, 1470))
screen.fill("blue")
screensize=1470
width, height=pygame.display.get_window_size()
hit_box_width=width/2
hit_box_height=height/2

hitboxes = {
 "yellow": pygame.Rect(0,0, hit_box_width, hit_box_height),
 "green": pygame.Rect(0,0, hit_box_width, hit_box_height),
}

hitboxes["green"].topleft = hitboxes["yellow"].topright
main_colors = {
 "yellow": (200, 200, 0),
 "green": (0, 200, 0),
}
highlight_colors = {
 "yellow": (255, 255, 0),
 "green": (0, 255, 0),
}
font=pygame.font.SysFont("Times New Roman", 12)
text = font.render("Who do you think is going to win?: Player yellow or Player green?", True, "white")
text = font.render("Please click a box", True, "white")
screen.blit(text, (0,0)) 
pygame.display.flip()
pygame.time.wait(250)
my_guess=""
while my_guess=="":
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if hitboxes["green"].collidepoint(event.pos):
                my_guess="green"
            if hitboxes["yellow"].collidepoint(event.pos):
                my_guess="yellow"
pygame.draw.circle(screen, "black", (735, 735), 735)
pygame.draw.circle(screen, "purple", (735, 735), 730)
pygame.draw.line(screen, "black", (735,0), (735,1470))
pygame.draw.line(screen, "black", (0,735), (1470,735))
player_green_score=0
player_yellow_score=0
for i in range(10):
    x1=735
    y1=735
    x2=random.randrange (0, screensize)
    y2=random.randrange (0, screensize)
    player_green=(x2,y2)
    distance_from_center = math.hypot(x1-x2, y1-y2)
    is_in_circle = distance_from_center <= 735
    if is_in_circle:
        pygame.draw.circle(screen, "green", (x2, y2), 5)
        player_green_score+=1
    else:
        pygame.draw.circle(screen, "orange", (x2, y2), 5)
    x3=random.randrange (0, screensize)
    y3=random.randrange (0, screensize)
    player_yellow=(x3,y3)
    distance_from_center = math.hypot(x1-x3, y1-y3)
    is_in_circle = distance_from_center <= 735
    if is_in_circle:
        pygame.draw.circle(screen, "yellow", (x3, y3), 5)
        player_yellow_score+=1
    else:
        pygame.draw.circle(screen, "orange", (x3, y3), 5)
pygame.display.flip()
pygame.time.wait(250) 
for c, hb in hitboxes.items():
    pygame.draw.rect(screen, main_colors[c], hb)
if player_green_score<player_yellow_score:
    winner="yellow"
    if my_guess==winner:
        font = pygame.font.SysFont("Times New Roman", 24)
        msg=("You were right! Player yellow won and they scored " + str(player_yellow_score) + " points!")
        text = font.render(msg, True, "white")
        screen.blit(text, (0,0)) 
    elif my_guess!=winner:
        font = pygame.font.SysFont("Times New Roman", 24)
        msg=("Um, not quite...Player yellow won and they scored " + str(player_yellow_score) + " points!")
        text = font.render(msg, True, "white")
        screen.blit(text, (0,0)) 
elif player_yellow_score<player_green_score:
    winner="green"
    if my_guess==winner:
        font = pygame.font.SysFont("Times New Roman", 24)
        msg=("You were right! Player green won and they scored " + str(player_green_score) + " points!")
        text = font.render(msg, True, "white")
        screen.blit(text, (0,0))  
    elif my_guess!=winner:
        font = pygame.font.SysFont("Times New Roman", 24)
        msg=("Oof, that's not it... Player green won and they scored " + str(player_green_score) + " points!")
        text = font.render(msg, True, "white")
        screen.blit(text, (0,0))  
elif player_yellow_score==player_green_score:
    font = pygame.font.SysFont("Times New Roman", 24)
    msg=("It's a tie! They both scored " + str(player_yellow_score) + " points!")
    text = font.render(msg, True, "white")
    screen.blit(text, (0,0))  
pygame.display.flip()
pygame.time.wait (10000)