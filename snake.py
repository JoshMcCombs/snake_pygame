import pygame
import sys
import random
from pygame.math import Vector2


class Fruit:
    def __init__(self) -> None:
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        # surface, color, rectangle  - old color 126, 166, 114
        pygame.draw.rect(screen, (100, 60, 200), fruit_rect)


class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw_snake(self):
        for block in self.body:
          x_pos = int(block.x * cell_size)
          y_pos = int(block.y * cell_size)
          block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
          pygame.draw.rect(screen, (0, 0, 255), block_rect)


pygame.init()
cell_size = 40
cell_number = 20
screen_size = cell_number * cell_size
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()

fruit = Fruit()
snake = Snake()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((90, 150, 150))
    fruit.draw_fruit()
    snake.draw_snake()
    # Draw all the elements
    pygame.display.update()
    clock.tick(50)
