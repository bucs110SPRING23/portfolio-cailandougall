import pygame
screen=pygame.display.set_mode()
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
    my_result=threenp1range(upper_limit)
    graph (my_result)
    print (my_result)
def graph(my_result):
    pygame.init()
    pygame.draw.lines(screen, "red", False, list(my_result.items()))
    new_screen=pygame.transform.flip(screen, False, True)
    width, height=new_screen.get_size()
    new_screen= pygame.transform.scale(new_screen, (width * 5, height * 5))
    screen.blit(new_screen, (0, 0))
    max_so_far=-1
    for value in (my_result.values()):
        if value>max_so_far:
            max_so_far=value
    font=pygame.font.Font(None, 24)
    msg=font.render(str(max_so_far), True, "blue")
    screen.blit(msg, (50,50))
main()
           
        