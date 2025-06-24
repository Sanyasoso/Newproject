import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity_y = 0
        self.on_ground = False
        self.speed = 5
        self.left_direction = False
        self.is_jumping = False
        self.jump_high = 10
        self.GRAVITY = 0.4
        self.MAX_FALL_SPEED = 10

    def update(self):
        # Применение гравитации (если не на земле)
        if not self.on_ground:
            self.velocity_y += self.GRAVITY
            if self.velocity_y > self.MAX_FALL_SPEED:
                self.velocity_y = self.MAX_FALL_SPEED

        # Обновление позиции
        self.y += self.velocity_y
        self.rect.y = self.y  # Обновляем rect

        #print(f"Before collision: y={self.y}, rect.y={self.rect.y}, velocity_y={self.velocity_y}, on_ground={self.on_ground}")

    def handle_input(self, keys):
        # Обработка движения
        if keys[pygame.K_d]:
            self.left_direction = False
            self.x += self.speed
        elif keys[pygame.K_a]:
            self.left_direction = True
            self.x -= self.speed

        # Обработка прыжка
        if not self.is_jumping and self.on_ground and keys[pygame.K_SPACE]:
            self.start_jump()

        self.rect.x = self.x
        #self.rect.y = self.y  #  не трогаем rect.y здесь

    def start_jump(self):
        self.velocity_y = -10
        self.is_jumping = True
        self.on_ground = False