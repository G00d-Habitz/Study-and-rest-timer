import pygame, timeit
from sys import exit

def animedoro():
    goaltime = int(input("How many seconds would you like to count down from? "))
    starttime = timeit.default_timer()
    while timeit.default_timer() - starttime < goaltime:
        timedown = goaltime - (timeit.default_timer() - starttime)
        print(f"Current time is: {int((timedown)/60)}:{(int(timedown) % 60)}")
    print("Bzzzt! The time is up!")

pygame.init()
pygame.display.set_caption("Czas na naukę!")
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()


while True:

    # user input eventloop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((94,129,162))
    
    pygame.display.update()
    clock.tick(10)