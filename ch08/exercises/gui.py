class Text:
    def __init__(self):
        """
        Initialize the Text object
        """
        self.font="Arial"
        self.size=12
        self.color="white"
        self.pos= (0,500)
class Brick:
    def __init__(self):
        """
        Initialize the Brick object
        """
        self.color="brown"
        self.length=20
        self.width=20
        self.pos= (0,0)
class Enemy:
    def __init__(self):
        """
        Initialize the enemy object
        """
        self.color="brown"
        self.is_large=False
        self.health=1