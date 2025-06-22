import pygame

def show_menu(screen):
    menu_run = True
    play_button = pygame.Surface((200, 100))
    play_button.fill('green')
    play_button_hbox = play_button.get_rect(topleft=(305, 120))
    leave_button = pygame.Surface((200,100))
    leave_button.fill('red')
    leave_button_hbox = leave_button.get_rect(topleft=(305,270))
    while menu_run:
        screen.blit((pygame.image.load('Sprites/menu/phon_menu.png')), (0, 0))
        screen.blit(play_button, play_button_hbox)
        screen.blit(leave_button,leave_button_hbox)

        mouse = pygame.mouse.get_pos()
        pygame.display.update()

        if play_button_hbox.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            menu_run = False
            screen.fill((0, 0, 0))
        if leave_button_hbox.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            menu_run = False
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
