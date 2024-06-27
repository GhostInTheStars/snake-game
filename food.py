import random


class Food:
    block_size = None
    x = 0
    y = 0
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = [r, g, b]
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, game, window):
        game.draw.rect(window, self.color,
                       (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = [r, g, b]
        blocks_in_x = (self.bounds[0]) // self.block_size
        blocks_in_y = (self.bounds[1]) // self.block_size
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size
