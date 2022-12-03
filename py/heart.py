from pico2d import *
import game_world
import play_state

class Heart:
    image = None

    def __init__(self,x,y):
        if Heart.image == None:
            Heart.image = load_image('heart.png')
        self.x = x
        self.y = y
        self.hit = False

        game_world.add_collision_paris(self,play_state.playercharacter, 'h:p')

    def update(self,x,y):
        if self.hit:
            self.x = 900
            self.y = 900
            game_world.remove_object(self)
        if play_state.r > 0:
            self.x = 900
            self.y = 900
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(0, 250, 75, 50, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y, self.x + 20, self.y + 20

    def handle_collision(self,other,group):
            if group == 'h:p':
                self.x, self.y = 900, 900

            if play_state.playercharacter.hp < play_state.playercharacter.max_hp:
                play_state.playercharacter.hp += 1
                self.hit = True
