import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 800
screen_height = 300

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Google Dinosaur")

# Загрузка изображений
dino_img = pygame.image.load("dino.png")
cactus_img = pygame.image.load("cactus.png")

# Определение начальной позиции динозавра
dino_x = 50
dino_y = 220

# Определение начальной скорости и положения кактусов
cactus_x = screen_width
cactus_y = 230
cactus_speed = 5

# Определение переменных для отслеживания игрового времени и количества очков
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont("Arial", 25)

# Начальные значения для прыжка
jump_speed = 0
gravity = 0.5

# Главный игровой цикл
game_over = False
while not game_over:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Обработка нажатия клавиши пробел
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        # Установка начальной скорости прыжка
        jump_speed = -9
    
    # Обновление вертикальной позиции динозавра на каждой итерации цикла
    dino_y += jump_speed
    jump_speed += gravity
    
    # Ограничение прыжка до определенной высоты
    if dino_y > 220:
        dino_y = 220
        jump_speed = 0
    
    # Отрисовка фона
    screen.fill((255, 255, 255))
    
    # Отрисовка динозавра
    screen.blit(dino_img, (dino_x, dino_y))
    
    # Отрисовка кактусов
    screen.blit(cactus_img, (cactus_x, cactus_y))
    
    # Обновление положения кактусов
    cactus_x -= cactus_speed
    
    # Проверка столкновений
    if cactus_x < 0:
        cactus_x = screen_width
        score += 1

    if dino_x + dino_img.get_width() > cactus_x and dino_x < cactus_x + cactus_img.get_width() and dino_y + dino_img.get_height() > cactus_y:
    	game_over = True
    	print('Game Over')
    
    # Отрисовка количества очков
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # Обновление экрана
    pygame.display.update()
    
    # Ограничение FPS
    clock.tick(60)

# Завершение Pygame
pygame.quit()
