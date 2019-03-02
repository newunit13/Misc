"""

Container for game objects

"""


class Player():
    """
    Player Class
    """
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

    def get(self):
        """
        returns the player's position and dimensions as a tuple
        """
        return (self.x, self.y, self.width, self.height)
