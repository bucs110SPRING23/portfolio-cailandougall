import turtle
import random
window=turtle.Screen().bgcolor("green")
print(turtle.screensize())
pen=turtle.Turtle
angle=90
turtle.pencolor ("blue")
turtle.goto (0,0)
heads=1
tails=2
screenx=turtle.screensize()[0]
screeny=turtle.screensize()[1]
while turtle.pos()[0] < screenx and turtle.pos()[0] > (screenx*-1) and turtle.pos()[1] < screeny and turtle.pos()[1] > (screeny*-1): 
    coinflip=random.randrange (1,3)
    print(coinflip)
    if coinflip==1:
        turtle.left(angle)
        turtle.fd (50)
    if coinflip==2:
        turtle.right(angle)
        turtle.fd (50)
print(turtle.pos())
window.exitonclick()