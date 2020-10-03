# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
pygame.init()
fpsclock=pygame.time.Clock()
pygame.display.set_caption("Speed Key")
# Set up the drawing window
screen = pygame.display.set_mode([800, 600])
icon=pygame.image.load("game-controller.png")
pygame.display.set_icon(icon)
object_x=pygame.image.load("home-plate.png")
def object(x,y,letter):
    screen.blit(object_x,(x,y))
    font = pygame.font.SysFont(None, 30)
    img = font.render(letter, True, (0,255,0))
    screen.blit(img, (x+22,y+18))

# Run until the user asks to quit
running = True
x=random.randint(0,800-64)
y=random.randint(0,50)
letter="S"
score=0
key='None'
screen.fill((10,10,0))

intro=True
while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro=False
            running=False
    font = pygame.font.Font(None, 36)
    text = font.render("Press any Key To Start", True, (255,255,255))
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                   
        if event.type==pygame.KEYDOWN:
                intro=False
    pygame.display.update()


while running:
    


    screen.fill((10,10,0))
    font = pygame.font.Font(None, 36)
    text = font.render("Score : "+str(score), True, (255,255,255))
    text_rect = text.get_rect()
    text_x = 650
    text_y = 0
    screen.blit(text, [text_x, text_y])
    text = font.render("Key Pressed:"+key, True, (255,255,255))
    text_rect = text.get_rect()
    text_x = 0
    text_y = 0
    screen.blit(text, [text_x, text_y])
    object(x,y,letter)
  
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if not y>550:
            
            if event.type==pygame.KEYDOWN:
                key=pygame.key.name(event.key).upper()  
                if letter == key:
                    score=score+1                    
                    x=random.randint(0,800-64)
                    y=random.randint(0,50)
                    letter=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                else:
                    y=560
            

    # Fill the background with white
    
    y=y+2
    if y>550:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over Score :"+str(score), True, (255,255,255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        
      
   
    
       
    
    pygame.display.update()
    fpsclock.tick(170)
    

# Done! Time to quit.
pygame.quit()