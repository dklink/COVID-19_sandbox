from SimpleObjects import Position
import Behavior


class Person:
    """represents a person in the simulation"""
    def __init__(self, initial_position: Position, behavior: Behavior):
        self.position = initial_position
        self.behavior = behavior

    def behave(self):
        self.position = self.behavior.update_position(self.position)
