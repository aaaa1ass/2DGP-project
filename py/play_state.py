from pico2d import *
import game_framework
import logo_state
import game_world
import paused_state
import menu_state
import gameover_state

from player import PlayerCharacter
from room import Room

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


def enter():
    global playercharacter, room
    playercharacter = PlayerCharacter()
    room = Room()
    game_world.add_object(playercharacter,2)
    game_world.add_object(room,0)


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
