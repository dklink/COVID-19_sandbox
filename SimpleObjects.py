from collections import namedtuple
from enum import Enum

DiseaseStage = Enum('DiseaseStage', 'susceptible infected recovered deceased')


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Position') -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** .5
