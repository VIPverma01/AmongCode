import pygame
import random
import math

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("my first game")
icon = pygame.image.load("LOGO.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")

# -----------------player--------#

ufo_icon = pygame.image.load("ufo.png")
player_x = 700
player_y = 500


def player(player__x, player__y):
    screen.blit(ufo_icon, (player__x, player__y))


player_change_horizontally = 0
player_change_vertically = 0
player_rate_h = 50
player_rate_v = 50

# ------------enemy------------#
# so every time when new enemy is created this function will call but until this enemy_x and
# enemy_y will get their initial values as random values

enemy=[]
enemy_x=[]
enemy_y=[]
enemy_change_h = []
enemy_change_v = []
enemy_rate_h = []
enemy_rate_v = []
dire = []
num_of_enemies=6
alter=False
for i in range(num_of_enemies):
    enemy.append(pygame.image.load("enemy1.png"))
    enemy_x.append(random.randint(50, 700))
    enemy_y.append(random.randint(50, 250))
    enemy_change_h.append(0)
    enemy_change_v.append(0)
    enemy_rate_h.append(i+1)
    enemy_rate_v.append(i + 1)
    if alter:
        #dire ==False means going left
        dire.append(alter)
        alter=False
    else:
        dire.append(alter)
        alter=True


def enemy1(enemy_,enemy__x, enemy__y):   #passing i to denote making i th enemy
    screen.blit(enemy_, (enemy__x, enemy__y))

# ----------bullet--------#

bullet_type_1 = pygame.image.load("bullet.png")
bullet_speed = 10
bullet_x = player_x
bullet_y = player_y
def bullet(bullet__x, bullet__y):
    screen.blit(bullet_type_1, (bullet__x, bullet__y))

fired = False

# ---------collison of bullet and enemy------------------#

def collison(enemy_x, enemy_y, bullet_x, bullet_y):
    d = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if d < 30:
        return True
    return False

#-------------------COLLISON BETWEEN ENEMY AND PLAYER---------------#

def collision_part_two(enemy_x,enemy_y,player_x,player_y):
    d = math.sqrt(math.pow(enemy_x - player_x, 2) + math.pow(enemy_y - player_y, 2))
    if d < 50:
        return True
    return False

#------------------SCORE---------------#

score_value=0
high_score=0
file_pointer=open("C:/Users/User/MY_PYTHON_PROJECT/game/high_score.txt","r+")
file_pointer.writelines("high_score is:" +str(high_score))
font=pygame.font.Font("aAbrushow.ttf",32)
textX=10
textY=10
def display_score(x,y):
    score=font.render("Score : "+str(score_value),True,(255,200,200))
    screen.blit(score,(x,y))
def display_game_over(x,y):
    ans=font.render("GAME OVER!!! ",True,(255,250,245))
    screen.blit(ans,(x,y))
game_over=False


running = True

while running:
    display_score(textX, textY)
    screen.blit(background, (0, 0))

    player(player_x, player_y)
    for i in range(num_of_enemies):
        enemy1(enemy[i],enemy_x[i], enemy_y[i])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("game ends")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if fired == False:
                    fired = True
                    bullet_y = player_y
                    bullet_x = player_x
                    bullet(player_x, player_y)
            if event.key == pygame.K_RIGHT:
                if (player_x <= 730):
                    player_change_horizontally = player_change_horizontally + player_rate_h
                    player_x = player_change_horizontally + player_x
            if event.key == pygame.K_LEFT:
                if (player_x > 10):
                    player_change_horizontally = player_change_horizontally - player_rate_h

                    player_x = player_change_horizontally + player_x
            if event.key == pygame.K_UP:
                if (player_y >= 10):
                    player_change_vertically = player_change_vertically - player_rate_v

                    player_y = player_change_vertically + player_y
            if event.key == pygame.K_DOWN:
                if (player_y <= 570):
                    player_change_vertically = player_change_vertically + player_rate_v

                    player_y = player_change_vertically + player_y

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass

    # --------------enemy movement--------------#
    for i in range(num_of_enemies):
        if (dire[i] == False):
            enemy_change_h[i] += enemy_rate_h[i]
        else:
            enemy_change_h[i] -= enemy_rate_h[i]
        if (enemy_x[i] <= 10):
            enemy_y[i] = enemy_y[i] + enemy_rate_v[i]
            dire[i] = False
        if (enemy_x[i] >= 736):
            enemy_y[i] = enemy_y[i] + enemy_rate_v[i]
            dire[i] = True

        if (enemy_y[i] == 600):
            enemy_y[i] = random.randint(50, 250)
            enemy_x[i] = random.randint(50, 700)
        enemy_x[i] = enemy_x[i] + enemy_change_h[i]
        enemy_change_v[i] = 0
        enemy_change_h[i] = 0
        enemy1(enemy[i],enemy_x[i], enemy_y[i])
    # ---------------bullet---------#

    if (fired):
        bullet_y = bullet_y - bullet_speed
        bullet(bullet_x, bullet_y)
        if (bullet_y <= 20):
            fired = False
    for i in range(num_of_enemies):
        collide = collison(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collide:
            fired = False
            score_value+=1
            if(score_value >high_score):
                file_pointer.writelines("high_score is: " +str(score_value))
                high_score=score_value
            enemy_x[i] = random.randint(50, 700)
            enemy_y[i] = random.randint(50, 250)

    # ---------player_change----------

    player_change_horizontally = 0
    player_change_vertically = 0
    for i in range(num_of_enemies):
        if collision_part_two(enemy_x[i],enemy_y[i],player_x,player_y):
            screen.fill((0,0,0))
            display_game_over(300,300)
            display_score(400,400)
            pygame.display.update()
            game_over=True
            ans_score=file_pointer.read()
            print(ans_score)
            score_value=0
            break;
    #if game_over:
     #   break;
    player(player_x, player_y)
    if game_over==True:
        break;
    display_score(textX,textY)
    pygame.display.update()
