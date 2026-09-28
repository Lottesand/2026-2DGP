import math
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')


def render(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    for deg in range(360):
        rad = math.radians(deg)
        x = 400 + 200 * math.cos(rad)
        y = 300 + 200 * math.sin(rad)
        render(x, y)


def move_rectangle():
    for x in range(50, 751, 5):
        render(x, 550)
    for y in range(550, 49, -5):
        render(750, y)
    for x in range(750, 49, -5):
        render(x, 50)
    for y in range(50, 551, 5):
        render(50, y)


def move_along_path(start, end, steps=100):
    x0, y0 = start
    x1, y1 = end
    for step in range(steps + 1):
        t = step / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        render(x, y)


def move_triangle():
    move_along_path((100, 100), (700, 100))
    move_along_path((700, 100), (400, 500))
    move_along_path((400, 500), (100, 100))


while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()
