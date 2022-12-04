from pico2d import *
import game_world
import game_framework
import random
import enemy_bullet
from heart import Heart
import time

import play_state


class Enemy_1:
    image_head = None
    die_sound = None
    hurt_sound = None

    def __init__(self):
        if Enemy_1.image_head == None:
            Enemy_1.image_head = load_image('image\enemy1.png')
        if Enemy_1.die_sound == None:
            Enemy_1.die_sound = load_wav('sound\Enemy_die.wav')
            Enemy_1.die_sound.set_volume(24)
        if Enemy_1.hurt_sound == None:
            Enemy_1.hurt_sound = load_wav('sound\Enemy_hurt.wav')
            Enemy_1.hurt_sound.set_volume(32)
        self.x = random.randint(100, 700)
        self.y = random.randint(300, 500)
        self.max_hp = 3
        self.hp = self.max_hp
        self.heart = Heart(self.x, self.y)
        self.heart_gen = random.randint(1, 100)
        self.cool_down = 1
        self.cool_down_time = 2.0

    def update(self, x, y):

        self.fire()

        if self.hp < 1:
            self.x, self.y = 800, 800

            play_state.playercharacter.exp += 20
            play_state.playercharacter.score += 1

            game_world.remove_object(self)

    def fire(self):
        if self.cool_down == 0:
            bullet = enemy_bullet.Enemy_bullet(self.x, self.y, play_state.playercharacter.x, play_state.playercharacter.y, 1)
            game_world.add_object(bullet, 1)
            self.cool_down = 1
        if self.cool_down == 1:
            self.fire_time = time.time() + self.cool_down_time
            self.cool_down = 2
        if self.cool_down == 2 and self.fire_time < time.time():
                self.cool_down = 0


    def draw(self):
        self.image_head.draw(self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 25, self.y + 20

    def handle_collision(self, other, group):
        for i in range(play_state.room.enemy_num):
            if group == 'b:e' + str(i):
                self.hp -= 1
                if self.hp < 1:
                    Enemy_1.die_sound.play()
                else:
                    Enemy_1.hurt_sound.play()

        for i in range(play_state.room.enemy_num):
            for j in range(play_state.room.enemy_num):
                if group == 'e' + str(i) + ':e' + str(j + 1):
                    if self.x < other.x + 25 and self.x > other.x - 20:
                        if self.y < other.y and self.y > other.y - 40:
                            self.y = other.y - 40
                        elif self.y > other.y and self.y < other.y + 40:
                            self.y = other.y + 40
                    if self.y < other.y + 20 and self.y > other.y - 20:
                        if self.x < other.x and self.x > other.x - 45:
                            self.x = other.x - 45
                        elif self.x > other.x and self.x < other.x + 40:
                            self.x = other.x + 45

PIXEL_PER_METER = (30.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Enemy_2:
    image_head = None
    die_sound = None
    hurt_sound = None

    def __init__(self):
        if Enemy_2.image_head == None:
            Enemy_2.image_head = load_image('image\enemy2.png')
        if Enemy_2.die_sound == None:
            Enemy_2.die_sound = load_wav('sound\Enemy_die.wav')
            Enemy_2.die_sound.set_volume(24)
        if Enemy_2.hurt_sound == None:
            Enemy_2.hurt_sound = load_wav('sound\Enemy_hurt.wav')
            Enemy_2.hurt_sound.set_volume(32)
        self.x = random.randint(100,700)
        self.y = random.randint(300,500)
        self.velocity = 0.2
        self.max_hp = 3
        self.hp = self.max_hp
        self.heart = Heart(self.x,self.y)
        self.heart_gen = random.randint(1,100)

    def update(self,x,y):
        if x < self.x: dx = self.x - x
        else: dx = x - self.x
        if y < self.y: dy = self.y - y
        else: dy = y - self.y

        if dx == 0: tx = 1
        else: tx = 0.1 / dx
        if tx > 1: tx = 1

        if dy == 0: ty = 1
        else: ty = 0.1 / dy
        if ty > 1: ty = 1


        d = dx ** 2 + dy ** 2
        d = d ** 0.5
        t = self.velocity * RUN_SPEED_PPS * game_framework.frame_time / d


        self.x = (1-t) * self.x + t * x
        self.y = (1-t) * self.y + t * y



        if self.hp < 1:
            self.x, self.y = 800, 800


            play_state.playercharacter.exp += 20
            play_state.playercharacter.score += 1

            game_world.remove_object(self)

    def draw(self):
        self.image_head.draw(self.x,self.y)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 25, self.y + 20

    def handle_collision(self, other, group):
        for i in range(play_state.room.enemy_num):
            if group == 'b:e' + str(i):
                self.hp -= 1
                if self.hp < 1:
                    Enemy_2.die_sound.play()
                else:
                    Enemy_2.hurt_sound.play()

        for i in range(play_state.room.enemy_num):
            for j in range(play_state.room.enemy_num):
                if group == 'e' + str(i) + ':e' + str(j+1):
                    if self.x < other.x + 25 and self.x > other.x - 20:
                        if self.y < other.y and self.y > other.y -40: self.y = other.y-40
                        elif self.y> other.y and self.y < other.y +40: self.y = other.y+40
                    if self.y < other.y + 20 and self.y > other.y - 20:
                        if self.x < other.x and self.x > other.x -45: self.x = other.x-45
                        elif self.x> other.x and self.x < other.x +40: self.x = other.x+45




