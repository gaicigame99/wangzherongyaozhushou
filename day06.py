import pygame
import random

screen = pygame.display.set_mode((800,600))
background = pygame.image.load("1.jpg")
snow = pygame.image.load("snow32.png")

list_x = []
list_y = []
speedy = []
speedx = []
for i in range(300):
    x = random.randint(0, 800-32)
    y = random.randint(0, 600-32)
    sy = random.randint(1,3)
    sx = random.randint(-3,3)
    list_x.append(x)
    list_y.append(y)
    speedy.append(sy)
    speedx.append(sx)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(background, (0, 0))
    for i in range(300):
        x1 = list_x[i]
        y1 = list_y[i]
        list_y[i] += speedy[i]
        list_x[i] += speedx[i]
        if list_y[i] > 600:
            list_y[i] = -32
            list_x[i] = random.randint(0, 800 - 32)
        screen.blit(snow, (x1, y1))

    pygame.display.update()

# 作业1，月食
# 作业2，五子棋盘

