from pico2d import *
import game_world
import play_state
import game_framework

PIXEL_PER_METER = (30.0 / 0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Bullet:
    image = None

    def __init__(self,x,y,x_dir,y_dir,velocity):
        if Bullet.image == None:
            Bullet.image = load_image('character.png')
        self.x = x
        self.y = y
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.velocity = velocity
        self.hit = False
        print(play_state.room.enemy_num)

        for i in range(play_state.room.enemy_num):
            game_world.add_collision_paris(self, play_state.room.enemy_list[i], 'b:e' + str(i))


    def update(self,x,y):
        self.x += self.velocity * self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.velocity * self.y_dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x <0 or self.x > 800 or self.hit:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(160, 490, 50, 30, self.x, self.y, 38, 24)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self,other,group):
        for i in range(play_state.room.enemy_num):
            if group == 'b:e' + str(i):
                self.x, self.y = 0, 900
                self.hit = True



