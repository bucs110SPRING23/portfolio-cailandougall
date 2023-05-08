import turtle
def letter_A(param1, param2):
    """
    This is a function that will draw the letter A
    args: angle (int), length (int), goto (x,y)
    """
    angle=50
    pen1=turtle.Turtle ()
    pen1.color("blue")
    pen1.up()
    pen1.goto(-200,00)
    pen1.down()
    pen1.speed(param1)
    pen1.left(angle)
    pen1.fd(75)
    pen1.goto(-100,0)
    pen1.up()
    pen1.goto(-100,-20)
    pen2=turtle.Turtle ()
    pen2.color("blue")
    pen2.up()
    pen2.goto(-180,24)
    pen2.down()
    pen2.speed (param2)
    pen2.goto(-122,24)
    pen2.up()
    pen2.goto(-100,24)
def letter_E(param3, param4, param5):
    """
    This is a function that will draw the letter E
    args: angle (int), length (int), goto (x,y)
    """
    angle=90
    pen3=turtle.Turtle ()
    pen3.color("blue")
    pen3.goto(0,0)
    pen3.speed(param3)
    pen3.lt(angle)
    pen3.fd(55)
    pen3.right(angle)
    pen3.fd(70)
    pen3.up()
    pen3.fd(20)
    pen4=turtle.Turtle ()
    pen4.color("blue")
    pen4.up()
    pen4.goto(0,24)
    pen4.down()
    pen4.speed(param4)
    pen4.fd(45)
    pen4.up()
    pen4.fd(20)
    pen5=turtle.Turtle ()
    pen5.color("blue")
    pen5.goto(0,0)
    pen5.speed(param5)
    pen5.fd(70)
    pen5.up()
    pen5.fd(20)
def symbol_Pi(param6):
    """
    This is a function that will draw the symbol Pi
    args: angle (int), length (int), goto (x,y)
    """
    angle=90
    pen6=turtle.Turtle ()
    pen6.color("blue")
    pen6.up()
    pen6.goto(225,0)
    pen6.down()
    pen6.speed(param6)
    for i in range (2):
        pen6.lt(angle)
        pen6.fd(55)
    pen6.goto(170,0)
    pen6.up()
    pen6.goto(170,-20)
def main():
    param1=int(input("Enter the parameter: "))
    param2=int(input("Enter a number: "))
    param3=int(input("Enter param1: "))
    param4=int(input("Please enter a number: "))
    param5=int(input("What would you like param3 to be?: "))
    param6=int(input("Input a number: "))
    window=turtle.Screen().bgcolor ("gold")
    letter_A(param1, param2)
    letter_E(param3, param4, param5)
    symbol_Pi(param6)
    window=turtle.Screen()
    window.exitonclick()
main ()