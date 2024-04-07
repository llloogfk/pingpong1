from pygame import *
win_width = 700
win_height = 500
fon = 'fon.jpg'
img_racket1 = 'racket.png'
img_racket2 = 'racket.png'
img_boll = 'boll.png'
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[W_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[S_Down] and self.rect.x < win_width - 90:
            self.rect.x += self.speed
    def reset(self):
         window.blit(self.image, (self.rect.x, self.rect.y))

display.set_caption("pinpong")
window = display.set_mode((win_width, win_height))


racket1.update()
racket2.update()
boll.update()
racket1.reset()
racket2.reset()
boll.reset()
racket1.draw(window)
racket2.draw(window)
boll.draw(window)
clock = time.Clock()
FPS = 60
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
             

    display.update()
    clock.tick(FPS)