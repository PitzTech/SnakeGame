import time
import random
import pygame
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1]) 

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if (event.key == K_UP or event.key == K_w) and my_direction != DOWN:
                my_direction = UP
            elif (event.key == K_DOWN or event.key == K_s) and my_direction != UP:
                my_direction = DOWN
            elif (event.key == K_LEFT or event.key == K_a) and my_direction != RIGHT:
                my_direction = LEFT
            elif (event.key == K_RIGHT or event.key == K_d) and my_direction != LEFT:
                my_direction = RIGHT
    
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
    if (snake[0] in snake[1::]) or (snake[0][0] < 0) or (snake[0][0] > 600) or (snake[0][1] < 0) or (snake[0][1] > 600):
        pygame.quit()

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    elif my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    else:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update();
