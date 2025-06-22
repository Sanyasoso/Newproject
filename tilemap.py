import pygame
from config import screen


Tile01 = pygame.image.load('Sprites/tileset/Tile-01.png')

TILE_SIZE_Sprite = 8
tile_x = 0
tile_y = 0

def blit_the_tile():
    global tile_x, tile_y

    tile_x = 0
    tile_y = 0

    with open('Sprites/tilemap/map.txt.txt', 'r') as mapfile:
        readfile = mapfile.readlines()

        for index_line, current_line in enumerate(readfile):
            current_line = current_line.strip()

            # tile_x сбрасывается в начале каждой строки
            tile_x = 0

            # Итерируемся по символам в строке для отрисовки тайлов в каждой позиции
            for char_index, char in enumerate(current_line):
                if char == '1':  # Если текущий символ - '1'

                    new_tile_x = char_index * TILE_SIZE_Sprite  # Позиция X зависит от индекса символа
                    new_tile_y = index_line * TILE_SIZE_Sprite  # Позиция Y зависит от индекса строки

                    screen.blit(Tile01, (new_tile_x, new_tile_y))












