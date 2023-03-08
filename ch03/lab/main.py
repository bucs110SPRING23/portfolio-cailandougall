import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((1470, 1470))
pygame.display.get_window_size()
screensize=1470
print ("Who do you think is going to win: joe or jack?")
myguess=str(input("Enter a player: "))
screen.fill("blue")
pygame.draw.circle(screen, "black", (735, 735), 735)
pygame.draw.circle(screen, "purple", (735, 735), 730)
pygame.draw.line(screen, "black", (735,0), (735,1470))
pygame.draw.line(screen, "black", (0,735), (1470,735))
for i in range (10):
    x1=735
    y1=735
    x2=random.randrange (0, screensize)
    y2=random.randrange (0, screensize)
    joe=(x2,y2)
    distance_from_center = math.hypot(x1-x2, y1-y2)
    is_in_circle = distance_from_center <= 735
    if is_in_circle:
        pygame.draw.circle(screen, "green", (x2, y2), 5)
    else:
        pygame.draw.circle(screen, "orange", (x2, y2), 5)
for i in range (10):
    x1=735
    y1=735
    x3=random.randrange (0, screensize)
    y3=random.randrange (0, screensize)
    jack=(x3,y3)
    distance_from_center = math.hypot(x1-x3, y1-y3)
    is_in_circle = distance_from_center <= 735
    if is_in_circle:
        pygame.draw.circle(screen, "yellow", (x3, y3), 5)
    else:
        pygame.draw.circle(screen, "orange", (x3, y3), 5)
pygame.display.flip()
pygame.time.wait (10000)
