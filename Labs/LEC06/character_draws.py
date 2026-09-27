import math
from pico2d import *

open_canvas(800, 600)
boy = load_image('character.png')

center_x, center_y = 400, 300
radius = 200

def move_circle():
    # 원운동 1회 완전 회전: 0도 -> 360도
    for degree in range(0, 360, 5):
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
