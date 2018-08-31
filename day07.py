# kick block
import pygame

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("1.jpg")
ball = pygame.image.load("ball32.png")
tray = pygame.image.load("tray2.png")
# 获取到托盘的宽高
t_rect = tray.get_rect()

block = pygame.image.load("block.jpg")
# 获取到砖块的宽高
bl_rect = block.get_rect()
width = bl_rect.width
height = bl_rect.height
# 改变图片的大小
block = pygame.transform.scale(block,(width//2,height//2))
bl_rect = block.get_rect()
width = bl_rect.width
height = bl_rect.height

lbx = []
lby = []
for i in range(3):
    for j in range(5):
         x = 50+j * width+ j*10
         y = 30+i * height+ i*10
         lbx.append(x)
         lby.append(y)

# for j in range(5):
#      x = 50+j * width+ j*10
#         30 + i * height + i * 10
#      y = 30+ height+10
#      lbx.append(x)
#      lby.append(y)
#
# for j in range(5):
#      x = 50+j * width+ j*10
#          30 + i * height + i * 10
#      y = 30+height*2+20
#      lbx.append(x)
#      lby.append(y)


bx,by = 100,100
direction = 0
speedx,speedy = 1,1
tx,ty = 200,500
while True:
    screen.blit(background, (0, 0))
    screen.blit(ball, (bx, by))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # 键盘事件
        # if event.type == pygame.KEYDOWN:
        #     # pygame.K_UP
        #     # pygame.K_DOWN
        #     if event.key == pygame.K_LEFT:
        #         tx -= 15
        #     if event.key == pygame.K_RIGHT:
        #         tx += 15

    #  键盘轮询
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     tx -= 5
    # if keys[pygame.K_RIGHT]:
    #     tx += 5

    # 鼠标轮询
    mx, my = pygame.mouse.get_pos()
    tx = mx - t_rect.width/2
    screen.blit(tray, (tx, ty))

    # 摆放砖块
    # screen.blit(block,(100, 100))
    for j in range(15):
        x = lbx[j]
        y = lby[j]
        screen.blit(block, (x, y))

    bx += speedx
    by += speedy
    if bx <0 or bx > 800-32:
        speedx = -speedx
    # if by <0 or by > 600-32:
    if by <0 or \
            by+32 > ty and \
            bx+32 > tx and \
            bx < tx + t_rect.width:
        speedy = -speedy



    # if direction == 0:
    #     bx += 1
    #     by += 1
    # if direction == 1:
    #     bx += 1
    #     by -= 1
    # if direction == 2:
    #     bx -= 1
    #     by -= 1
    # if direction == 3:
    #     bx -= 1
    #     by += 1
    # if by > 600-32:
    #     if direction == 0:
    #         direction = 1
    #     else:
    #         direction = 2
    # if bx > 800-32:
    #     if direction == 1:
    #         direction = 2
    #     else:
    #         direction = 3
    # if by < 0:
    #     if direction == 2:
    #         direction = 3
    #     else:
    #         direction = 0
    # if bx < 0:
    #     if direction == 3:
    #         direction = 0
    #     else:
    #         direction = 1


    pygame.display.update()