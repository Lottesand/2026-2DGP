from pico2d import *

open_canvas(800, 600)
sprite_sheet = load_image('megaman-sprite.png')

sprite_sheet.clip_draw(8, 313, 21, 24, 400, 300)
update_canvas()
delay(1.0)

close_canvas()
