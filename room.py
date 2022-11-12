from pico2d import *
import play_state
import game_world
from door import Door
from enemy import Enemy_2


class Room:
    def __init__(self):
        self.image = load_image('room.png')
        self.door = Door()
        game_world.add_object(self.door, 1)
        self.lock = True
        # self.enemy = [Enemy_2() for i in range(3)]
        self.new = False
        self.level = 1
        self.enemy_num = self.level
        self.clear = False
        self.enemy_list = [Enemy_2() for i in range(self.enemy_num)]
        print(self.enemy_num)
        game_world.add_collision_paris(play_state.playercharacter,self.door,'p:d')

        for i in self.enemy_list:
            game_world.add_object(i,1)
        for i in range(self.enemy_num):
            game_world.add_collision_paris(play_state.playercharacter, self.enemy_list[i], 'p:e' + str(i))
        for i in range(self.enemy_num - 1):
            for j in range(self.enemy_num - 1 - i):
                game_world.add_collision_paris(self.enemy_list[i], self.enemy_list[j+1], 'e'+str(i) +':e'+str(j+1))

        print(self.enemy_num)
    def draw(self):
        self.image.draw(400,300,800,600)


    def update(self,x,y):
        # if not self.lock:
        if not self.enemy_list:
            self.door.lock = False
            self.clear = False
        for i in self.enemy_list:
            if i.hp < 1:
                self.enemy_list.remove(i)
                self.enemy_num -= 1
        if self.new == True:
            self.enemy_num = self.level
            self.enemy_list = [Enemy_2() for i in range(self.enemy_num)]
            print(self.enemy_list)
            for i in self.enemy_list:
                game_world.add_object(i, 1)
            for i in range(self.enemy_num):
                game_world.add_collision_paris(play_state.playercharacter, self.enemy_list[i], 'p:e' + str(i))
            for i in range(self.enemy_num):
                for j in range(self.enemy_num):
                    game_world.add_collision_paris(self.enemy_list[i], self.enemy_list[j],'e' + str(i) + ':e' + str(j))
            self.new = False




    def get_bb(self):
        return 95,100,700,500