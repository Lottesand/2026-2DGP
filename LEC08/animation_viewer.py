from pico2d import *

open_canvas(800, 600)
sprite_sheet = load_image('megaman-sprite.png')

scale = 12

ACTIONS = (
    (
        (8, 313, 21, 24),
        (58, 313, 21, 24)
    ),
    (
        (156, 313, 24, 22),
        (209, 313, 16, 24),
        (255, 313, 21, 22)
    ),
    (
        (306, 307, 26, 30),
        (351, 313, 24, 21),
        (408, 315, 20, 22),
        (463, 309, 16, 29)
    ),
    (
        (163, 63, 27, 24),
        (213, 63, 29, 16),
        (263, 63, 29, 17),
        (313, 63, 29, 12),
        (360, 63, 23, 24)
    )
)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()


def render_frame(left, bottom, width, height):
    clear_canvas()
    sprite_sheet.clip_draw(left, bottom, width, height, 400, 300, width * scale, height * scale)
    update_canvas()
    handle_events()
    delay(0.1)


def play_action(action, repeat_count=5):
    for r in range(repeat_count):
        for frame in action:
            render_frame(*frame)
    for _ in range(10):
        handle_events()
        delay(0.1)


def main():
    while True:
        for action in ACTIONS:
            play_action(action, 5)


if __name__ == '__main__':
    main()
    close_canvas()
