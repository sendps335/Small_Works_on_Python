import time
import pygame
import random

pygame.init()
dis = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Snake(Nokia)")

clock = pygame.time.Clock()

blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

x1 = 400
y1 = 300

x1_change = 0
y1_change = 0

font_style = pygame.font.SysFont("bahnschrift",80)
score_font = pygame.font.SysFont("comicsansms",35)

def our_snake(sl):
    for x in sl:
        pygame.draw.rect(dis,red,[x[0],x[1],10,10])

def message(msg,color,coor):
    mesg = font_style.render(msg,True,color)
    dis.blit(mesg,coor)

def gameloop():
    game_over = False
    game_close = False

    x1 = 500
    y1 = 500

    x1_change = 0
    y1_change = 0

    snake_l = []
    len_snake = 1

    fx = round(random.randrange(0,(1300-10))/10)*10
    fy = round(random.randrange(0,(700-10))/10)*10

    while not game_over:
        while game_close==True:
            dis.fill(white)
            message("Please type q-quit or p-play again",red,[50,200])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_p:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

            if x1>1366 or x1<0 or y1<0 or y1>768:
                game_close = True

            x1=x1+x1_change
            y1=y1+y1_change

            dis.fill(white)
            pygame.draw.rect(dis, (255, 255, 0), [fx, fy, 10, 10])

            snake_h = []
            snake_h.append(x1)
            snake_h.append(y1)
            snake_l.append(snake_h)
            if len(snake_l)>len_snake:
                del snake_l[0]
            for i in snake_l[:-1]:
                if i == snake_h:
                    game_close = True

            our_snake(snake_l)

            sc = len_snake - 1
            message(f"Score:{sc}", (0, 255, 0), [0,0])

            pygame.display.update()

            if x1==fx and y1==fy:
                print("yummy!")
                fx = round(random.randrange(0, (1300 - 10)) / 10) * 10
                fy = round(random.randrange(0, (700 - 10)) / 10) * 10
                len_snake += 1


        clock.tick(30)
    message("Till next time!",blue,[400,300])
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()

gameloop()