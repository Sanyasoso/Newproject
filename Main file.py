import pygame

screen = pygame.display.set_mode((700, 500))

game_run = True
while game_run:

    screen.blit(pygame.image.load("phon.png"), (0,0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

pygame.quit()