from pico2d import *
import game_framework
import play_state
import menu_state
import player

pause_font = None
other_font = None

mx1, my1 = 290, 270
mx2, my2 = mx1 + 220, my1 + 30
rx1, ry1 = 270, 330
rx2, ry2 = rx1 + 270, ry1 + 30

paused_color = (0,0,255)
on_color = (255,0,0)
off_color = (255,255,255)
resume_color = off_color
menu_color = off_color


def handle_events():
    global resume_color, menu_color
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if event.x > mx1 and event.x < mx2 and 600 - 1 - event.y > my1 and 600 - 1 - event.y < my2:
                game_framework.quit()
            elif event.x > rx1 and event.x < rx2 and 600 - 1 - event.y > ry1 and 600 - 1 - event.y < ry2:
                game_framework.pop_state()
        elif event.type == SDL_MOUSEMOTION:
            if event.x > mx1 and event.x < mx2 and 600 - 1 - event.y > my1 and 600 - 1 - event.y < my2:
                menu_color = on_color
            elif event.x > rx1 and event.x < rx2 and 600 - 1 - event.y > ry1 and 600 - 1 - event.y < ry2:
                resume_color = on_color
            else:
                resume_color = off_color
                menu_color = off_color

def enter():
    global pause_font, other_font
    pause_font = load_font('ENCR10B.TTF',32)
    other_font = load_font('ENCR10B.TTF',40)

def exit():
    play_state.playercharacter.cur_state = player.IDLE
    pass

def update():
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    pause_font.draw(340,400,'PAUSED',paused_color)
    other_font.draw(rx1,ry1+15,'RESUME GAME',resume_color)
    other_font.draw(mx1,my1+15,'QUIT GAME',menu_color)
    update_canvas()

def pause():
    pass
def resume():
    pass