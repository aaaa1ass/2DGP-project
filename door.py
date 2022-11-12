from pico2d import *
import game_world
import play_state

class Door:
    image = None

    def __init__(self):
        if Door.image == None:
            Door.image = load_image('door.png')
        self. x = 400
        self. y = 520
        self.lock = True

    def update(self,x,y):
        if play_state.room.enemy_list:
            self.lock = True

    def draw(self):
        self.image.clip_draw(0,200,50,50, self.x, self.y, 100, 100)

        if self.lock == False:
            self.image.clip_draw(64,200,50,50, self.x, self.y, 100, 100)
        else:
            self.image.clip_draw(0, 152, 50, 50, self.x, self.y, 100, 100)
            self.image.clip_draw(64, 152, 50, 50, self.x, self.y, 100, 100)

    def get_bb(self):
        return self.x - 20, self.y - 50, self.x + 20, self.y + 20

    def handle_collision(self,other,group):
            if group == 'p:d' and self.lock == False:
                play_state.room.new = True
                play_state.room.level += 1
                play_state.playercharacter.y -= 400
                play_state.room.clear = True
                play_state.r = 1
                self.lock = True
        # if group == 'b:e1'or group == 'b:e2':