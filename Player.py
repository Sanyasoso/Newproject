import pygame

class player:
    p_x = 100
    p_y = 492
    p_speed = 3
    jump_count = 5
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

