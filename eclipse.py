import pygame

screen = pygame.display.set_mode((600,400))
background = pygame.image.load("mblack.jpg")
shadow = pygame.image.load("black_circle128.png")
s_rect = shadow.get_rect()
width = s_rect.width
height = s_rect.height
shadow = pygame.transform.scale(shadow,(width*2,height*2))

x,y = 305,8
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(background, (0, 0))

    screen.blit(shadow, (x , y))
    x -= 1
    if x <-200:
        x = 305


    pygame.display.update()