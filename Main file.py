import pygame
from Player import  player
pygame.init()

screen = pygame.display.set_mode((700, 500))
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
while game_run:

    screen.blit(pygame.image.load("Sprites/Bg/phon.png"), (0,0))

    now = pygame.time.get_ticks()
    if now - last_update > animation_speed:
        last_update = now
        current_frame = (current_frame + 1) % len(player.idle_animation)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

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

    pygame.display.update()

pygame.quit()