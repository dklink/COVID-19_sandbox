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

from SimulationViewer import SimulationViewer


import cProfile

pr = cProfile.Profile()
pr.enable()

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
population.people[0].get_infected(covid)

# run behaviors, plot

# initialize graphics
graphics = SimulationViewer(world, population)

susceptible_and_infected = []
infected = []
recovered = []
all_but_deceased = []

timestep = 1
while True:
    population.spread_disease()
    population.behave()
    # update population view
    graphics.update_population_view(population, timestep)

    # update progress chart
    stats = population.calculate_stats()
    susceptible_and_infected.append(stats[DiseaseStage.susceptible] + stats[DiseaseStage.infected])
    infected.append(stats[DiseaseStage.infected])
    all_but_deceased.append(population.size - stats[DiseaseStage.deceased])
    graphics.update_progress_chart(infected, susceptible_and_infected, all_but_deceased, population.size)

    if stats[DiseaseStage.infected] == 0:  # eradicated
        break
    timestep += 1
    print(timestep)

pr.disable()
# after your program ends
pr.print_stats(sort="tottime")