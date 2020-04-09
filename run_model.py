"""
Top-level driver
"""
from random import randint
from Environment import Environment
from Behavior import Behavior
from Person import Person
from Population import Population
from SimpleObjects import Position, DiseaseStage
import Virus

import numpy as np
import matplotlib.pyplot as plt


def disease_stage_to_color(disease_stage):
    if disease_stage == DiseaseStage.infected:
        return 'tab:orange'
    elif disease_stage == DiseaseStage.susceptible:
        return 'b'
    elif disease_stage == DiseaseStage.recovered:
        return 'g'
    elif disease_stage == DiseaseStage.deceased:
        return 'k'


# create an environment

# this world is 2d, has an x-y extent
world_width = 100
world_height = 100

world = Environment(min_x=0, max_x=world_width,
                    min_y=0, max_y=world_height)

# create behaviors
# people move randomly
randomWalk = Behavior(world, 2)

# create a population
pop_size = 100
people = [Person(Position(randint(0, world_width), randint(0, world_height)), randomWalk) for _ in range(pop_size)]
population = Population(people)

# create a virus, put it into population
covid = Virus.covid
population.people[0].virus = covid
population.people[0].disease_stage = DiseaseStage.infected

# run behaviors, plot
# plt.ion()
fig, ax = plt.subplots()
disease_stage = [p.disease_stage for p in population.people]
colors = list(map(disease_stage_to_color, disease_stage))
sc = ax.scatter(x=[p.position.x for p in population.people], y=[p.position.y for p in population.people], c=colors)
plt.xlim([world.min_x, world.max_x])
plt.ylim([world.min_y, world.max_y])

plt.draw()
for timestep in range(1000):
    population.spread_disease()
    population.behave()
    x, y = [p.position.x for p in population.people], [p.position.y for p in population.people]
    sc.set_offsets(np.c_[x, y])
    disease_stage = [p.disease_stage for p in population.people]
    sc.set_facecolor(list(map(disease_stage_to_color, disease_stage)))
    plt.title(timestep)
    fig.canvas.draw_idle()
    plt.pause(0.01)

plt.waitforbuttonpress()

