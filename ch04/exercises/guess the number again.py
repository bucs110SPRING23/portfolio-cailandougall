import random
the_number=random.randrange(1,1001)
i=0
while i<1001:
    my_guess=int(input("Guess a number between 1 and 1000: "))
    i+=1
    number_of_guesses=i
    if my_guess<the_number:
        print("Too Low")
    elif my_guess>the_number:
        print("Too High")
    elif my_guess==the_number:
        print("You got it! The correct answer is", the_number, "and it took you", number_of_guesses, "tries to get it")
        break