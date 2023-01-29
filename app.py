import pygame, timeit
from sys import exit


pygame.init()
pygame.display.set_caption("Przerwa i nauka")
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
app_phase = "Menu"
# Fonts
main_font = pygame.font.Font("./fonts/orange juice 2.0.ttf", 69)
smaller_main_font = pygame.font.Font("./fonts/orange juice 2.0.ttf", 35)
timer_font = pygame.font.Font("./fonts/orange juice 2.0.ttf", 120)
# Menu
app_name = main_font.render("Przerwa i nauka", True, "Black")
app_name_rect = app_name.get_rect(center = (320, 75))
tonton_studying = pygame.image.load("./images/tonton_studying.gif").convert_alpha()
menu_start = smaller_main_font.render("-Zacznij naukę", True, "Black" )
menu_ustaw = smaller_main_font.render("-Ustawienia", True, "Black" )
menu_instr = smaller_main_font.render("-Instrukcje", True, "Black" )
menu_start1 = smaller_main_font.render("-Zacznij naukę", True, "#191970" )
menu_ustaw1 = smaller_main_font.render("-Ustawienia", True, "#191970" )
menu_instr1 = smaller_main_font.render("-Instrukcje", True, "#191970" )
user_position_menu = 0
# Timer screen
what_timer = 0
session_time = 5
break_time = 3
sessions = 0
breaks = 0
press_space = smaller_main_font.render("Wciśnij: \"p\" = pauza, \"spacja\" = kolejna tura", True, "Black")
press_space_rect = press_space.get_rect(center = (320, 320))
session_text = main_font.render("Sesja", True, "Black")
session_text_rect = session_text.get_rect(center = (320, 50))
break_text = main_font.render("Przerwa", True, "Black")
break_text_rect = break_text.get_rect(center = (320, 50))
#Pause screen
start_back = main_font.render("\"s\" by wznowić", True, "Black")

while True:
    # user input eventloop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN and app_phase == "Menu":
            if event.key == pygame.K_DOWN:
                user_position_menu += 1
            elif event.key == pygame.K_UP:
                user_position_menu -= 1
            elif event.key == pygame.K_RETURN and user_position_menu == 0:
                app_phase = "Timer"
                starttime = timeit.default_timer()
        
        if event.type == pygame.KEYDOWN and app_phase == "Timer":
            if event.key == pygame.K_p:
                app_phase = "Pause"
            if event.key == pygame.K_SPACE and timedown < 0:
                what_timer +=1
                if what_timer % 2 == 1:
                    sessions +=1
                else:
                    breaks += 1  
                starttime = timeit.default_timer()

        if event.type == pygame.KEYDOWN and app_phase == "Pause":
            if event.key == pygame.K_s:
                app_phase = "Timer"

    screen.fill((94,129,162))
    if app_phase == "Menu":
        if user_position_menu > 2:
            user_position_menu = 0
        if user_position_menu < 0:
            user_position_menu = 2
        screen.blit(app_name,app_name_rect)
        screen.blit(menu_start1 if user_position_menu == 0 else menu_start,(75,138))
        screen.blit(menu_ustaw1 if user_position_menu == 1 else menu_ustaw,(75,188))
        screen.blit(menu_instr1 if user_position_menu == 2 else menu_instr,(75,238))
        screen.blit(tonton_studying, (300,75))
    elif app_phase == "Timer":
        timedown = (session_time if what_timer % 2 == 0 else break_time) - (timeit.default_timer() - starttime)
        show_time = timer_font.render(f"{int((timedown)/60)}:{(int(timedown) % 60)}", True, "Black" if timedown > 0 else "Red")
        screen.blit(session_text, session_text_rect)  if what_timer % 2 == 0 else screen.blit(break_text, break_text_rect)
        screen.blit(show_time, show_time.get_rect(center = (320, 175)))
        session_counter = smaller_main_font.render(f"Sesje: {sessions}   Przerwy: {breaks}", True, "Black")
        screen.blit(session_counter, session_counter.get_rect(center = (320, 250)))
        screen.blit(press_space, press_space_rect)
    elif app_phase == "Pause":
        screen.blit(start_back, app_name_rect)
        starttime = timeit.default_timer()
        session_time = timedown
    pygame.display.update()
    clock.tick(5)