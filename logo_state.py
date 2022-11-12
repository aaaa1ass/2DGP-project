from pico2d import *
import game_framework
import play_state
import time

running = True
image = None
start_time = time.time()
logo_time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')
    pass

def exit():
    global image
    del image

def update():
    global logo_time
    # global running
    if logo_time > start_time + 2:
        logo_time = 0
        game_framework.change_state(play_state)
        # game_framework.quit()
    logo_time = time.time()

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()





