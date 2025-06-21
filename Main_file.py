import pygame
from Newproject.tilemap import blit_the_tile
from config import screen
from Player import  player
import csv
import tilemap

def show_menu():
    menu_run = True

    phon_menu = pygame.image.load('Sprites/menu/phon_menu.png')
    button = pygame.Surface((200, 100))
    button.fill('blue')
    button_hbox = button.get_rect(topleft=(245, 200))

    while menu_run:
        screen.blit((phon_menu), (0, 0))
        screen.blit(button, button_hbox)

        mouse = pygame.mouse.get_pos()

        pygame.display.update()

        if button_hbox.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print(';qwef')
            menu_run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame, quit()

pygame.init()

clock = pygame.time.Clock()

current_frame = 0
animation_speed = 100  # Миллисекунды между кадрами (чем меньше, тем быстрее)
last_update = pygame.time.get_ticks() # Время последнего обновления кадра

left_dirrection = False

is_jump = False
jump_count = 5

frame = 0
idle_run = True
game_run = True

show_menu()

while game_run:

    screen.blit(pygame.image.load("Sprites/Bg/phon.png"), (0,0))

    now = pygame.time.get_ticks()
    if now - last_update > animation_speed:
        last_update = now
        current_frame = (current_frame + 1) % len(player.idle_animation)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        left_dirrection = False
        player.p_x += player.p_speed
    elif keys[pygame.K_a]:
        player.p_x -= player.p_speed
        left_dirrection = True
       
    if not left_dirrection:
        screen.blit(player.idle_animation[current_frame], (player.p_x, player.p_y))
    else:
        screen.blit(player.Left_idle_animation[current_frame], (player.p_x, player.p_y))

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -5:
            if jump_count > 0:
                player.p_y -= (jump_count ** 2) / 2
            else:
                player.p_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 5

    blit_the_tile()

    pygame.display.update()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

pygame.quit()
