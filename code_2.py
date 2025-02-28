import pygame
from math import*
pygame.init()
pygame.display.set_caption("my game")
screen = pygame.display.set_mode((1000, 600))
h_1=pygame.Rect((350,450),(300,80))
pygame.draw.rect(screen,(0,0,0,0),h_1)
play_button_0 = pygame.image.load('knopka.png')
play_button=pygame.transform.scale(play_button_0,(300,80))
screen.blit(play_button, (350, 450))
pygame.display.flip()
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
                screen.blit(m_5,(20,60))
                screen.blit(m_4,(100,60))
                screen.blit(m_3,(180,60))
                screen.blit(m_4,(260,60))
                screen.blit(m_2,(340,60))
                screen.blit(m_5,(420,60))
                screen.blit(m_4,(500,60))
                screen.blit(m_3,(580,60))
                screen.blit(m_5,(660,60))
                screen.blit(m_4,(740,60))
                screen.blit(m_2,(820,60))
                screen.blit(m_5,(900,60))
                screen.blit(m_3,(20,140))
                screen.blit(m_5,(100,140))
                screen.blit(m_5,(180,140))
                screen.blit(m_4,(260,140))
                screen.blit(m_4,(340,140))
                screen.blit(m_3,(420,140))
                screen.blit(m_4,(500,140))
                screen.blit(m_5,(580,140))
                screen.blit(m_4,(660,140))
                screen.blit(m_2,(740,140))
                screen.blit(m_4,(820,140))
                screen.blit(m_4,(900,140))
                screen.blit(m_5,(20,220))
                screen.blit(m_5,(100,220))
                screen.blit(m_4,(180,220))
                screen.blit(m_5,(260,220))
                screen.blit(m_4,(340,220))
                screen.blit(m_5,(420,220))
                screen.blit(m_2,(500,220))
                screen.blit(m_4,(580,220))
                screen.blit(m_5,(660,220))
                screen.blit(m_5,(740,220))
                screen.blit(m_4,(820,220))
                screen.blit(m_5,(900,220))
                screen.blit(m_5,(20,300))
                screen.blit(m_2,(100,300))
                screen.blit(m_4,(180,300))
                screen.blit(m_5,(260,300))
                screen.blit(m_4,(340,300))
                screen.blit(m_5,(420,300))
                screen.blit(m_4,(500,300))
                screen.blit(m_4,(580,300))
                screen.blit(m_3,(660,300))
                screen.blit(m_5,(740,300))
                screen.blit(m_4,(820,300))
                screen.blit(m_5,(900,300))
                sq_1=pygame.Rect(20,60,80,80)
                sq_2=pygame.Rect(100,60,80,80)
                sq_3=pygame.Rect(180,60,80,80)
                sq_4=pygame.Rect(260,60,80,80)
                sq_5=pygame.Rect(340,60,80,80)
                sq_6=pygame.Rect(420,60,80,80)
                sq_7=pygame.Rect(500,60,80,80)
                sq_8=pygame.Rect(580,60,80,80)
                sq_9=pygame.Rect(660,60,80,80)
                sq_10=pygame.Rect(740,60,80,80)
                sq_11=pygame.Rect(820,60,80,80)
                sq_12=pygame.Rect(900,60,80,80)
                sq_13=pygame.Rect(20,140,80,80)
                sq_14=pygame.Rect(100,140,80,80)
                sq_15=pygame.Rect(180,140,80,80)
                sq_16=pygame.Rect(260,140,80,80)
                sq_17=pygame.Rect(340,140,80,80)
                sq_18=pygame.Rect(420,140,80,80)
                sq_19=pygame.Rect(500,140,80,80)
                sq_20=pygame.Rect(580,140,80,80)
                sq_21=pygame.Rect(660,140,80,80)
                sq_22=pygame.Rect(740,140,80,80)
                sq_23=pygame.Rect(820,140,80,80)
                sq_24=pygame.Rect(900,140,80,80)
                sq_25=pygame.Rect(20,220,80,80)
                sq_26=pygame.Rect(100,220,80,80)
                sq_27=pygame.Rect(180,220,80,80)
                sq_28=pygame.Rect(260,220,80,80)
                sq_29=pygame.Rect(340,220,80,80)
                sq_30=pygame.Rect(420,220,80,80)
                sq_31=pygame.Rect(500,220,80,80)
                sq_32=pygame.Rect(580,220,80,80)
                sq_33=pygame.Rect(660,220,80,80)
                sq_34=pygame.Rect(740,220,80,80)
                sq_35=pygame.Rect(820,220,80,80)
                sq_36=pygame.Rect(900,220,80,80)
                sq_37=pygame.Rect(20,300,80,80)
                sq_38=pygame.Rect(100,300,80,80)
                sq_39=pygame.Rect(180,300,80,80)
                sq_40=pygame.Rect(260,300,80,80)
                sq_41=pygame.Rect(340,300,80,80)
                sq_42=pygame.Rect(420,300,80,80)
                sq_43=pygame.Rect(500,300,80,80)
                sq_44=pygame.Rect(580,300,80,80)
                sq_45=pygame.Rect(660,300,80,80)
                sq_46=pygame.Rect(740,300,80,80)
                sq_47=pygame.Rect(820,300,80,80)
                sq_48=pygame.Rect(900,300,80,80)
                n_1=0
                n_2=0
                n_3=0
                n_4=0
                n_5=0
                n_6=0
                n_7=0
                n_8=0
                n_9=0
                n_10=0
                n_11=0
                n_12=0
                n_13=0
                n_14=0
                n_15=0
                n_16=0
                n_17=0
                n_18=0
                n_19=0
                n_20=0
                n_21=0
                n_22=0
                n_23=0
                n_24=0
                n_25=0
                n_26=0
                n_27=0
                n_28=0
                n_29=0
                n_30=0
                n_31=0
                n_32=0
                n_33=0
                n_34=0
                n_35=0
                n_36=0
                n_37=0
                n_38=0
                n_39=0
                n_40=0
                n_41=0
                n_42=0
                n_43=0
                n_44=0
                n_45=0
                n_46=0
                n_47=0
                n_48=0


                pygame.draw.line(screen, (255,255,255), [0,0],[0,600],10 )
                pygame.draw.line(screen, (255,255,255), [0,0],[1000,0],10 )
                pygame.draw.line(screen, (255,255,255), [1000,600],[1000,0],10 )
                pygame.draw.line(screen, (255,255,255), [1000,600],[0,600],10 )
                pygame.draw.circle(screen,(160,128,96),(500,550),8)
                pygame.display.flip()
                run = True
                while (run):
                    meet=True
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
                                    if(sq_1.collidepoint(x_1,y_1) and n_1==0):
                                        meet=False
                                        n_1=1
                                        pygame.draw.rect(screen,(0,0,0),sq_1)
                                    if(sq_2.collidepoint(x_1,y_1) and n_2==0):
                                        meet=False
                                        n_2=1
                                        pygame.draw.rect(screen,(0,0,0),sq_2)
                                    if(sq_3.collidepoint(x_1,y_1) and n_3==0):
                                        meet=False
                                        n_3=1
                                        pygame.draw.rect(screen,(0,0,0),sq_3)
                                        mistake()
                                    if(sq_4.collidepoint(x_1,y_1) and n_4==0):
                                        meet=False
                                        n_4=1
                                        pygame.draw.rect(screen,(0,0,0),sq_4)
                                    if(sq_5.collidepoint(x_1,y_1) and n_5==0):
                                        meet=False
                                        n_5=1
                                        pygame.draw.rect(screen,(0,0,0),sq_5)
                                        mistake()
                                    if(sq_6.collidepoint(x_1,y_1) and n_6==0):
                                        meet=False
                                        n_6=1
                                        pygame.draw.rect(screen,(0,0,0),sq_6)
                                    if(sq_7.collidepoint(x_1,y_1) and n_7==0):
                                        meet=False
                                        n_7=1
                                        pygame.draw.rect(screen,(0,0,0),sq_7)
                                    if(sq_8.collidepoint(x_1,y_1) and n_8==0):
                                        meet=False
                                        n_8=1
                                        pygame.draw.rect(screen,(0,0,0),sq_8)
                                        mistake()
                                    if(sq_9.collidepoint(x_1,y_1) and n_9==0):
                                        meet=False
                                        n_9=1
                                        pygame.draw.rect(screen,(0,0,0),sq_9)
                                    if(sq_10.collidepoint(x_1,y_1) and n_10==0):
                                        meet=False
                                        n_10=1
                                        pygame.draw.rect(screen,(0,0,0),sq_10)
                                    if(sq_11.collidepoint(x_1,y_1) and n_11==0):
                                        meet=False
                                        n_11=1
                                        pygame.draw.rect(screen,(0,0,0),sq_11)
                                        mistake()
                                    if(sq_12.collidepoint(x_1,y_1) and n_12==0):
                                        meet=False
                                        n_12=1
                                        pygame.draw.rect(screen,(0,0,0),sq_12)
                                    if(sq_13.collidepoint(x_1,y_1) and n_13==0):
                                        meet=False
                                        n_13=1
                                        pygame.draw.rect(screen,(0,0,0),sq_13)
                                        mistake()
                                    if(sq_14.collidepoint(x_1,y_1) and n_14==0):
                                        meet=False
                                        n_14=1
                                        pygame.draw.rect(screen,(0,0,0),sq_14)
                                    if(sq_15.collidepoint(x_1,y_1) and n_15==0):
                                        meet=False
                                        n_15=1
                                        pygame.draw.rect(screen,(0,0,0),sq_15)
                                    if(sq_16.collidepoint(x_1,y_1) and n_16==0):
                                        meet=False
                                        n_16=1
                                        pygame.draw.rect(screen,(0,0,0),sq_16)
                                    if(sq_17.collidepoint(x_1,y_1) and n_17==0):
                                        meet=False
                                        n_17=1
                                        pygame.draw.rect(screen,(0,0,0),sq_17)
                                    if(sq_18.collidepoint(x_1,y_1) and n_18==0):
                                        meet=False
                                        n_18=1
                                        pygame.draw.rect(screen,(0,0,0),sq_18)
                                        mistake()
                                    if(sq_19.collidepoint(x_1,y_1) and n_19==0):
                                        meet=False
                                        n_19=1
                                        pygame.draw.rect(screen,(0,0,0),sq_19)
                                    if(sq_20.collidepoint(x_1,y_1) and n_20==0):
                                        meet=False
                                        n_20=1
                                        pygame.draw.rect(screen,(0,0,0),sq_20)
                                    if(sq_21.collidepoint(x_1,y_1) and n_21==0):
                                        meet=False
                                        n_21=1
                                        pygame.draw.rect(screen,(0,0,0),sq_21)
                                    if(sq_22.collidepoint(x_1,y_1) and n_22==0):
                                        meet=False
                                        n_22=1
                                        pygame.draw.rect(screen,(0,0,0),sq_22)
                                        mistake()
                                    if(sq_23.collidepoint(x_1,y_1) and n_23==0):
                                        meet=False
                                        n_23=1
                                        pygame.draw.rect(screen,(0,0,0),sq_23)
                                    if(sq_24.collidepoint(x_1,y_1) and n_24==0):
                                        meet=False
                                        n_24=1
                                        pygame.draw.rect(screen,(0,0,0),sq_24)
                                    if(sq_25.collidepoint(x_1,y_1) and n_25==0):
                                        meet=False
                                        n_25=1
                                        pygame.draw.rect(screen,(0,0,0),sq_25)
                                    if(sq_26.collidepoint(x_1,y_1) and n_26==0):
                                        meet=False
                                        n_26=1
                                        pygame.draw.rect(screen,(0,0,0),sq_26)
                                    if(sq_27.collidepoint(x_1,y_1) and n_27==0):
                                        meet=False
                                        n_27=1
                                        pygame.draw.rect(screen,(0,0,0),sq_27)
                                    if(sq_28.collidepoint(x_1,y_1) and n_28==0):
                                        meet=False
                                        n_28=1
                                        pygame.draw.rect(screen,(0,0,0),sq_28)
                                    if(sq_29.collidepoint(x_1,y_1) and n_29==0):
                                        meet=False
                                        n_29=1
                                        pygame.draw.rect(screen,(0,0,0),sq_29)
                                    if(sq_30.collidepoint(x_1,y_1) and n_30==0):
                                        meet=False
                                        n_30=1
                                        pygame.draw.rect(screen,(0,0,0),sq_30)
                                    if(sq_31.collidepoint(x_1,y_1) and n_31==0):
                                        meet=False
                                        n_31=1
                                        pygame.draw.rect(screen,(0,0,0),sq_31)
                                        mistake()
                                    if(sq_32.collidepoint(x_1,y_1) and n_32==0):
                                        meet=False
                                        n_32=1
                                        pygame.draw.rect(screen,(0,0,0),sq_32)
                                    if(sq_33.collidepoint(x_1,y_1) and n_33==0):
                                        meet=False
                                        n_33=1
                                        pygame.draw.rect(screen,(0,0,0),sq_33)
                                    if(sq_34.collidepoint(x_1,y_1) and n_34==0):
                                        meet=False
                                        n_34=1
                                        pygame.draw.rect(screen,(0,0,0),sq_34)
                                    if(sq_35.collidepoint(x_1,y_1) and n_35==0):
                                        meet=False
                                        n_35=1
                                        pygame.draw.rect(screen,(0,0,0),sq_35)
                                    if(sq_36.collidepoint(x_1,y_1) and n_36==0):
                                        meet=False
                                        n_36=1
                                        pygame.draw.rect(screen,(0,0,0),sq_36)
                                    if(sq_37.collidepoint(x_1,y_1) and n_37==0):
                                        meet=False
                                        n_37=1
                                        pygame.draw.rect(screen,(0,0,0),sq_37)
                                    if(sq_38.collidepoint(x_1,y_1) and n_38==0):
                                        meet=False
                                        n_38=1
                                        pygame.draw.rect(screen,(0,0,0),sq_38)
                                        mistake()
                                    if(sq_39.collidepoint(x_1,y_1) and n_39==0):
                                        meet=False
                                        n_39=1
                                        pygame.draw.rect(screen,(0,0,0),sq_39)
                                    if(sq_40.collidepoint(x_1,y_1) and n_40==0):
                                        meet=False
                                        n_40=1
                                        pygame.draw.rect(screen,(0,0,0),sq_40)
                                    if(sq_41.collidepoint(x_1,y_1) and n_41==0):
                                        meet=False
                                        n_41=1
                                        pygame.draw.rect(screen,(0,0,0),sq_41)
                                    if(sq_42.collidepoint(x_1,y_1) and n_42==0):
                                        meet=False
                                        n_42=1
                                        pygame.draw.rect(screen,(0,0,0),sq_42)
                                    if(sq_43.collidepoint(x_1,y_1) and n_43==0):
                                        meet=False
                                        n_43=1
                                        pygame.draw.rect(screen,(0,0,0),sq_43)
                                    if(sq_44.collidepoint(x_1,y_1) and n_44==0):
                                        meet=False
                                        n_44=1
                                        pygame.draw.rect(screen,(0,0,0),sq_44)
                                    if(sq_45.collidepoint(x_1,y_1) and n_45==0):
                                        meet=False
                                        n_45=1
                                        pygame.draw.rect(screen,(0,0,0),sq_45)
                                        mistake()
                                    if(sq_46.collidepoint(x_1,y_1) and n_46==0):
                                        meet=False
                                        n_46=1
                                        pygame.draw.rect(screen,(0,0,0),sq_46)
                                    if(sq_47.collidepoint(x_1,y_1) and n_47==0):
                                        meet=False
                                        n_47=1
                                        pygame.draw.rect(screen,(0,0,0),sq_47)
                                    if(sq_48.collidepoint(x_1,y_1) and n_48==0):
                                        meet=False
                                        n_48=1
                                        pygame.draw.rect(screen,(0,0,0),sq_48)
                                if(n_1==1 and n_2==1 and n_4==1 and n_6==1 and n_7==1 and n_9==1 and n_10==1 and n_12==1 and n_14==1 and n_15==1 and n_16==1 and n_17==1 and n_19==1 and n_20==1 and n_21==1 and n_23==1 and n_24==1 and n_25==1 and n_26==1 and n_27==1 and n_28==1 and n_29==1 and n_30==1 and n_32==1 and n_33==1 and n_34==1 and n_35==1 and n_36==1 and n_37==1 and n_39==1 and n_40==1 and n_41==1 and n_42==1 and n_43==1 and n_44==1 and n_46==1 and n_47==1 and n_48==1):
                                    winning()

                                ball=pygame.draw.circle(surface=screen,color=(0,0,0),center=[x_1,y_1],radius=8)
                            ball=pygame.draw.circle(surface=screen,color=(160,128,96),center=[500,550],radius=8)
                    pygame.display.flip()
                pygame.quit()
pygame.quit()