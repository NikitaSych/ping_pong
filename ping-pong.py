from pygame import *

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
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > win_height - (win_height/100*90):
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - (win_height/100*10):
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > win_height - (win_height/100*90):
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - (win_height/100*10):
            self.rect.y += self.speed

win_height = 800
win_wight = 1534
display.set_caption("SPASE")
window = display.set_mode((win_wight, win_height))
background = ('#99958C')

game = True
clock = time.Clock()
FPS = 20

while True:
     
    for i in event.get():
        if i.type == QUIT:
            game = False

    window.fill(background)
