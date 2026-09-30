from pico2d import *

open_canvas(800, 600)
sprite_sheet = load_image('megaman-sprite.png')

scale = 12

ACTIONS = (
    (
        (8, 313, 21, 24),
        (58, 313, 21, 24)
    ),
)


def render_frame(left, bottom, width, height):
    clear_canvas()
    sprite_sheet.clip_draw(left, bottom, width, height, 400, 300, width * scale, height * scale)
    update_canvas()
    delay(0.1)


def play_action(action, repeat_count=5):
    for r in range(repeat_count):
        for frame in action:
            render_frame(*frame)


play_action(ACTIONS[0], 5)

close_canvas()
