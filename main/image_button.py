import pyglet

class ImageButton:
    def __init__(self, normal_image_path, hover_image_path, 
                 clicked_image_path, x, y, width, height):
        self.normal_image = pyglet.image.load(normal_image_path)
        self.hover_image = pyglet.image.load(hover_image_path)
        self.clicked_image = pyglet.image.load(clicked_image_path)
        self.sprite = pyglet.sprite.Sprite(self.normal_image, x=x, y=y)
        self.width = width
        self.height = height
        self.hovered = False
        self.clicked = False

    def draw(self):
        # Change the sprite image based on hover state
        if self.clicked:
            self.sprite.image = self.clicked_image
        elif self.hovered:
            self.sprite.image = self.hover_image
        else:
            self.sprite.image = self.normal_image
        self.sprite.draw()

    def update_hover(self, x, y):
        # Check if the mouse is over the button
        self.hovered = (self.sprite.x <= x <= self.sprite.x + self.width and
                        self.sprite.y <= y <= self.sprite.y + self.height)

    def is_clicked(self, x, y, button):
        # Check if the left mouse button is clicked on the button
        return (button == pyglet.window.mouse.LEFT and
                self.sprite.x <= x <= self.sprite.x + self.width and
                self.sprite.y <= y <= self.sprite.y + self.height)
    def toogle_clicked(self):
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True