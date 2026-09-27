import math
from pico2d import *

open_canvas(800, 600)
boy = load_image('character.png')

center_x, center_y = 400, 300
radius = 200

def move_circle():
    # 반원 호 이동: 0도 -> 180도 (600, 300) -> (400, 500) -> (200, 300)
    for degree in range(0, 181, 5):
        theta = math.radians(degree)
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        clear_canvas()
        boy.draw(x, y)
        update_canvas()
        delay(0.01)

def move_rectangle():
    print('rectangle')

def move_triangle():
    print('triangle')

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    break

close_canvas()
