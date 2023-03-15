import pygame
def threenp1(n):
    count=0
    while n>1.0:
        count+=1
        if n%2==0:
            n=int(n/2)
        else:
            n=int(3 * n+1)
    return count
def threenp1range(upper_limit):
    my_dict={}
    for n in range(2, upper_limit+1):
       my_dict[n]= threenp1(n)
    return my_dict
def main():
    upper_limit=int(input("Enter the limit: "))
    print (threenp1range(upper_limit))
def graph():
    pygame.init()
    screen=pygame.display.set_mode()
    pygame.draw.lines()

main()
           
        