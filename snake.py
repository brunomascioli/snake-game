import pygame, random
from pygame.locals import *
from time import sleep

def on_grid_random():
    x = random.randint(0,30) * 20
    y = random.randint(0,30) * 20
    return (x, y)

def apple_collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def collision(snake_head, snake):
    for i in range(1, len(snake) -1):
        if snake[i] == snake_head:
            return True
    return False

def game_over():
    fonte = pygame.font.SysFont("Monospace", 50, True, False)
    lose_message = fonte.render('Game Over!', True, (255,0,0))
    screen.blit(lose_message, (150,250))
    pygame.display.update()
    sleep(3)
    pygame.quit()

def board():
    for row in range(resolution[0] // square_size):
        for col in range(resolution[1] // square_size):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen,(114, 183, 106), (col * square_size, row * square_size, square_size, square_size))
            else:
                pygame.draw.rect(screen,(172, 206, 94), (col * square_size, row * square_size, square_size, square_size))

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
resolution = (600,600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Snake')

font = pygame.font.SysFont("Monospace", 30, True, False)
pontos = 0
snake = [(0, 0), (10,0), (20,0)]
snake_skin = pygame.Surface((20,20))
snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((20,20))
apple.fill((255,0,0))

square_size = 20

my_direction = DOWN
change_to = my_direction


fps_controller = pygame.time.Clock()

while True:
    mensagem = f'Pontuação: {pontos}'
    formatacao_texto = font.render(f'Score: {pontos}', True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                change_to = UP
            if event.key == K_DOWN:
                change_to = DOWN
            if event.key == K_LEFT:
                change_to = LEFT
            if event.key == K_RIGHT:
                change_to = RIGHT


    if change_to == UP and my_direction != DOWN:
        my_direction = UP
    if change_to == DOWN and my_direction != UP:
        my_direction = DOWN
    if change_to == LEFT and my_direction != RIGHT:
        my_direction = LEFT
    if change_to == RIGHT and my_direction != LEFT:
        my_direction = RIGHT

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 20)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 20)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 20, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 20, snake[0][1])

    if collision(snake[0], snake):
        game_over()

    if apple_collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        pontos += 1

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    board()
    screen.blit(apple, apple_pos)
    screen.blit(formatacao_texto, (0,0))

    for pos in snake:
        screen.blit(snake_skin,pos)
        for i in pos:
            if i > resolution[0] or i < 0:
                game_over()

    fps_controller.tick(15)
    pygame.display.update()