import pygame
from tilemap import blit_the_tile
from config import screen
from Player import  player
from menu import show_menu

pygame.init()

clock = pygame.time.Clock()

current_frame = 0
animation_speed = 100  # Миллисекунды между кадрами (чем меньше, тем быстрее)
last_update = pygame.time.get_ticks() # Время последнего обновления кадра

left_dirrection = False

is_jump = False

frame = 0
idle_run = True
game_run = True

show_menu(screen)

scroll_x = 0
scroll_y = 0

phon_x = 0
phon_y = 0
while game_run:

    screen.blit(pygame.image.load("Sprites/Bg/phon.png"), (phon_x + 0,phon_y - 100))
    screen.blit(pygame.image.load("Sprites/Bg/phon.png"), (phon_x + 700,phon_y - 100))
    screen.blit(pygame.image.load("Sprites/Bg/phon.png"), (phon_x + 0,phon_y + 200))
    screen.blit(pygame.image.load("Sprites/Bg/phon.png"), (phon_x + 700,phon_y + 200))

    player_collision = player.idle_animation[0].get_rect(topleft=(player.x,player.y))


    now = pygame.time.get_ticks()
    if now - last_update > animation_speed:
        last_update = now
        current_frame = (current_frame + 1) % len(player.idle_animation)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        left_dirrection = False
        #player.x += player.speed
        if player.x >= ((800 / 2) - player.size_x):
            phon_x -= player.speed
            scroll_x += player.speed
        else:
            player.x += player.speed
    elif keys[pygame.K_a]:
        left_dirrection = True
        if phon_x < 0:
            #player.x -= player.speed
            phon_x += player.speed
            scroll_x -= player.speed
        else:
            if player.x > 0:
                player.x -= player.speed

    if not left_dirrection:
        screen.blit(player.idle_animation[current_frame], (player.x, player.y))
    else:
        screen.blit(player.Left_idle_animation[current_frame], (player.x, player.y))

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if player.jump_count >= -player.jump_high:
            if player.jump_count > 0:
                scroll_y -= (player.jump_count ** 2) / 2
                phon_y += (player.jump_count ** 2) / 2
            else:
                scroll_y += (player.jump_count ** 2) / 2
                phon_y -= (player.jump_count ** 2) / 2
            player.jump_count -= 1
        else:
            is_jump = False
            player.jump_count = player.jump_high

    if phon_x <= -576:
        phon_x = 0

    blit_the_tile(scroll_x + 100, scroll_y)
    pygame.display.update()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

pygame.quit()
