import pygame
from tilemap import blit_the_tile
from config import screen, WIDTH, HEIGHT, FPS
from Player import Player

pygame.init()
clock = pygame.time.Clock()

# Создаем экземпляр игрока
player = Player(100, 100, 35, 35)  # Начальная позиция и размеры

# Гравитация и другие константы перенесены в класс Player

# Загрузка карты (предполагается, что у вас есть функция load_map)
# map_data = load_map("Sprites/tilemap/map.txt.txt")

# Основной цикл игры
running = True
scroll_x = 0
scroll_y = 0  # Инициализация scroll_y
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Добавьте другие обработчики событий, если необходимо

    # Обработка ввода
    keys = pygame.key.get_pressed()
    player.handle_input(keys)

    # Обновление игрока (физика)
    player.update()

    # Скроллинг камеры (центрируем на игроке)
    scroll_x = player.x - WIDTH // 2
    #scroll_y = player.y - HEIGHT // 2 #Удаляем, он нам мешает

    # Отрисовка
    screen.fill((135, 206, 235))  # Небесный фон

    # Отрисовка тайлов
    blit_the_tile(scroll_x, scroll_y, player)

    # Отрисовка игрока (debug)
    pygame.draw.rect(screen, (255, 255, 255), player.rect, 2)

        # Вывод отладочной информации
    #print(f"on_ground: {player.on_ground}, is_jumping: {player.is_jumping}, velocity_y: {player.velocity_y}")

    # Обновление экрана
    pygame.display.flip()

    # Контроль FPS
    clock.tick(FPS)

pygame.quit()