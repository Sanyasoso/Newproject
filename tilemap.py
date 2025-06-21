import csv
import pygame
from config import screen

Tile01 = pygame.image.load('Sprites/tileset/Tile-01.png')
def blit_the_tile():
    with open('Sprites/tilemap/tilemap..csv', 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
            row = list(row)
            findinrow = row[0].find('0')
            if findinrow:
                screen.blit(Tile01, (100, 100))
    file.close()

blit_the_tile()