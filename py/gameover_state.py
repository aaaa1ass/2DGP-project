from pico2d import *
import game_framework
import play_state

gameover_font = None
menu_font = None

mx1, my1 = 290, 200
mx2, my2 = mx1 + 220, my1 + 30

gameover_color = (0,0,255)
off_color = (255,255,255)
on_color = (255,0,0)
menu_color = off_color



def handle_events():
    global menu_color
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if event.x > mx1 and event.x < mx2 and 600 - 1 - event.y > my1 and 600 - 1 - event.y < my2:
                game_framework == game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            if event.x > mx1 and event.x < mx2 and 600 - 1 - event.y > my1 and 600 - 1 - event.y < my2:
                menu_color = on_color
            else:
                menu_color = off_color

def enter():
    global gameover_font, menu_font
    gameover_font = load_font('ENCR10B.TTF',70)
    menu_font = load_font('ENCR10B.TTF',40)

def exit():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    gameover_font.draw(200,400,'GAME OVER',gameover_color)
    menu_font.draw(mx1,my1+15,'QUIT GAME',menu_color)
    update_canvas()
def update():
    pass

def pause():
    pass
def resume():
    pass