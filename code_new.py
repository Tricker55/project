import pygame
from math import*
from random import*
pygame.init()
pygame.display.set_caption("my game")
screen = pygame.display.set_mode((1000, 600))
h_1=pygame.Rect((350,450),(300,80))
pygame.draw.rect(screen,(0,0,0,0),h_1)
play_button_0 = pygame.image.load('knopka.png')
play_button=pygame.transform.scale(play_button_0,(300,80))
screen.blit(play_button, (350, 450))
pygame.display.flip()
class Mark():
    def __init__(self,value,rect):
        self.value=value
        self.rect=rect
        self.hit=False
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if h_1.collidepoint(mousePos):
                screen.fill((0,0,0))
                def mistake():
                    you_lost_0 = pygame.image.load('lose.png')
                    you_lost = pygame.transform.scale(you_lost_0,(600,100))
                    screen.blit(you_lost,(200,450))
                def winning():
                    you_won_0 = pygame.image.load('win.png')
                    you_won = pygame.transform.scale(you_won_0,(600,100))
                    screen.blit(you_won,(200,450))


                meet=True
                r_2=pygame.image.load('2.png')
                r_3=pygame.image.load('3.png')
                r_4=pygame.image.load('4.png')
                r_5=pygame.image.load('5.png')
                m_2=pygame.transform.scale(r_2,(80,80))
                m_3=pygame.transform.scale(r_3,(80,80))
                m_4=pygame.transform.scale(r_4,(80,80))
                m_5=pygame.transform.scale(r_5,(80,80))
                L=[]
                M=[2,3,4,4,4,4,4,5,5,5,5,5]
                for i in range(48):
                    L.append(Mark(choice(M),pygame.Rect((i%12)*80+20,(i//12)*80+60,80,80)))
                    if(L[i].value==2):
                        screen.blit(m_2,((i%12)*80+20,(i//12)*80+60))
                    if(L[i].value==3):
                        screen.blit(m_3,((i%12)*80+20,(i//12)*80+60))
                    if(L[i].value==4):
                        screen.blit(m_4,((i%12)*80+20,(i//12)*80+60))
                    if(L[i].value==5):
                        screen.blit(m_5,((i%12)*80+20,(i//12)*80+60))
                pygame.draw.line(screen, (255,255,255), [0,0],[0,600],10 )
                pygame.draw.line(screen, (255,255,255), [0,0],[1000,0],10 )
                pygame.draw.line(screen, (255,255,255), [1000,600],[1000,0],10 )
                pygame.draw.line(screen, (255,255,255), [1000,600],[0,600],10 )
                pygame.draw.circle(screen,(160,128,96),(500,550),8)
                pygame.display.flip()
                run = True
                while (run):
                    meet=True
                    complete=True
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                mousePos = pygame.mouse.get_pos()
                                x=mousePos[0]
                                y=mousePos[1]
                                z=sqrt((x-500)*(x-500)+(y-550)*(y-550))
                                cos_a=radians((y-550)/z)
                                sin_a=radians((x-500)/z)
                                x_1=500
                                y_1=550
                                ball=pygame.draw.circle(surface=screen,color=(160,128,96),center=[x_1,y_1],radius=8)

                                while(meet==True):
                                    if ball.left < 10 or ball.right>990:
                                        sin_a=-sin_a
                                    if ball.top < 10 or ball.bottom>590:
                                        cos_a=-cos_a
                                    ball=pygame.draw.circle(surface=screen,color=(0,0,0),center=[x_1,y_1],radius=8)
                                    x_1+=30*sin_a
                                    y_1+=30*cos_a
                                    ball=pygame.draw.circle(surface=screen,color=(160,128,96),center=[x_1,y_1],radius=8)
                                    pygame.display.flip()
                                    if(x_1<0 or x_1>1000 or y_1<0 or y_1>1000):
                                        meet=False
                                    for i in range(48):
                                        if(L[i].rect.collidepoint(x_1,y_1) and L[i].hit == False):
                                            meet=False
                                            L[i].hit = True
                                            pygame.draw.rect(screen,(0,0,0),L[i])
                                            if(L[i].value==2 or L[i].value==3):
                                                mistake()
                                    for i in range(48):
                                        if((L[i].value==4 or L[i].value==5) and (L[i].hit==False)):
                                            complete=False
                                            break
                                    if(complete==True):
                                        winning()




                                ball=pygame.draw.circle(surface=screen,color=(0,0,0),center=[x_1,y_1],radius=8)
                            ball=pygame.draw.circle(surface=screen,color=(160,128,96),center=[500,550],radius=8)
                    pygame.display.flip()
                pygame.quit()
pygame.quit()