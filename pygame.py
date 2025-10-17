import pygame, random, sys

pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100, 50)]
dx, dy = 10, 0
food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: dx, dy = 0, -10
    if keys[pygame.K_DOWN]: dx, dy = 0, 10
    if keys[pygame.K_LEFT]: dx, dy = -10, 0
    if keys[pygame.K_RIGHT]: dx, dy = 10, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)
    if head == food:
        food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
    else:
        snake.pop()

    if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]):
        sys.exit()

    win.fill((0, 0, 0))
    for x, y in snake: pygame.draw.rect(win, (0, 255, 0), (x, y, 10, 10))
    pygame.draw.rect(win, (255, 0, 0), (*food, 10, 10))
    pygame.display.update()
    clock.tick(15)
