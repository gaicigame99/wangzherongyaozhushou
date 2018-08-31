import pygame
import random

FONTSIZE = 40
NUMBER = 10

# 初始化我们的pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
background = pygame.image.load("1.jpg")
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", FONTSIZE)
# "得分:100"
lt = []
lx = []
ly = []
for i in range(NUMBER):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    lx.append(x)
    ly.append(y)
    k = random.randint(0, 25)
    # text = font.render(chr(65+k), False, (255, 255, 255))
    zimu = chr(65 + k)
    lt.append(zimu)

fenshu = 0
ax = -50
ay = -50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            print(chr(event.key-32))
            if chr(event.key - 32) not in lt:
                print("你没敲对，减分怪我咯")
                fenshu -= 1
            for i in range(NUMBER):
                t = lt[i]
                if t == chr(event.key-32):
                    # 分数效果获得字母位置
                    ax = lx[i]
                    ay = ly[i]
                    # print(x,y)
                    # 修改字母位置
                    ly[i] = -40
                    k = random.randint(0, 25)
                    lt[i] = chr(65 + k)
                    lx[i] = random.randint(0, 800 - FONTSIZE)
                    fenshu += 1
    screen.blit(background, (0, 0))
    # 得分
    score = font.render("得分:%d" % fenshu, True, (255, 255, 255))
    screen.blit(score, (0, 0))

    # +1 效果
    add_s = font.render("+1", True, (255,255,255))
    screen.blit(add_s, (ax, ay))
    ay -= 1


    for i in range(NUMBER):
        x = lx[i]
        y = ly[i]
        ly[i] += 0.1
        if ly[i] > 600:
            ly[i] = -FONTSIZE
            lx[i] = random.randint(0, 800-FONTSIZE)
            k = random.randint(0, 25)
            lt[i] = chr(65 + k)
        text = font.render(lt[i], False, (255, 255, 255))
        screen.blit(text, (x, y))

    pygame.display.update()