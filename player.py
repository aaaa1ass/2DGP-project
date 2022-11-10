from pico2d import *
import game_framework

RD, LD, UD, DD,RU, LU, UU, DU = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYUP, SDLK_UP) : UU,
    (SDL_KEYUP, SDLK_DOWN) : DU
}

class IDLE:
    @staticmethod
    def enter(self,event):
        print('enter idle')
        self.x_dir = 0
        self.y_dir = 0

    @staticmethod
    def exit(self):
        print('exit idle')

    @staticmethod
    def do(self):
        self.body_frame = (self.body_frame + 1) % 10
        pass

    def draw(self):
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
FRAMES_PER_ACTION = 8

class RUN_1:
    def enter(self,event):
        self.x_dir = -0.7
        self.y_dir = 0.7
    def exit(self):
        self.look_x_dir = -1
        self.look_y_dir = 1
    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time
        pass
    def draw(self):
        self.image_1.clip_draw(1045 - int(self.body_frame) * 32 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
        self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)

class RUN_2:
    def enter(self,event):
        self.x_dir = 0
        self.y_dir = 1
    def exit(self):
        self.look_x_dir = 0
        self.look_y_dir = 1
    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        self.image.clip_draw(2 + int(self.body_frame) * 32, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
        self.image.clip_draw(160, 900, 50, 30, self.x, self.y, 100, 60)


class RUN_3:
    def enter(self, event):
        self.x_dir = 0.7
        self.y_dir = 0.7

    def exit(self):
        self.look_x_dir = 1
        self.look_y_dir = 1

    def do(self):
        self.body_frame = (self.body_frame  + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image.clip_draw(1 + int(self.body_frame) * 32, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
        self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)

class RUN_4:
    def enter(self,event):
        self.x_dir = -1
        self.y_dir = 0
    def exit(self):
        self.look_x_dir = -1
        self.look_y_dir = -1
    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        self.image_1.clip_draw(1045 - int(self.body_frame) * 32 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
        self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)
class RUN_6:
    def enter(self,event):
        self.x_dir = 1
        self.y_dir = 0
    def exit(self):
        self.look_x_dir = 1
        self.look_y_dir = 1
    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        self.image.clip_draw(1 + int(self.body_frame) * 32, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
        self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)

class RUN_7:
    def enter(self, event):
        self.x_dir = -0.7
        self.y_dir = -0.7

    def exit(self):
        self.look_x_dir = -1
        self.look_y_dir = -1

    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image_1.clip_draw(1045 - int(self.body_frame) * 32 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
        self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)


class RUN_8:
    def enter(self, event):
        self.x_dir = 0
        self.y_dir = -1

    def exit(self):
        self.look_x_dir = 0
        self.look_y_dir = -1

    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time
    def draw(self):
        self.image.clip_draw(2 + int(self.body_frame) * 32, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
        self.image.clip_draw(0, 900, 50, 30, self.x, self.y, 100, 60)
class RUN_9:
    def enter(self, event):
        self.x_dir = 0.7
        self.y_dir = -0.7

    def exit(self):
        self.look_x_dir = 1
        self.look_y_dir = -1

    def do(self):
        self.body_frame = (self.body_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image.clip_draw(1 + int(self.body_frame) * 32, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
        self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)


# class RUN:
#     def enter(self,event):
#         print('enter run')
#         self.dir = 0
#
#     def exit(self):
#         print('exit run')
#         self.look_x_dir = self.x_dir
#         self.look_y_dir = self.y_dir
#
#     def do(self):
#         self.body_frame = (self.body_frame + 1) % 10
#         self.x += self.x_dir
#         self.y += self.y_dir
#
#
#     def draw(self):
#         if self.x_dir == -1:
#             self.image_1.clip_draw(1045 - self.body_frame * 32 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
#             self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)
#         elif self.x_dir == 1:
#             self.image.clip_draw(1 + self.body_frame * 32, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
#             self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)
#         elif self.y_dir == -1:
#             self.image.clip_draw(2 + self.body_frame * 32, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
#             self.image.clip_draw(0, 900, 50, 30, self.x, self.y, 100, 60)
#         elif self.y_dir == 1:
#             self.image.clip_draw(2 + self.body_frame * 32, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
#             self.image.clip_draw(160, 900, 50, 30, self.x, self.y, 100, 60)

next_state = {
    IDLE: { RU : RUN_4, LU : RUN_6, RD : RUN_6, LD : RUN_4, UU : RUN_8, DU : RUN_2, UD : RUN_2, DD : RUN_8 },
    RUN_1:{ RU : RUN_1, LU : RUN_2, LD : RUN_1, RD : RUN_2, UU : RUN_4, DU : RUN_1, UD : RUN_1, DD : RUN_4 },
    RUN_2:{ RU : RUN_1, LU : RUN_3, LD : RUN_1, RD : RUN_3, UU : IDLE , DU : RUN_2, UD : RUN_2, DD : IDLE  },
    RUN_3:{ RU : RUN_2, LU : RUN_3, LD : RUN_2, RD : RUN_3, UU : RUN_6, DU : RUN_3, UD : RUN_3, DD : RUN_6 },
    RUN_4:{ RU : RUN_4, LU : IDLE , LD : RUN_4, RD : IDLE , UU : RUN_7, DU : RUN_1, UD : RUN_1, DD : RUN_7 },
    RUN_6:{ RU : IDLE , LU : RUN_6, LD : IDLE , RD : RUN_6, UU : RUN_9, DU : RUN_3, UD : RUN_3, DD : RUN_9 },
    RUN_7:{ RU : RUN_7, LU : RUN_8, LD : RUN_7, RD : RUN_8, UU : RUN_7, DU : RUN_4, UD : RUN_4, DD : RUN_7 },
    RUN_8:{ RU : RUN_7, LU : RUN_9, LD : RUN_7, RD : RUN_9, UU : RUN_8, DU : IDLE , UD : IDLE , DD : RUN_8 },
    RUN_9:{ RU : RUN_8, LU : RUN_9, LD : RUN_8, RD : RUN_9, UU : RUN_9, DU : RUN_6, UD : RUN_6, DD : RUN_9 },
}
class PlayerCharacter:
    def add_event(self,key_event):
        self.q.insert(0,key_event)

    def __init__(self):
        self.image = load_image('character.png')
        self.image_1 = load_image('character-1.png')
        self.body_frame = 0
        self.x = 400
        self.y = 300
        self.x_dir, self.y_dir, self.look_x_dir, self.look_y_dir = 0, 0, 0, 0

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

    def handle_event(self, event):  # event : 키 입력 이벤트
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def update(self):
        self.cur_state.do(self)

        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self,event)

    def draw(self):
        self.cur_state.draw(self)

# class Bullet:
#     def __init__(self):
#         self.image = load_image('character.png')
#         self.x = 1000
#         self.y = 1000
#         self.x_dir = 0
#         self.y_dir = 0
#
#     def update(self):
#         self.x += 10 * self.x_dir
#         self.y += 10 * self.y_dir
#
#     def draw(self):
#         self.image.clip_draw(160, 490, 50, 30, self.x, self.y, 38, 24)
#
#
#
# x_dir = 0
# y_dir = 0
# look_x_dir = 0
# look_y_dir = -1
# dash = 1
# bullet_num = 0
# def handle_events():
#     global running
#     global x_dir
#     global y_dir
#     global dash
#     global look_x_dir
#     global look_y_dir
#     global bullets
#     global bullet_num
#
#     events = get_events()
#
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_KEYDOWN:
#             if event.key == SDLK_RIGHT:
#                 x_dir += 1
#             elif event.key == SDLK_LEFT:
#                 x_dir -= 1
#             elif event.key == SDLK_UP:
#                 y_dir += 1
#             elif event.key == SDLK_DOWN:
#                 y_dir -= 1
#             elif event.key == SDLK_z: # 대시
#                 dash = 2
#             elif event.key == SDLK_x: # 탄환 발사
#                 bullets[bullet_num].x = player.x
#                 bullets[bullet_num].y = player.y
#                 if x_dir == 0 and y_dir == 0:
#                     bullets[bullet_num].x_dir = look_x_dir
#                     bullets[bullet_num].y_dir = look_y_dir
#                 else:
#                     bullets[bullet_num].x_dir = x_dir
#                     bullets[bullet_num].y_dir = y_dir
#         elif event.type == SDL_KEYUP:
#             if event.key == SDLK_RIGHT:
#                 x_dir -= 1
#                 look_x_dir = 1
#                 look_y_dir = 0
#             elif event.key == SDLK_LEFT:
#                 x_dir += 1
#                 look_x_dir = -1
#                 look_y_dir = 0
#             elif event.key == SDLK_UP:
#                 y_dir -= 1
#                 look_x_dir = 0
#                 look_y_dir = 1
#             elif event.key == SDLK_DOWN:
#                 y_dir += 1
#                 look_x_dir = 0
#                 look_y_dir = -1
#             elif event.key == SDLK_z:
#                 dash = 1
#             elif event.key == SDLK_x:
#                 bullet_num = (bullet_num + 1) % 10
#
# player = None
# room = None
# running = None
# bullets = None
#
# def enter():
#     global player, bullets, running, room
#     open_canvas()
#     room = Room()
#     player = PlayerCharacter()
#     bullets = [Bullet() for i in range(10)]
#     running = True
#     while running:
#         handle_events()
#         for bullet in bullets:
#             bullet.update()
#         player.update()
#         clear_canvas()
#         room.draw()
#         for bullet in bullets:
#             bullet.draw()
#         player.draw()
#         update_canvas()
# def exit():
#     global player, bullets, room
#     del player
#     del bullets
#     del room
#
#
# def pause():
#     pass
#
# def resume():
#     pass
#
