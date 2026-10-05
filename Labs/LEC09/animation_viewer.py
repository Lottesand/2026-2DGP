from pico2d import *

open_canvas(1200, 600)
sprite_sheet = load_image('sonic-sprite.png')

scale = 4
x, y = 100, 300
dir = 1

ACTIONS = (
    (
        (1, 361, 33, 40),
        (39, 362, 35, 39),
        (89, 362, 35, 38),
        (130, 362, 34, 42),
        (181, 362, 34, 41),
        (228, 363, 33, 40)
    ),
)

SPEEDS = (0,)


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


def play_action(action, speed, repeat_count=5):
    for r in range(repeat_count):
        for frame in action:
            render_frame(*frame)


play_action(ACTIONS[0], SPEEDS[0], 5)

close_canvas()
