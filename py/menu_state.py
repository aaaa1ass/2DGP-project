from pico2d import *
import game_framework
import play_state

image = None
font = None
qx1, qy1, qx2, qy2 = 100, 85, 275, 115
px1, py1, px2, py2 = 100, 125, 180, 155

on_color = (255,0,0)
off_color = (255,255,255)
play_color = off_color
quit_color = off_color

def enter():
    global image, font
    image = load_image('image\main_menu.png')
    font = load_font('ENCR10B.TTF',32)

def exit():
    global image
    del image

def update():
    pass

def draw():
    clear_canvas()
    image.draw(400,300,800,600)
    font.draw(100,140,'PLAY',play_color)
    font.draw(100,100,'QUIT GAME',quit_color)
    draw_rectangle(px1,py1,px2,py2)
    update_canvas()

def handle_events():
    global quit_color, play_color
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if event.x > qx1 and event.x < qx2 and 600 - 1 - event.y > qy1 and 600 - 1 - event.y < qy2:
                game_framework.quit()
            elif event.x > px1 and event.x < px2 and 600 - 1 - event.y > py1 and 600 - 1 - event.y < py2:
                game_framework.change_state(play_state)
        elif event.type == SDL_MOUSEMOTION:
            if event.x > qx1 and event.x < qx2 and 600 - 1 - event.y > qy1 and 600 - 1 - event.y < qy2:
                quit_color = on_color
            elif event.x > px1 and event.x < px2 and 600 - 1 - event.y > py1 and 600 - 1 - event.y < py2:
                play_color = on_color
            else:
                quit_color = off_color
                play_color = off_color


            # game_framework.change_state(play_state)

def pause():
    pass
def resume():
    pass
def test_self():
    import menu_state

    pico2d.open_canvas()
    game_framework.run(menu_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()