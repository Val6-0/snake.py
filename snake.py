import pygame
pygame.init()


dis=pygame.display.set_mode((800,600))

white = (255, 255, 255)
blue=(0,0,255)
black = (0,0,0)
red=(255,0,0)

pygame.display.set_caption('fromage')
game_over=False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_z:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_s:
                y1_change = 10
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis,black,[x1,y1,10,10])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()