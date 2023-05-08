import turtle
print ("How many sides are there?")
sides=int(input("Enter a number: "))
angle=(360/sides)
print ("What is the length of each side?")
length=float(input("Enter a number: "))
pen=turtle.Turtle
turtle.pencolor ("purple")
for i in range (sides):
    turtle.rt (angle)
    turtle.fd (length)
window=turtle.Screen ()
window.exitonclick ()

