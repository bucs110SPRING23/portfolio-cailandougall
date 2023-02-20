#Part A
import turtle
import random
window=turtle.Screen()
pen1=turtle.Turtle ()
pen2=turtle.Turtle ()
pen1.color ("red")
pen2.color ("blue")
pen1.goto (-100,20)
pen2.goto (-100,-20)
pen1.forward (random.randrange (1,100))
pen2.forward (random.randrange (1,100))
pen1.goto (-100,20)
pen2.goto (-100,-20)
for i in range (1,10):
    pen1.forward (random.randrange(i))
    pen2.forward (random.randrange(i))
pen1.goto (-100,20)
pen2.goto (-100,-20)
window.exitonclick ()

#Part B
import pygame
import math
pygame.init()
window=pygame.display.set_mode()
num_sides=int(3)
side_length=int(50)
xpos=int(200)
ypos=int(200)
window.fill("purple")
pygame.display.flip()
for num_sides in [3, 4, 6, 20, 100, 360]:
    points=[]
    print (num_sides)
    for i in range (0, num_sides, 1):
        angle= (360/num_sides)
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append ([x,y])
    pygame.draw.polygon (window, pygame.Color(0,0,0), points)
    pygame.display.flip()
    pygame.time.wait (3000)
    window.fill ("green")
    pygame.display.flip()
    