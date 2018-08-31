import pygame
import random
# 创建一块屏幕
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("1.jpg")

snow = pygame.image.load("snow32.png")
# x = 100
# y = -32
lx = []
ly = []
for i in range(300):
    x = random.randint(0,800-32)
    y = random.randint(0,600-32)
    lx.append(x) # lx[0],lx[1]
    ly.append(y)
while True:
    # 逐条获取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(background, (0,0))# 显示背景
    for i in range(300):# 显示图片
        x = lx[i]
        y = ly[i]
        ly[i] += 1
        if ly[i]> 600:
            ly[i] =-32
        screen.blit(snow, (x, y))
    # 显示一下
    pygame.display.update()