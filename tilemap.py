import pygame
from config import screen
from Player import Player

# Константы (определяем размеры тайла один раз)
TILE_SIZE = 35  # Размер тайла (предполагаю, что он квадратный)

# Загружаем текстуру тайла (делаем это один раз)
TILE_IMAGE = pygame.transform.scale(pygame.image.load('Sprites/tileset/Tile-01.png'), (TILE_SIZE, TILE_SIZE))


def blit_the_tile(scroll_x, scroll_y, player):  # Передаем player как аргумент

    with open('Sprites/tilemap/map.txt.txt', 'r') as mapfile:
        # Читаем карту из файла (предполагается, что файл не очень большой)
        map_data = [line.strip() for line in mapfile.readlines()]

    # Сбрасываем флаг "на земле" перед каждой проверкой
    player.on_ground = False

    # Перебираем строки карты
    for row_index, row in enumerate(map_data):
        # Перебираем символы в строке
        for col_index, tile_type in enumerate(row):
            if tile_type == '1':  # Если текущий символ - '1' (тайл)
                # Вычисляем координаты тайла на экране с учетом скроллинга
                tile_x = (col_index * TILE_SIZE) - scroll_x
                tile_y = (row_index * TILE_SIZE) - scroll_y

                # Создаем прямоугольник для тайла (используем константу TILE_SIZE)
                tile_rect = pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE)

                # Проверяем столкновение с игроком
                if player.rect.colliderect(tile_rect):

                    # Обработка столкновения (сверху)
                    if player.velocity_y > 0 and player.rect.bottom > tile_rect.top:
                        player.rect.bottom = tile_rect.top
                        player.y = player.rect.y # Обновляем позицию y игрока
                        player.velocity_y = 0
                        player.on_ground = True

                    #Обработка столкновения (снизу)
                    elif player.velocity_y < 0 and player.rect.top < tile_rect.bottom:
                        player.rect.top = tile_rect.bottom
                        player.y = player.rect.y
                        player.velocity_y = 0


                # Отрисовываем тайл
                screen.blit(TILE_IMAGE, tile_rect)

                # Отрисовываем прямоугольник для отладки (можно убрать в финальной версии)
                pygame.draw.rect(screen, (255, 0, 0), tile_rect, 1)  # Ширина 1 для отображения контура