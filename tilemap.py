import csv
import pygame
from pygame.examples.grid import TILE_SIZE
from config import screen


Tile01 = pygame.image.load('Sprites/tileset/Tile-01.png')
TILE_SIZE_Sprite = 8
def blit_the_tile():
    with open('Sprites/tilemap/tilemap..csv', 'r', newline='') as file:
        reader = csv.reader(file)

        row_index = 0
        for row in reader:
            col_index = 0
            for tile_value in row:
                try:
                   tile_index = tile_value.find('0')
                   if tile_index:
                        move_tile_x = col_index * TILE_SIZE_Sprite
                        move_tile_y = row_index * TILE_SIZE_Sprite
                        screen.blit(Tile01, (move_tile_x, move_tile_y))

                   else:
                        print(f"Некорректный индекс тайла: {tile_index} Пропускаем.")
                except ValueError:
                    print(f"Некорректное значение тайла: {tile_value}. Пропускаем.")

                col_index += 1  # Переходим к следующему столбцу
            row_index += 1  # Переходим к следующей строке
            break







