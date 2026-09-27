from pico2d import *

def move_circle():
    print('circle')

def move_rectangle():
    print('rectangle')

def move_triangle():
    print('triangle')

open_canvas(800, 600)
boy = load_image('character.png')

# 캔버스 중앙에 캐릭터 단일 출력 확인
clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    break

close_canvas()
