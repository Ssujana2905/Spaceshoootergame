import pygame
import random  #for generating random enemies
import math
from pygame import mixer

mixer.init()
pygame.init()

mixer.music.load('background.wav')
mixer.music.play(-1)

pygame.init() #initializing
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Shooter Game')
icon=pygame.image.load("aliennew.png") 
pygame.display.set_icon(icon)

backgroundi=pygame.image.load('background.png')
spaceshipimg=pygame.image.load('arcade.png')

enemyimg=[]
enemyX=[]
enemyY=[]
enemyspeedX=[]
enemyspeedY=[]

no_of_enemies=6
for i in range(no_of_enemies):


        enemyimg.append(pygame.image.load('enemy.png'))
        enemyX.append(random.randint(0,736))
        enemyY.append(random.randint(30,150)) #smaller range otherwise enemies appear near to spaceship
        enemyspeedX.append(-1)
        enemyspeedY.append(40)


bulletimg=pygame.image.load('bullet.png')



spaceshipX=370 #near 1/2 of org width
spaceshipY=480 
changeX=0

score=0
check=False
running=True
bulletX=386
bulletY=490  #to make bullet appear f

font=pygame.font.SysFont('Arial',32,'bold')

def  score1():
    img=font.render(f'score:{score}',True,'white') #fstring is used to concatenate string with the variable

    screen.blit(img,(10,10))


font_gameover=pygame.font.SysFont('Arial',64,'bold')
def gameover():
    img_gameover=font_gameover.render('GAME OVER',True,'white')
    screen.blit(img_gameover,(200,250)) #centre





#while true is not used becoz it wont allow us to close window
while running: # without using loop screen time last for only 1 sec
    screen.blit(backgroundi,(0,0)) #blit is used to draw(get) image
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:#for moving spaceship
            if event.key==pygame.K_LEFT:
                changeX=-4 #thi num determines speed
            if event.key==pygame.K_RIGHT:
                changeX=4
            if event.key==pygame.K_SPACE: #pace key
                if check is False:
                    bulletsound=mixer.Sound('laser.wav')
                    bulletsound.play()

                    check=True  #to make bullet diplay only when space is pressed
                    bulletX=spaceshipX+16 #to make bullet come only from spaceship
       
        if event.type==pygame.KEYUP:#COMING BACK TO ORG POS
            changeX=0
    spaceshipX+=changeX

    if spaceshipX <=0: #for not crossing the window
        spaceshipX=0
    elif spaceshipX>=736:#img size is 64px on moving right we need to subtract it from 800
        spaceshipX=736
    for i in range(no_of_enemies):
        if enemyY[i]>420:
            for j in range(no_of_enemies):
                 
                enemyY[j]=2000 #give large value to make enemy disappear when game out
            gameover() 
            break

        enemyX[i]+=enemyspeedX[i]
        if enemyX[i]<=0:
            enemyspeedX[i]=1
            enemyY[i]+=enemyspeedY[i]
        if enemyX[i]>=736:
            enemyspeedX[i]=-1
            enemyY[i]+=enemyspeedY[i] #on touching left and right border it comes down once it is touching our spaceship then gameend
        
        distance=math.sqrt(math.pow(bulletX-enemyX[i],2)+math.pow(bulletY-enemyY[i],2))# sqrt((x1-x2)^2 +(y1-y2)^2)
        if distance<27:
            explosionSound=mixer.Sound('explosion.wav')
            explosionSound.play()
            bulletY=480 #if bullet touches enemy it comes back to org
            check=False
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(30,150)
            score+=1
        screen.blit(enemyimg[i],(enemyX[i],enemyY[i]))
    
    
    #to move it left an right
    if bulletY<=0: # if bullet reaches border again it comes back to org position
        bulletY=490 
        check=False #when user press spacebar key again only when bullet will come
    if check:
        screen.blit(bulletimg,(bulletX,bulletY))
        bulletY-=5 #to incre speed
    
    
    
        
    
    screen.blit(spaceshipimg,(spaceshipX,spaceshipY))
  
    score1()
    pygame.display.update()