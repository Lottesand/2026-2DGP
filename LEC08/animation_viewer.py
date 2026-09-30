from pico2d import *

open_canvas(800, 600)
sprite_sheet = load_image('megaman-sprite.png')

scale = 12


def render_frame(left, bottom, width, height):
    clear_canvas()
    sprite_sheet.clip_draw(left, bottom, width, height, 400, 300, width * scale, height * scale)
    update_canvas()
    delay(0.1)


render_frame(8, 313, 21, 24)

close_canvas()
