from SimpleObjects import Position
from random import randint


class Behavior:
    """describes a pattern of movement in time through an environment"""
    # should be abstract eventually, for now is random walk
    def __init__(self, environment, radius):
        self.environment = environment
        self.radius = radius

    def update_position(self, position: Position) -> Position:
        # random walk within environment
        new_x = position.x + randint(-self.radius, self.radius)
        new_y = position.y + randint(-self.radius, self.radius)

        if new_x > self.environment.max_x:
            new_x = self.environment.max_x
        elif new_x < self.environment.min_x:
            new_x = self.environment.min_x
        if new_y > self.environment.max_y:
            new_y = self.environment.max_y
        elif new_y < self.environment.min_y:
            new_y = self.environment.min_y

        return Position(new_x, new_y)
