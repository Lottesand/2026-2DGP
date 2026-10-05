from pico2d import *

open_canvas(1200, 600)
sprite_sheet = load_image('sonic-sprite.png')

scale = 4
x, y = 100, 300


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()


sprite_sheet.clip_draw(1, 361, 33, 40, x, y, 33 * scale, 40 * scale)
update_canvas()
handle_events()
delay(1.0)

close_canvas()
