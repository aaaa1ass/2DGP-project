from pico2d import *
import game_framework
import logo_state
import game_world
import paused_state
import menu_state
import gameover_state

from player import PlayerCharacter
from room import Room
from enemy import Enemy_1


r = 0
main_menu = False
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(paused_state)
        else:
            playercharacter.handle_event(event)


playercharacter = None  # c로 따지믄 NULL
room = None
enemy1 = None
enemy2 = None

def enter():
    global playercharacter, room, enemy1, enemy2
    playercharacter = PlayerCharacter()
    room = Room()
    # enemy1 = Enemy_1(200,200,0.2)
    # enemy2 = Enemy_1(300,200,0.2)
    # game_world.add_object(enemy1, 1)
    # game_world.add_object(enemy2, 1)
    game_world.add_object(playercharacter,2)
    game_world.add_object(room,0)

    # game_world.add_collision_paris(playercharacter,enemy1,'p:e1')
    # game_world.add_collision_paris(playercharacter,enemy2,'p:e2')
    # game_world.add_collision_paris(enemy1,enemy2,'e1:e2')



def exit():
    game_world.clear()

def update():
    global r, main_menu
    for game_object in game_world.all_objects():
            game_object.update(playercharacter.x,playercharacter.y)



    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            # print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    if main_menu is True:
        main_menu = False
        game_framework.change_state(menu_state)
    elif playercharacter.hp < 1:
        playercharacter.score_x = 300
        playercharacter.score_y = 300
        game_framework.push_state(gameover_state)

    if r > 0:
        r += 1
    if r > 100 :
        r = 0


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():

    pass

def resume():
    pass


def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True
#
# class PlayerCharacter:
#     def __init__(self):
#         self.image = load_image('character.png')
#         self.image_1 = load_image('character-1.png')
#         self.body_frame = 0
#         self.x = 400
#         self.y = 300
#
#     def update(self):
#         self.x += x_dir * 5 * dash
#         self.y += y_dir * 5 * dash
#         self.body_frame = (self.body_frame + 1) % 10
#
#     def draw(self):
#
#         if x_dir == -1:
#             self.image_1.clip_draw(1045 - self.body_frame * 32 - 48 ,810, 40 ,20,self.x - 10,self.y - 35,80,40)
#             self.image.clip_draw(240,900,50,30,self.x,self.y,100,60)
#         elif x_dir == 1:
#             self.image.clip_draw(1 + self.body_frame * 32,810,40,20,self.x - 10,self.y - 35, 80, 40)
#             self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)
#         elif y_dir == -1:
#             self.image.clip_draw(2 + self.body_frame * 32,855,40,20,self.x - 6,self.y - 30, 80, 40 )
#             self.image.clip_draw(0, 900, 50, 30, self.x, self.y, 100, 60)
#         elif y_dir == 1:
#             self.image.clip_draw(2 + self.body_frame * 32, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
#             self.image.clip_draw(160, 900, 50, 30, self.x, self.y, 100, 60)
#         else:
#             if look_x_dir == -1:
#                 self.image_1.clip_draw(1045 - 48, 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
#                 self.image.clip_draw(240, 900, 50, 30, self.x, self.y, 100, 60)
#             elif look_x_dir == 1:
#                 self.image.clip_draw(1 , 810, 40, 20, self.x - 10, self.y - 35, 80, 40)
#                 self.image.clip_draw(80, 900, 50, 30, self.x, self.y, 100, 60)
#             elif look_y_dir == 1:
#                 self.image.clip_draw(2 , 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
#                 self.image.clip_draw(160, 900, 50, 30, self.x, self.y, 100, 60)
#             else:
#                 self.image.clip_draw(2, 855, 40, 20, self.x - 6, self.y - 30, 80, 40)
#                 self.image.clip_draw(0, 900, 50, 30, self.x, self.y, 100, 60)
#
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
