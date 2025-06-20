import pygame

screen = pygame.display.set_mode((700, 500))

idle_animation = [
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle1.png'),
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle2.png'),
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle3.png'),
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle4.png'),
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle5.png'),
]


p_x = 10
p_y = 492

frame = 0
idle_run = True
game_run = True
while game_run:

    screen.blit(pygame.image.load("Sprites/Bg/phon.png"), (0,0))

    if idle_run:
        screen.blit(idle_animation[frame], (p_x,p_y))
        if frame == 4:
            frame = 0
        else:
            frame += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p_x += 3
    elif keys[pygame.K_a]:
        p_x -= 3


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

pygame.quit()