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
    (
        (1, 326, 29, 30),
        (35, 327, 29, 31),
        (67, 327, 30, 29),
        (98, 327, 31, 29),
        (131, 327, 29, 30),
        (162, 326, 29, 31),
        (193, 326, 30, 29),
        (230, 326, 31, 29),
        (268, 325, 30, 30)
    ),
    (
        (1, 108, 27, 38),
        (31, 110, 31, 36),
        (64, 110, 31, 36),
        (99, 110, 33, 38),
        (136, 110, 32, 36),
        (176, 110, 33, 36),
        (217, 110, 33, 36),
        (254, 111, 33, 36)
    )
)

SPEEDS = (0, 4, 10)


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
    global x, dir
    last_frame = action[-1]
    for r in range(repeat_count):
        for frame in action:
            x += speed * dir
            if x > 1120:
                x = 1120
                dir = -1
            elif x < 80:
                x = 80
                dir = 1
            render_frame(*frame)
            last_frame = frame
    for _ in range(10):
        clear_canvas()
        if dir == 1:
            sprite_sheet.clip_draw(last_frame[0], last_frame[1], last_frame[2], last_frame[3], x, y, last_frame[2] * scale, last_frame[3] * scale)
        else:
            sprite_sheet.clip_composite_draw(last_frame[0], last_frame[1], last_frame[2], last_frame[3], 0, 'h', x, y, last_frame[2] * scale, last_frame[3] * scale)
        update_canvas()
        handle_events()
        delay(0.1)


play_action(ACTIONS[2], SPEEDS[2], 5)

close_canvas()
