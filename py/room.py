from pico2d import *
import play_state
import game_world
from door import Door
from enemy import Enemy_2
from enemy import Enemy_1


class Room:
    def __init__(self):
        self.image = load_image('image\\room.png')
        self.font = load_font('ENCR10B.TTF', 40)
        self.door = Door()
        game_world.add_object(self.door, 1)
        self.lock = True
        self.new = False
        self.level = 0
        self.enemy_num = self.level
        self.clear = False
        self.enemy_list = []
        game_world.add_collision_paris(play_state.playercharacter,self.door,'p:d')

    def draw(self):
        self.image.draw(400,300,800,600)
        if self.level == 0:
            self.font.draw(150,300,'z:run',(255,255,255))
            self.font.draw(500,300,'x:fire',(255,255,255))
            self.font = load_font('ENCR10B.TTF', 24)
            self.font.draw(240,80,'Level up for quick fire',(255,255,255))


    def update(self,x,y):
        if not self.enemy_list:
            self.door.lock = False
            self.clear = False
        for i in self.enemy_list:
            if i.hp < 1:
                self.enemy_list.remove(i)
                self.enemy_num -= 1

        if self.new == True:
            self.enemy_num = self.level + self.level // 4
            self.enemy_list = [Enemy_2() for i in range(self.enemy_num - self.level // 4)]
            for i in range(self.level // 4):
                self.enemy_list.append(Enemy_1())
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