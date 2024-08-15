#**************************************
# https://github.com/AryanJAryanJ-droid
#**************************************

import pyglet

class LabelChanger:
    def __init__(self, texts, window_width, window_height):
        self.texts = texts
        self.index = 0  # To keep track of the current text
        self.label = pyglet.text.Label(self.texts[self.index],
                                       font_name='Arial',
                                       font_size=13,
                                       x=window_width - 150,
                                       y=window_height - 30,
                                       anchor_x='center',
                                       anchor_y='center')

    def update_label(self, dt):
        self.index = (self.index + 1) % len(self.texts)  # Cycle through the texts
        self.label.text = self.texts[self.index]  # Update the label text

    def draw(self):
        self.label.draw()
