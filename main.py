#создай игру "Лабиринт"!
from pygame import *

#создай окно игры
win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height ))
display.set_caption('лабиринт')
#задай фон сцены
background = transform.scale(image.load('background.jpg'),(win_width,win_height))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y,player_speed):
        self.image =  transform.scale(image.load(player_image),(65,65)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x =player_x
        self.rect.y =player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

#обработай событие «клик по кнопке "Закрыть окно"»
run = True
clock = time.Clock()
FPS = 60
player = GameSprite('hero.png',5,win_height -80,4)
monster = GameSprite('cyborg.png',win_width -80,280,2)
final = GameSprite('treasure.png',win_width -120,win_height -80,0 )

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0,0))
    player.reset()
    monster.reset()
    final.reset()
    display.update()
    clock.tick(FPS)


