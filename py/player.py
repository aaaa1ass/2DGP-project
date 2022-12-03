from pico2d import *
import game_framework
import game_world
from bullet import Bullet
import time
import play_state

RD, LD, UD, DD,RU, LU, UU, DU, X ,ZU, ZD= range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYUP, SDLK_UP) : UU,
    (SDL_KEYUP, SDLK_DOWN) : DU,
    (SDL_KEYDOWN, SDLK_x) : X,
    (SDL_KEYDOWN, SDLK_z) : ZD,
    (SDL_KEYUP, SDLK_z) : ZU

}

class IDLE:
    @staticmethod
    def enter(self,event):
        # print('enter idle')
        pass


    @staticmethod
    def exit(self, event):
        if event == X:
            self.fire()
        # print('exit idle')

    @staticmethod
    def do(self):
        self.body_frame = (self.body_frame + 1) % 10
        pass

    def draw(self):
        if self.damaged == 2 and int(self.body_frame) // 2 == 0:
            pass
        else:
            if self.look_x_dir == -1:
                self.image_1.clip_draw(1045 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
                self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)
            elif self.look_x_dir == 1:
                self.image.clip_draw(1, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
                self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)
            elif self.look_y_dir == 1:
                self.image.clip_draw(2, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
                self.image.clip_draw(160, 900, 50, 30, self.x, self.y, 100, 60)
            else:
                self.image.clip_draw(2, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
                self.image.clip_draw(0, 900, 50, 30, self.x, self.y, 100, 60)

PIXEL_PER_METER = (30.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 16

class RUN_1:
    def enter(self,event):
        self.x_dir = -0.7
        self.y_dir = 0.7

    def exit(self, event):
        self.look_x_dir = -1
        self.look_y_dir = 1
        if event == X:
            self.fire()
        if event == ZD:
            self.dash()
        if event == ZU:
            self.walk()
    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time
        pass
    def draw(self):
        if self.damaged == 2 and int(self.body_frame) // 2 == 0:
            pass
        else:
            self.image_1.clip_draw(1045 - int(self.body_frame) * 32 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
            self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)
class RUN_2:
    def enter(self,event):
        self.x_dir = 0
        self.y_dir = 1

    def exit(self, event):
        self.look_x_dir = 0
        self.look_y_dir = 1
        if event == X:
            self.fire()
        if event == ZD:
            self.dash()
        if event == ZU:
            self.walk()
    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        if self.damaged == 2 and int(self.body_frame) // 2 == 0:
            pass
        else:
            self.image.clip_draw(2 + int(self.body_frame) * 32, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
            self.image.clip_draw(160, 900, 50, 30, self.x, self.y, 100, 60)
class RUN_3:
    def enter(self, event):
        self.x_dir = 0.7
        self.y_dir = 0.7

    def exit(self, event):
        self.look_x_dir = 1
        self.look_y_dir = 1
        if event == X:
            self.fire()
        if event == ZD:
            self.dash()
        if event == ZU:
            self.walk()

    def do(self):
        self.body_frame = (self.body_frame  + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        if self.damaged == 2 and int(self.body_frame) // 2 == 0:
            pass
        else:
            self.image.clip_draw(1 + int(self.body_frame) * 32, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
            self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)
class RUN_4:
    def enter(self,event):
        self.x_dir = -1
        self.y_dir = 0

    def exit(self, event):
        self.look_x_dir = -1
        self.look_y_dir = 0
        if event == X:
            self.fire()
        if event == ZD:
            self.dash()
        if event == ZU:
            self.walk()
    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        if self.damaged == 2 and int(self.body_frame) // 2 == 0:
            pass
        else:
            self.image_1.clip_draw(1045 - int(self.body_frame) * 32 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
            self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)
class RUN_6:
    def enter(self,event):
        self.x_dir = 1
        self.y_dir = 0

    def exit(self, event):
        self.look_x_dir = 1
        self.look_y_dir = 0
        if event == X:
            self.fire()
        if event == ZD:
            self.dash()
        if event == ZU:
            self.walk()
    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        if self.damaged == 2 and int(self.body_frame) // 2 == 0:
            pass
        else:
            self.image.clip_draw(1 + int(self.body_frame) * 32, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
            self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)
class RUN_7:
    def enter(self, event):
        self.x_dir = -0.7
        self.y_dir = -0.7

    def exit(self, event):
        self.look_x_dir = -1
        self.look_y_dir = -1
        if event == X:
            self.fire()
        if event == ZD:
            self.dash()
        if event == ZU:
            self.walk()

    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        if self.damaged == 2 and int(self.body_frame) // 2 == 0:
            pass
        else:
            self.image_1.clip_draw(1045 - int(self.body_frame) * 32 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
            self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)
class RUN_8:
    def enter(self, event):
        self.x_dir = 0
        self.y_dir = -1

    def exit(self, event):
        self.look_x_dir = 0
        self.look_y_dir = -1
        if event == X:
            self.fire()
        if event == ZD:
            self.dash()
        if event == ZU:
            self.walk()

    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        if self.damaged == 2 and int(self.body_frame) // 2 == 0:
            pass
        else:
            self.image.clip_draw(2 + int(self.body_frame) * 32, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
            self.image.clip_draw(0, 900, 50, 30, self.x, self.y, 100, 60)
class RUN_9:
    def enter(self, event):
        self.x_dir = 0.7
        self.y_dir = -0.7

    def exit(self,event):
        self.look_x_dir = 1
        self.look_y_dir = -1
        if event == X:
            self.fire()
        if event == ZD:
            self.dash()
        if event == ZU:
            self.walk()

    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        if self.damaged == 2 and int(self.body_frame) // 2 == 0:
            pass
        else:
            self.image.clip_draw(1 + int(self.body_frame) * 32, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
            self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)

next_state = {
    IDLE: { RU : RUN_4, LU : RUN_6, RD : RUN_6, LD : RUN_4, UU : RUN_8, DU : RUN_2, UD : RUN_2, DD : RUN_8, X : IDLE, ZD : IDLE, ZU : IDLE},
    RUN_1:{ RU : RUN_1, LU : RUN_2, LD : RUN_1, RD : RUN_2, UU : RUN_4, DU : RUN_1, UD : RUN_1, DD : RUN_4, X : RUN_1, ZD : RUN_1, ZU : RUN_1},
    RUN_2:{ RU : RUN_1, LU : RUN_3, LD : RUN_1, RD : RUN_3, UU : IDLE , DU : RUN_2, UD : RUN_2, DD : IDLE  ,X : RUN_2, ZD : RUN_2, ZU : RUN_2},
    RUN_3:{ RU : RUN_2, LU : RUN_3, LD : RUN_2, RD : RUN_3, UU : RUN_6, DU : RUN_3, UD : RUN_3, DD : RUN_6 ,X : RUN_3, ZD : RUN_3, ZU : RUN_3},
    RUN_4:{ RU : RUN_4, LU : IDLE , LD : RUN_4, RD : IDLE , UU : RUN_7, DU : RUN_1, UD : RUN_1, DD : RUN_7,X : RUN_4 , ZD : RUN_4, ZU : RUN_4},
    RUN_6:{ RU : IDLE , LU : RUN_6, LD : IDLE , RD : RUN_6, UU : RUN_9, DU : RUN_3, UD : RUN_3, DD : RUN_9,X : RUN_6 , ZD : RUN_6, ZU : RUN_6},
    RUN_7:{ RU : RUN_7, LU : RUN_8, LD : RUN_7, RD : RUN_8, UU : RUN_7, DU : RUN_4, UD : RUN_4, DD : RUN_7 ,X : RUN_7, ZD : RUN_7, ZU : RUN_7},
    RUN_8:{ RU : RUN_7, LU : RUN_9, LD : RUN_7, RD : RUN_9, UU : RUN_8, DU : IDLE , UD : IDLE , DD : RUN_8 ,X : RUN_8, ZD : RUN_8, ZU : RUN_8},
    RUN_9:{ RU : RUN_8, LU : RUN_9, LD : RUN_8, RD : RUN_9, UU : RUN_9, DU : RUN_6, UD : RUN_6, DD : RUN_9 ,X : RUN_9, ZD : RUN_9, ZU : RUN_9},
}

class PlayerCharacter:
    def add_event(self,key_event):
        self.q.insert(0,key_event)

    def __init__(self):
        self.image = load_image('image\character.png')
        self.image_1 = load_image('image\character-1.png')
        self.image_heart = load_image('image\heart.png')
        self.image_exp = load_image('image\exp.png')
        self.body_frame = 0
        self.x = 400
        self.y = 300
        self.x_dir, self.y_dir, self.look_x_dir, self.look_y_dir = 0, 0, 0, -1
        self.cool_down = 0
        self.fire_time = 0
        self.cool_down_time = 0.5
        self.god_time = 1
        self.damaged = 0
        self.max_hp = 5
        self.hp = self.max_hp
        self.font = load_font('ENCR10B.TTF', 32)

        self.level = 1
        self.exp = 0
        self.levelup_exp = 100
        self.dexp = 20

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

    def handle_event(self, event):  # event : 키 입력 이벤트
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def update(self,x,y):
        self.cur_state.do(self)
        if self.cool_down == 1:
            self.fire_time = time.time() + self.cool_down_time
            self.cool_down = 2
        if self.cool_down == 2 and self.fire_time < time.time():
                self.cool_down = 0

        if self.damaged == 1:
            self.damage_time = time.time() + self.god_time
            self.damaged = 2
        if self.damaged == 2 and self.damage_time < time.time():
            self.damaged = 0

        if self.exp >= self.levelup_exp:
            self.level += 1
            self.exp -= self.levelup_exp
            self.levelup_exp *= (self.dexp / 100 + 1)



        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self,event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self,event)


        if self.x < 110: self.x = 110
        if self.y < 140: self.y = 140
        if self.x > 700: self.x = 700
        if self.y > 500: self.y = 500

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(400,50,str(self.level),(0,255,0))
        for i in range(self.max_hp):
            if i >= self.hp:
                self.image_heart.clip_draw(0,121,75,50,100 + i * 50,550)
            else:
                self.image_heart.clip_draw(0,250,75,50,100 + i * 50,550)

        self.image_exp.clip_draw(900,0,50,30,0,0,1600,30)
        self.image_exp.clip_draw(200,0,50,30,0,0,self.exp/self.levelup_exp * 1600,30)

        # draw_rectangle(*self.get_bb())

    def fire(self):
        if self.cool_down == 0:
            if self.cur_state == IDLE:
                bullet = Bullet(self.x, self.y, self.look_x_dir, self.look_y_dir, 1)
            else:
                bullet = Bullet(self.x, self.y, self.x_dir, self.y_dir, 1)
            self.cool_down = 1
            game_world.add_object(bullet,1)


    def dash(self):
        global RUN_SPEED_PPS
        RUN_SPEED_KMPH = 20.0
        RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def walk(self):
        global RUN_SPEED_PPS
        RUN_SPEED_KMPH = 10.0
        RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def get_bb(self):
        return self.x -22, self.y - 42, self.x + 18, self.y - 2

    def handle_collision(self,other,group):
        for i in range(play_state.room.enemy_num):
            if group == 'p:e'+ str(i) and self.damaged == 0:
                self.hp -= 1
                self.damaged = 1
        # if group == 'p:e1' and self.damaged == 0:




