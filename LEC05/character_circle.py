from pico2d import *
from math import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

# grass.draw(400, 30)
# character.draw(400, 90)
# update_canvas()

x = 0
y = 80
center_x = 400
center_y = 300
radius = 200
angle = 0

while True:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

    angle += 5

    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))

    delay(0.01)
    

update_canvas()
close_canvas()