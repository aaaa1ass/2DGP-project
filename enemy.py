from pico2d import *
import game_world
import random
from heart import Heart

import play_state


class Enemy_1:
    image_head = None
    image_body = None

    def __init__(self,x,y,velocity):
        if Enemy_1.image_head == None:
            Enemy_1.image_head = load_image('enemy1.png')
        if Enemy_1.image_body == None:
            Enemy_1.image_body = load_image('character.png')
        self.x = x
        self.y = y
        self.velocity = velocity
        self.i = 0
        self.max_hp = 5
        self.hp = self.max_hp

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
        t = self.velocity / d

        # self.x = (1 - tx) * self.x + tx * x
        # self.y = (1-ty) * self.y + ty * y

        # t = self.i / 100
        self.x = (1-t) * self.x + t * x
        self.y = (1-t) * self.y + t * y

        self.i = 0.01

        if self.hp < 1:
            print('remove 1')
            self.x, self.y = 800, 800
            game_world.remove_object(self)

    def draw(self):
        self.image_head.draw(self.x,self.y)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 25, self.y + 20

    def handle_collision(self, other, group):
        if group == 'b:e1':
            self.hp -= 1
            print(self.hp)
        if group == 'b:e2':
            self.hp -= 1
        if group == 'e1:e2':
            if self.x < other.x + 25 and self.x > other.x - 20:
                if self.y < other.y and self.y > other.y -40: self.y = other.y-40
                elif self.y> other.y and self.y < other.y +40: self.y = other.y+40
            if self.y < other.y + 20 and self.y > other.y - 20:
                if self.x < other.x and self.x > other.x -45: self.x = other.x-45
                elif self.x> other.x and self.x < other.x +40: self.x = other.x+45

            # if self.y < 140: self.y = 140
            # if self.x > 700: self.x = 700
            # if self.y > 500: self.y = 500

class Enemy_2:
    image_head = None
    image_body = None

    def __init__(self):
        if Enemy_2.image_head == None:
            Enemy_2.image_head = load_image('enemy2.png')
        if Enemy_2.image_body == None:
            Enemy_2.image_body = load_image('character.png')
        self.x = random.randint(100,700)
        self.y = random.randint(300,500)
        self.velocity = 0.2
        self.i = 0
        self.max_hp =1
        self.hp = self.max_hp
        self.heart = None

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
        t = self.velocity / d

        # self.x = (1 - tx) * self.x + tx * x
        # self.y = (1-ty) * self.y + ty * y

        # t = self.i / 100
        self.x = (1-t) * self.x + t * x
        self.y = (1-t) * self.y + t * y

        self.i = 0.01

        if self.hp < 1:
            print('remove 1')
            self.heart = Heart(self.x, self.y)
            self.x, self.y = 800, 800

            i = random.randint(1,100)
            if i > 70:
                game_world.add_object(self.heart,1)
            play_state.playercharacter.exp += 20
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

        # if group == 'b:e1':
        #     self.hp -= 1
        #     print(self.hp)
        # if group == 'b:e2':
        #     self.hp -= 1
        # if group == 'e1:e2':
        # for i in range(play_state.room.enemy_num - 1):
        #     for j in range(play_state.room.enemy_num - 1 - i):

        for i in range(play_state.room.enemy_num):
            for j in range(play_state.room.enemy_num):
                if group == 'e' + str(i) + ':e' + str(j+1):
                    if self.x < other.x + 25 and self.x > other.x - 20:
                        if self.y < other.y and self.y > other.y -40: self.y = other.y-40
                        elif self.y> other.y and self.y < other.y +40: self.y = other.y+40
                    if self.y < other.y + 20 and self.y > other.y - 20:
                        if self.x < other.x and self.x > other.x -45: self.x = other.x-45
                        elif self.x> other.x and self.x < other.x +40: self.x = other.x+45

            # if self.y < 140: self.y = 140
            # if self.x > 700: self.x = 700
            # if self.y > 500: self.y = 500




