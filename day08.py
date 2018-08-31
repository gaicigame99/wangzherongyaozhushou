# kick block
import pygame
# import math

WHITE = (255,255,255)
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("1.jpg")
ball = pygame.image.load("ball32.png")
ball_rect = ball.get_rect()
# print(ball_rect)
# print(ball_rect.width)
# print(ball_rect.height)

tray = pygame.image.load("tray2.png")
# 获取到托盘的宽高
t_rect = tray.get_rect()
block = pygame.image.load("block.jpg")
# 获取到砖块的宽高
bl_rect = block.get_rect()
w = bl_rect.width
h = bl_rect.height
# 改变图片的大小
block = pygame.transform.scale(block, (w // 2, h // 2))
bl_rect = block.get_rect()
width = bl_rect.width
height = bl_rect.height

lbx = []
lby = []
for i in range(3):
    for j in range(5):
        x = 50 + j * width + j * 10
        y = 30 + i * height + i * 10
        lbx.append(x)
        lby.append(y)
bx, by = 200+t_rect.width//2-16, 500-32
# bx+16,by+16
direction = 0
speedx, speedy = 0, 0
tx, ty = 200, 500
# 球的四条边
# 顶  by
# 底  by+ball_rect.height
# 左  bx
# 右  bx+ball_rect.width

# 砖块的四条边
# 顶  lby[i]
# 底  lby[i]+height
# 左  lbx[i]
# 右  lbx[i]+width

# 碰撞
# 球顶, 球顶<砖底，and 砖底 < 球底
#       球顶< 砖底 < 球底
#  by< lby[i]+height < by+ball_rect.height
# 球底 球底>砖顶 and 砖顶 > 球顶
#    球底>砖顶 >球顶
#    球顶<砖顶 <球底
#  by< lby[i] < by+ball_rect.height

# 球左
# 球右
flag = 0
start = 0
xdir = 0

while True:
    screen.blit(background, (0, 0))
    screen.blit(ball, (bx, by))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # 鼠标轮询
    mx, my = pygame.mouse.get_pos()
    if start:
        tx = mx - t_rect.width / 2
    screen.blit(tray, (tx, ty))

    m1, m2, m3 = pygame.mouse.get_pressed()
    # print(m1,m2,m3)

    # 计算比率
    # print((mx - (bx+16)) /(abs(my - (by+16))))

    if start == 0:
        pygame.draw.line(screen, WHITE, (bx + 16, by + 16), (mx, my))
    if m1 == 1:
        flag = 1
    if flag:
        start = 1
        speedx = 2*(mx - (bx+16)) /(abs(my - (by+16)))
        speedy = -1*2
        flag = 0

    # 摆放砖块
    for j in range(15):
        x = lbx[j]
        y = lby[j]
        #  底边碰撞 + 顶边碰撞
        if by < lby[j] + height < by + ball_rect.height and \
                lbx[j] < bx + 16 < lbx[j] + width or \
                by < lby[j] < by + ball_rect.height and \
                lbx[j] < bx + 16 < lbx[j] + width:  # 在某块砖的范围
            lbx[j] = -200
            lby[j] = -200
            speedy = -speedy
        screen.blit(block, (x, y))

    bx += speedx
    by += speedy
    # print((tx,bx,tx + t_rect.width), (by+32, ty),(speedx,speedy))

    if bx < 0 or bx > 800 - 32:
        speedx = -speedx
    if by < 0 or \
            by + 32 > ty and \
            bx + 32 > tx and \
            bx < tx + t_rect.width:
        speedy = -speedy

    pygame.display.update()
