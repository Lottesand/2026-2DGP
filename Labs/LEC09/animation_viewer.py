from pico2d import *

open_canvas(1200, 600)
sprite_sheet = load_image('sonic-sprite.png')

scale = 4
x, y = 100, 300
dir = 1


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()


def render_frame(left, bottom, width, height):
    clear_canvas()
    if dir == 1:
        sprite_sheet.clip_draw(left, bottom, width, height, x, y, width * scale, height * scale)
    else:
        sprite_sheet.clip_composite_draw(left, bottom, width, height, 0, 'h', x, y, width * scale, height * scale)
    update_canvas()
    handle_events()
    delay(0.08)


render_frame(1, 361, 33, 40)

close_canvas()
