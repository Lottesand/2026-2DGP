from pico2d import *

open_canvas(1200, 600)
sprite_sheet = load_image('sonic-sprite.png')

sprite_sheet.clip_draw(1, 361, 33, 40, 100, 300)
update_canvas()
delay(1.0)

close_canvas()
