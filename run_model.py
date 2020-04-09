"""
Top-level driver
"""
from random import randint

import numpy as np
import matplotlib.pyplot as plt

from Environment import Environment
from Behavior import Behavior
from Person import Person
from SimpleObjects import Position

# create an environment

# this world is 2d, has an x-y extent
world_width = 1024
world_height = 1024

world = Environment(min_x=0, max_x=world_width,
                    min_y=0, max_y=world_height)

# create behaviors
# people move randomly
randomWalk = Behavior(world, 15)

# create a population
pop_size = 100
population = [Person(Position(randint(0, world_width), randint(0, world_height)), randomWalk) for _ in range(pop_size)]

# create a disease

# run behaviors, plot
# plt.ion()
fig, ax = plt.subplots()
sc = ax.scatter([p.position.x for p in population], [p.position.y for p in population])
plt.xlim([world.min_x, world.max_x])
plt.ylim([world.min_y, world.max_y])

plt.draw()
for timestep in range(100):
    for person in population:
        person.behave()
    x, y = [p.position.x for p in population], [p.position.y for p in population]
    sc.set_offsets(np.c_[x, y])
    plt.title(timestep)
    fig.canvas.draw_idle()
    plt.pause(0.05)

plt.waitforbuttonpress()
