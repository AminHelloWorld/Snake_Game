from random import randint
import pygame
pygame.init()

global z,q,my_list,boul,condition,score,win

def start():
    global z,q,my_list,boul,score,win,font,direction,resolution
    direction="UP"
    resolution=500  
    font = pygame.font.SysFont(None, 40)
    win = pygame.display.set_mode((resolution,resolution))
    pygame.display.set_caption("Snake Game")
    score=1
    q=50
    my_list=list()
    boul=0
    if (q*q) % 2 == 0 :
        z=[int((((q*q)-1)/2 +((q*q)+1)/2)/2.0)]
    else:
        z=[int(((q*q)-1)/2)]
        
        
def boule():
    global boul
    if not boul:
        boul=randint(0,q*q-1)
        while boul in z:
            boul=randint(0,q*q-1)

def construire():
    global z, boul, my_list, score
    my_list=[]
    for i in range ((q*q)):
        if i in z[-score:]:
            my_list.append("o")
        elif i==boul:
            my_list.append("0")
        else:
            my_list.append("*")

def imprimer():
    global my_list, q, win, score,font,resolution,z,direction
    win.fill((0,0,0))
    des=resolution/q
    text = font.render(str(score), True, (255, 255, 255))
    for y in range (q):
        my_list2=my_list[q*y:q*(y+1)]
        for x in range (len(my_list2)):
            if my_list2[x]== 'o':
                pygame.draw.rect(win, (0,255,0), (x*des, y*des, des, des))
            if my_list2[x]== '0':
                pygame.draw.rect(win, (255,255,0), (x*des, y*des, des, des))
    if direction=="RIGHT":
        pygame.draw.rect(win, (255,0,0), ((z[-1]%q)*des, (z[-1]//q)*des, 10, 10))
        pygame.draw.rect(win, (255,0,0), ((z[-1]%q)*des, ((z[-1]//q)+1)*des, 10, -10))
    elif direction=="LEFT":
        pygame.draw.rect(win, (255,0,0), (((z[-1]%q)+1)*des, (z[-1]//q)*des, -10, 10))
        pygame.draw.rect(win, (255,0,0), (((z[-1]%q)+1)*des, ((z[-1]//q)+1)*des, -10, -10))
    elif direction=="UP":
        pygame.draw.rect(win, (255,0,0), (((z[-1]%q)+1)*des, ((z[-1]//q)+1)*des, -10, -10))
        pygame.draw.rect(win, (255,0,0), (((z[-1]%q))*des, ((z[-1]//q)+1)*des, 10, -10))
    elif direction=="DOWN":
        pygame.draw.rect(win, (255,0,0), (((z[-1]%q)+1)*des, ((z[-1]//q))*des, -10, 10))
        pygame.draw.rect(win, (255,0,0), (((z[-1]%q))*des, ((z[-1]//q))*des, 10, 10))
    
    
    win.blit(text,(0.9*resolution ,0.9*resolution))

                    
        
def changdirection():
    global direction
    movement=pygame.key.get_pressed()   
    if direction=="UP" or direction=="DOWN":
        if movement[pygame.K_RIGHT]:
            direction="RIGHT"
        elif movement[pygame.K_LEFT]:
            direction="LEFT"
    elif direction=="LEFT" or direction=="RIGHT":
        if movement[pygame.K_UP]:
            direction="UP"
        elif movement[pygame.K_DOWN]:
            direction="DOWN"
    
    
    
    
def mov():
    global z,direction
    x=z[-1]%q
    y=z[-1]//q
    changdirection()
    if direction=="RIGHT":
        x=x+1
        if x==q:
            x=0
    elif direction=="LEFT":
        x=x-1
        if x==-1:
            x=q-1   
    elif direction=="DOWN":
        y=y+1
        if y==q:
            y=0
    elif direction=="UP":
        y=y-1
        if y==-1:
            y=q-1
    if x+y*q != z[-1]:
        z.append(x+y*q)
        z=z[-score:]
    
        
def manger():
    global z, boul,score
    if boul in z:
        score+=1
        boul=False
        

condition=True
start()
while condition==True:
    boule()
    construire()
    imprimer()   
    pygame.display.update() 
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            condition = False
    mov()
    manger()
        
pygame.quit()