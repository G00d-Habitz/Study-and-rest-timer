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
pygame.display.set_caption("Przerwa dla nauki")
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()

# Fonts
main_font = pygame.font.Font("./fonts/orange juice 2.0.ttf", 69)
smaller_main_font = pygame.font.Font("./fonts/orange juice 2.0.ttf", 35)
app_name = main_font.render("Przerwa dla nauki", True, "Black")
app_name_rect = app_name.get_rect(center = (320, 75))
menu_start = smaller_main_font.render("-Zacznij naukę", True, "Black" )
menu_start_rect = menu_start.get_rect(bottomleft = (75, 175))
menu_ustaw = smaller_main_font.render("-Ustawienia", True, "Black" )
menu_ustaw_rect = menu_ustaw.get_rect(bottomleft = (75, 225))
menu_instr = smaller_main_font.render("-Instrukcje", True, "Black" )
menu_instr_rect = menu_instr.get_rect(bottomleft = (75, 275))
while True:

    # user input eventloop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((94,129,162))
    screen.blit(app_name,app_name_rect)
    screen.blit(menu_start,menu_start_rect)
    screen.blit(menu_ustaw,menu_ustaw_rect)
    screen.blit(menu_instr,menu_instr_rect)

    pygame.display.update()
    clock.tick(10)