from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

# grass.draw(400, 30)
# character.draw(400, 90)
# update_canvas()

x = 100
y = 80

while True:
    while x < 600:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        x += 5
        delay(0.01)

    while y < 400:
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, y)
            update_canvas()
            y += 5
            delay(0.01)

    while x > 100:
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, y)
            update_canvas()
            x -= 5
            delay(0.01)

    while y > 80:
                clear_canvas()
                grass.draw(400, 30)
                character.draw(x, y)
                update_canvas()
                y -= 5
                delay(0.01)
    


close_canvas()