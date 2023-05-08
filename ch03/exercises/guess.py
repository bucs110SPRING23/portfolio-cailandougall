import random
the_number=random.randrange(1,11)
for i in range(3):
    my_guess=int(input("Guess a number between 1 and 10: "))
    if my_guess<the_number:
        print("Too Low")
    elif my_guess>the_number:
        print("Too High")
    elif my_guess==the_number:
        print("Correct!")
        break