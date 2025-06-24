import pygame
from tilemap import blit_the_tile
from config import screen
from Player import player  # Исправлено: импортируем класс player
from menu import show_menu

pygame.init()

clock = pygame.time.Clock()

current_frame = 0
animation_speed = 100  # Миллисекунды между кадрами (чем меньше, тем быстрее)
last_update = pygame.time.get_ticks()  # Время последнего обновления кадра

left_dirrection = False


frame = 0
idle_run = True
game_run = True

show_menu(screen)

scroll_x = 0
scroll_y = 0

phon_x = 0
phon_y = 0

player1 = player()  # Исправлено: Создаем экземпляр класса player

phon_load = pygame.image.load("Sprites/Bg/phon.png")

while game_run:
    player1.update()  # Исправлено: Вызываем update() правильно
    screen.blit(phon_load, (phon_x + 0, phon_y - 100))
    screen.blit(phon_load, (phon_x + 700, phon_y - 100))
    screen.blit(phon_load, (phon_x + 0, phon_y + 200))
    screen.blit(phon_load, (phon_x + 700, phon_y + 200))

    # player_collision = player.idle_animation[0].get_rect(topleft=(player.x,player.y))

    now = pygame.time.get_ticks()
    if now - last_update > animation_speed:
        last_update = now
        current_frame = (current_frame + 1) % len(player1.idle_animation)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        left_dirrection = False
        # player.x += player.speed
        if player1.x >= ((800 / 2) - player1.size_x):
            phon_x -= player.speed  # Заменили player на player1
            scroll_x += player.speed
        else:
            player1.x += player1.speed
    elif keys[pygame.K_a]:
        left_dirrection = True
        if phon_x < 0:
            # player.x -= player.speed
            phon_x += player1.speed
            scroll_x -= player1.speed
        else:
            if player1.x > 0:
                player1.x -= player.speed #Заменили player на player1

    if not left_dirrection:
        screen.blit(player1.idle_animation[current_frame], (player1.x, player1.y))
    else:
        screen.blit(player1.Left_idle_animation[current_frame], (player1.x, player1.y))

    if not player1.is_jumping: #Исправили is_jump на is_jumping
        if keys[pygame.K_SPACE]:
            player1.in_is_jump()

    else:
        if player1.jump_count >= -player1.jump_high:
            if player1.jump_count > 0:
                scroll_y -= (player1.jump_count * 2) / 2
                phon_y += (player1.jump_count * 2) / 2
            else:
                scroll_y += (player1.jump_count * 2) / 2
                phon_y -= (player1.jump_count * 2) / 2
            player1.jump_count -= 1
        else:
            player1.is_jumping = False  #Исправили is_jump на is_jumping
            player1.jump_count = player1.jump_high

    if phon_x <= -576:
        phon_x = 0

    blit_the_tile(scroll_x + 100, scroll_y)
    pygame.draw.rect(screen, color=(0, 255, 0), rect=player1.player_collision)  # отображение колизии игрока Временно
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    clock.tick(60)

pygame.quit()