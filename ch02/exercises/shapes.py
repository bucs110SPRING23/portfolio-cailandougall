import pygame
pygame.init()
screen=pygame.display.set_mode()
screen.fill("black")
while 1:
    pygame.event.pump()
    pygame.draw.circle (screen, "blue", [300,200], 50)
    pygame.draw.circle (screen, "blue", [300,150], 40)
    pygame.draw.circle (screen, "blue", [300,100], 30)
    pygame.display.flip()
    pygame.time.wait (5000)
    break

