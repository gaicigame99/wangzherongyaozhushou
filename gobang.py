import pygame

screen = pygame.display.set_mode((600, 600))

WHITE = (255,255,255)
# pygame.draw.line(screen,WHITE,(100,100),(600,100))

for i in range(15):
    pygame.draw.line(screen, WHITE, (100, 100+i*20), (380, 100+i*20))
    pygame.draw.line(screen,WHITE,(100 + i * 20,100), (100 + i * 20, 380))

pygame.draw.circle(screen,WHITE,(240,240),5, 5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()