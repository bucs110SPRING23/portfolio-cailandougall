import rectangle
class Surface():
    def __init__(self, filename, x, y, h, w):
        self.image=str(filename)
        self.rect=rectangle.Rectangle(x, y, h, w)
    def get_rect (self):
        return self.rect