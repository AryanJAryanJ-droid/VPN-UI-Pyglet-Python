#**************************************
# https://github.com/AryanJAryanJ-droid
#**************************************

import pyglet
from connection_check import check
from image_button import ImageButton
from speedlabel import LabelChanger


background_image = pyglet.image.load('C:\\Users\\Aryan\\Desktop\\Project VPN\\UI Elements\\BGIMG.jpg')

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BUTTON_WIDTH = 297
BUTTON_HEIGHT = 105

window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, 
                              caption='Street VPN')

pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_LINEAR)
pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_LINEAR)

button = ImageButton('button.png', 'button-hover.png', 'button-click.png', 
                     x=(WINDOW_WIDTH - BUTTON_WIDTH) // 2, 
                     y=(WINDOW_HEIGHT - BUTTON_HEIGHT) // 2, 
                     width=BUTTON_WIDTH, height=BUTTON_HEIGHT)


connect = check
print(connect())
speed_download = LabelChanger(connect(), window.width, window.height)
pyglet.clock.schedule_interval(speed_download.update_label, 1.0)


@window.event
def on_draw():
    window.clear()
    
    background_image.blit(0, 0, 
                          width = window.width, height = window.height)
    button.draw()
    speed_download.draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    button.update_hover(x, y)

@window.event
def on_mouse_press(x, y, button_code, modifiers):
    if button.is_clicked(x, y, button_code):
        print("clicked")
        button.toogle_clicked()

# @window.event
# def on_mouse_release(x, y, button_code, modifiers):

def reset_button(dt):
    button.set_clicked(False)
pyglet.app.run()


#**************************************
# https://github.com/AryanJAryanJ-droid
#**************************************
