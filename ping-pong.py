from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_sprite, player_x, player_y, player_speed, wight, hight):
        
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_sprite), (wight, hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > win_height - (win_height/100*95):
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - (win_height/100*15):
            self.rect.y += self.speed

    def move_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > win_height - (win_height/100*95):
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - (win_height/100*15):
            self.rect.y += self.speed

    def avto(self):

        global speed_x
        global speed_y

        if random_y == 1:
            self.rect.y += speed_y
        else:
            self.rect.y -= speed_y
        if random_x == 1:
            self.rect.x += speed_x
        else:
            self.rect.x -= speed_x
        if self.rect.y > win_height - 17:
            speed_y = speed_y*-1
        if self.rect.y < 5:
            speed_y = speed_y*-1
        if sprite.collide_rect(ball, player1) == True:
            speed_x = speed_x*-1*1.1
        if sprite.collide_rect(ball, player2) == True:
            speed_x = speed_x*-1*1.1

random_y = randint(0,1)
random_x = randint(0,1)
win_height = 830
win_wight = 1534
display.set_caption("SPASE")
window = display.set_mode((win_wight, win_height))
background = transform.scale(image.load('Green eagle.jpg'), (win_wight, win_height))

player1 = Player('pixil-frame-0 (7.png', win_wight - (win_wight/100*10), win_height/2, 10, 20, 100)
player2 = Player('pixil-frame-0 (7 — копия.png', win_wight - (win_wight/100*90), win_height/2, 10, 20, 100)
ball = Player('pixil-frame-0 (7).png',(win_wight/2), (win_height/2), 3, 30, 30)

game = True
clock = time.Clock()
FPS = 60

speed_y = 3
speed_x = 3

while game:

    for i in event.get():
        if i.type == QUIT:
            game = False

    if ball.rect.x < 0 or ball.rect.x > win_wight:
        break

    window.blit(background, (0,0))
    player2.move_l()
    player1.move_r()
    ball.avto()

    player1.reset()
    player2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
