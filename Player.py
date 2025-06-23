import pygame

class player:
    size_x = 50
    size_y = 50
    x = (800 / 2) - size_x
    y = 600 - (size_y * 3)
    speed = 3
    jump_high = 8
    jump_count = jump_high
    idle_animation = [
        pygame.transform.scale(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle1.png'), (size_x,size_y)),
        pygame.transform.scale(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle2.png'), (size_x,size_y)),
        pygame.transform.scale(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle3.png'), (size_x,size_y)),
        pygame.transform.scale(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle4.png'), (size_x,size_y)),
        pygame.transform.scale(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle5.png'), (size_x,size_y)),
    ]

    Left_idle_animation = [
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle1.png'), True, False), (size_x,size_y)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle2.png'), True, False), (size_x,size_y)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle3.png'), True, False), (size_x,size_y)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle4.png'), True, False), (size_x,size_y)),
        pygame.transform.scale(pygame.transform.flip(pygame.image.load('Sprites/Animation/Idle_anim/Playersprite_idle5.png'), True, False), (size_x,size_y))
    ]
