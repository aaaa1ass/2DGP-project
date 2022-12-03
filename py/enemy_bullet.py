from pico2d import *
import game_world
import play_state
import game_framework

PIXEL_PER_METER = (30.0 / 0.3)
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Enemy_bullet:
    image = None

    def __init__(self, x, y, x_dir, y_dir, velocity):
        if Enemy_bullet.image == None:
            Enemy_bullet.image = load_image('image\character.png')

        self.x = x
        self.y = y
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.t = 0
        self.i = 0
        self.velocity = velocity
        self.hit = False

        game_world.add_collision_paris(self,play_state.playercharacter,'eb:p')

    def update(self,x,y):
        self.t = self.i / 8000
        self.x = (1 - self.t) * self.x + self.t * self.x_dir
        self.y = (1 - self.t) * self.y + self.t * self.y_dir
        self.i += RUN_SPEED_PPS * game_framework.frame_time * 0.2
        if self.i > 250 or self.hit:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(538, 490, 50, 30, self.x, self.y, 38, 24)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self,other,group):
            if group == 'eb:p':
                self.x, self.y = 0, 900
                self.hit = True