import pygame

pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

idle_animation = [
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle1.png'),
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle2.png'),
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle3.png'),
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle4.png'),
    pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle5.png'),
]

Left_idle_animation = [
    pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle1.png'), True, False),
    pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle2.png'), True, False),
    pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle3.png'), True, False),
    pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle4.png'), True, False),
    pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle5.png'), True, False)
]

current_frame = 0
animation_speed = 100  # Миллисекунды между кадрами (чем меньше, тем быстрее)
last_update = pygame.time.get_ticks() # Время последнего обновления кадра

left_dirrection = False
p_x = 100
p_y = 492


frame = 0
idle_run = True
game_run = True
while game_run:

    screen.blit(pygame.image.load("Sprites/Bg/phon.png"), (0,0))

    now = pygame.time.get_ticks()
    if now - last_update > animation_speed:
        last_update = now
        current_frame = (current_frame + 1) % len(idle_animation)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        left_dirrection = False
        p_x += 3
    elif keys[pygame.K_a]:
        p_x -= 3
        left_dirrection = True
       
    if not left_dirrection:
        screen.blit(idle_animation[current_frame], (p_x, p_y))
    else:
        screen.blit(Left_idle_animation[current_frame], (p_x, p_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

pygame.quit()