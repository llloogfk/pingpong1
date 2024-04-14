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
    def reset(self):
         window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_racket1(self):
        keys = key.get_pressed()
        if keys[W_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[S_Down] and self.rect.y < win_width - 90:
            self.rect.y += self.speed

    def update_racket2(self):
        keys = key.get_pressed()
        if keys[W_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[S_Down] and self.rect.y < win_width - 90:
            self.rect.y += self.speed
         

class Boll(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.retc.x >= 640 - 55:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


display.set_caption("pinpong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('Fon.jpg'), (win_width, win_height))         
   
    



finish = False
run = True
clock = time.Clock()
FPS = 60

racket1  = Player('racket.png', 30, 200, 4, 50, 150)
racket2  = Player('racket.png', 520, 200, 4, 50, 150 )
boll = GameSprite('boll.png', 200, 200, 4, 50, 50) 

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
speed_x = 3
speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background, (0, 0))
        racket1.update()
        racket2.update()
        boll.rect.x += speed_x
        boll.rect.y += speed_y
        boll.update()
        racket1.reset()
        racket2.reset()
        boll.reset()
        # racket1.draw(window)
        # racket2.draw(window)
        # boll.draw(window)
        if boll.rect.y > win_height-50 or boll.rect.y < 0:
                speed_y *= -1
        if sprite.collide_rect(racket1,boll) or sprite.collide_rect(racket2,boll):
            speed_x *= -1
        if boll.rect.y > 500-50 or boll.rect.y <0:
            speed_y *= -1
        if boll.rect.x > 700-50 or boll.rect.x <0:
            speed_x *= -1
        if boll.rect.x > 700-50:
            print(lose1)
            break
        if boll.rect.x <0:
            print(lose2)
            break
        
             

    display.update()
    clock.tick(FPS)


#     from pygame import *
# from random import *
# from time import time as  timer
# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')
 
# img_back = "galaxy.jpg" 
# img_hero = "rocket.png" 
# img_enemy = "ufo.png"
# img_bullet = "bullet.png"
# img_ast = "asteroid.png"
# win_width = 700
# win_height = 500
# font.init()
# font1 = font.SysFont('Arial', 80)
# win = font1.render('You Win!', True, (255, 255, 255))
# lose = font1.render('You Lose!', True, (180, 0, 0))
# font2 = font.SysFont('Arial', 36)
# score = 0
# lost = 0
# life = 3

# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

#         super().__init__()
#         self.image = transform.scale(image.load(player_image), (size_x, size_y))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))
# class Player(GameSprite):
#     def update(self):
#         keys = key.get_pressed()
#         if keys[K_LEFT] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys[K_RIGHT] and self.rect.x < win_width - 90:
#             self.rect.x += self.speed
#     def fire(self):
#         bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
#         bullets.add(bullet)

# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost 

#         if self.rect.y > win_height:
#             self.rect.x = randint(80, win_width - 80)
#             self.rect.y = 0 
#             lost = lost + 1

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y < 0:
#             self.kill()

 
# display.set_caption("Shooter")
# window = display.set_mode((win_width, win_height))
# background = transform.scale(image.load(img_back), (win_width, win_height))
# ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
# asteroid = Enemy(img_ast, randint(80, win_width - 80), - 40, 80, 50, randint(1, 5))
# asteroids = sprite.Group()
# for i in range(1, 6):
#     asteroid = Enemy(img_ast, randint(80, win_width - 80), - 40, 80, 50, randint(1, 5))
#     asteroids.add(asteroid)


# monsters = sprite.Group()
# for i in range(1, 6):
#     monster = Enemy(img_enemy, randint(80, win_width - 80), - 40, 80, 50, randint(1, 3))
#     monsters.add(monster)
# bullets = sprite.Group()
# finish = False
# run = True
# sprites_list = sprite.spritecollide(ship, monsters, False)
# clock = time.Clock()
# FPS = 60
# rel_time = False

# num_fire = 0
# while run:
#     for e in event.get():
#         if e.type == QUIT:
#             run = False
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 if num_fire < 5 and rel_time == False:
#                     num_fire = num_fire + 1
#                     fire_sound.play()
#                     ship.fire()

#                 if num_fire >= 5 and rel_time == False:
#                     lost_time = timer()
#                     rel_time = True
    
#     if not finish:
#         window.blit(background,(0,0))
#         text = font2.render("Счёт:" + str(score), 1, (255, 255, 255))
#         window.blit(text, (10, 20))

#         text_lose = font2.render("Пропущенно:" + str(lost), 1, (255, 255, 255))
#         window. blit(text_lose, (10, 50))

#         ship.update()
#         monsters.update()
#         asteroids.update()
#         ship.reset()
#         monsters.draw(window)
#         asteroids.draw(window)
    
#         bullets.update()
#         bullets.draw(window)

#         if rel_time == True:
#             now_time = timer()
#             if now_time - lost_time < 3:
#                 reload = font2.render('Wait, reload...', 1, (150, 0, 0))
#                 window.blit(reload, (250, 450))
#             else:
#                 num_fire = 0
#                 rel_time = False

#         collides = sprite.groupcollide(monsters, bullets, True, True) 
#         for c in collides:
#             score = score + 1
#             monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint (1, 5))
#             monsters.add(monster)

#         if sprite.spritecollide(ship, monsters, True) or sprite.spritecollide(ship, asteroids, True):
#             life = life - 1
#         if life == 0 or lost >= 5:
#             finish = True
#             window.blit(win, (200, 200))
        
#         if score >= 10:
#             finish = True
#             window.blit(lose, (200, 200))

#         if life == 3:
#             life_color = (0, 150, 0)
#         if life == 2:
#             life_color = (150, 150, 0)
#         if life == 1:
#             life_color = (150, 0, 0)

#         text_life = font1.render(str(life), 1, life_color)
#         window.blit(text_life, (650, 10))

#     else:
#         finish = False 
#         score = 0
#         lost = 0
#         life = 3
#         for b in bullets:
#             b.kill()
#         for m in monsters:
#             m.kill()
#         time.delay (3000)
#         for i in range(1, 6):
#             monster = Enemy(img_enemy, randint(80, win_width - 80), - 40, 80, 50, randint(1, 3))
#             monsters.add(monster)


#     display.update()
#     clock.tick(FPS)