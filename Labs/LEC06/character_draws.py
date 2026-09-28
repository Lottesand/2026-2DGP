import math
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')


def draw_circle():
    print("CIRCLE")
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_top():
    for x in range(50, 751, 5):
        draw_character(x, 550)


def move_right():
    for y in range(550, 49, -5):
        draw_character(750, y)


def move_bottom():
    for x in range(750, 49, -5):
        draw_character(x, 50)


def move_left():
    for y in range(50, 551, 5):
        draw_character(50, y)


def draw_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()


def draw_triangle():
    print("TRIANGLE")


while True:
    draw_rectangle()
    draw_triangle()
    break
