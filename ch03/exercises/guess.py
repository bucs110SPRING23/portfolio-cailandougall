import random
the_number=random.randrange(1,11)
for i in range(1,4):
    my_guess=int(input("Guess the number: "))
    if my_guess<the_number:
        print("Too Low")
    elif my_guess>the_number:
        print("Too High")
    elif my_guess==the_number:
        print("Correct!")
        break