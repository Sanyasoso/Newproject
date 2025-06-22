import pygame
from config import screen


Tile01 = pygame.image.load('Sprites/tileset/Tile-01.png')
TILE_SIZE_Sprite = 8
tile_x = 0
tile_y = 0

def blit_the_tile():
    global tile_x, tile_y
    with open('Sprites/tilemap/map.txt.txt', 'r') as mapfile:
        readfile = mapfile.readlines()

        for index_line, current_line in enumerate(readfile):
            current_line = current_line.strip()
            if '1' in current_line:

               new_tile_x = tile_x * TILE_SIZE_Sprite
               new_tile_y = tile_y * TILE_SIZE_Sprite

               screen.blit(Tile01, (new_tile_x, new_tile_y))

               tile_x += 1







