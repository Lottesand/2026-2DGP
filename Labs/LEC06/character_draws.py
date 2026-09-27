import math
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')




def draw_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    pass

def draw_rectangle():
    pass

def draw_triangle():
    pass

while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()
    break
    pass
