from pico2d import *

class Room:
    def __init__(self):
        self.image = load_image('room.png')

    def draw(self):
        self.image.draw(400,300,800,600)

class PlayerCharacter:
    def __init__(self):
        self.image = load_image('character.png')
        self.image_1 = load_image('character-1.png')
        self.body_frame = 0
        self.x = 400
        self.y = 300

    def update(self):
        self.x += x_dir * 5 * dash
        self.y += y_dir * 5 * dash
        self.body_frame = (self.body_frame + 1) % 10

    def draw(self):

        if x_dir == -1:
            self.image_1.clip_draw(1045 - self.body_frame * 32 - 48 ,810, 40 ,20,self.x - 10,self.y - 35,80,40)
            self.image.clip_draw(240,900,50,30,self.x,self.y,100,60)
        elif x_dir == 1:
            self.image.clip_draw(1 + self.body_frame * 32,810,40,20,self.x - 10,self.y - 35, 80, 40)
            self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)
        elif y_dir == -1:
            self.image.clip_draw(2 + self.body_frame * 32,855,40,20,self.x - 6,self.y - 30, 80, 40 )
            self.image.clip_draw(0, 900, 50, 30, self.x, self.y, 100, 60)
        elif y_dir == 1:
            self.image.clip_draw(2 + self.body_frame * 32, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
            self.image.clip_draw(160, 900, 50, 30, self.x, self.y, 100, 60)
        else:
            if look_x_dir == -1:
                self.image_1.clip_draw(1045 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
                self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)
            elif look_x_dir == 1:
                self.image.clip_draw(1 , 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
                self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)
            elif look_y_dir == 1:
                self.image.clip_draw(2 , 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
                self.image.clip_draw(160, 900, 50, 30, self.x, self.y, 100, 60)
            else:
                self.image.clip_draw(2, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
                self.image.clip_draw(0, 900, 50, 30, self.x, self.y, 100, 60)

class Bullet:
    def __init__(self):
        self.image = load_image('character.png')
        self.x = 1000
        self.y = 1000
        self.x_dir = 0
        self.y_dir = 0

    def update(self):
        self.x += 10 * self.x_dir
        self.y += 10 * self.y_dir

    def draw(self):
        self.image.clip_draw(160, 490, 50, 30, self.x, self.y, 38, 24)



x_dir = 0
y_dir = 0
look_x_dir = 0
look_y_dir = -1
dash = 1
bullet_num = 0
def handle_events():
    global running
    global x_dir
    global y_dir
    global dash
    global look_x_dir
    global look_y_dir
    global bullets
    global bullet_num

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x_dir += 1
            elif event.key == SDLK_LEFT:
                x_dir -= 1
            elif event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1
            elif event.key == SDLK_z: # 대시
                dash = 2
            elif event.key == SDLK_x: # 탄환 발사
                bullets[bullet_num].x = player.x
                bullets[bullet_num].y = player.y
                if x_dir == 0 and y_dir == 0:
                    bullets[bullet_num].x_dir = look_x_dir
                    bullets[bullet_num].y_dir = look_y_dir
                else:
                    bullets[bullet_num].x_dir = x_dir
                    bullets[bullet_num].y_dir = y_dir
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                x_dir -= 1
                look_x_dir = 1
                look_y_dir = 0
            elif event.key == SDLK_LEFT:
                x_dir += 1
                look_x_dir = -1
                look_y_dir = 0
            elif event.key == SDLK_UP:
                y_dir -= 1
                look_x_dir = 0
                look_y_dir = 1
            elif event.key == SDLK_DOWN:
                y_dir += 1
                look_x_dir = 0
                look_y_dir = -1
            elif event.key == SDLK_z:
                dash = 1
            elif event.key == SDLK_x:
                bullet_num = (bullet_num + 1) % 10


open_canvas()

room = Room()
player = PlayerCharacter()
bullets = [Bullet() for i in range(10)]

running = True

while running:
    handle_events()
    for bullet in bullets:
        bullet.update()
    player.update()
    clear_canvas()
    room.draw()
    for bullet in bullets:
        bullet.draw()
    player.draw()
    update_canvas()
    delay(0.01)