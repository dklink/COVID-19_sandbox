from random import random

from SimpleObjects import Position, DiseaseStage
import Behavior


class Person:
    """represents a person in the simulation"""
    def __init__(self, initial_position: Position, behavior: Behavior):
        self.position = initial_position
        self.behavior = behavior
        self.disease_stage = DiseaseStage.susceptible
        self.virus = None
        self.hours_left_in_infection = None

    def behave(self):
        """does its thing for 1 hour"""
        if self.disease_stage != DiseaseStage.deceased:
            self.position = self.behavior.update_position(self.position)

        if self.hours_left_in_infection is not None:
            if self.hours_left_in_infection <= 0:
                if random() < self.virus.death_rate:
                    self.disease_stage = DiseaseStage.deceased
                else:
                    self.disease_stage = DiseaseStage.recovered
                self.hours_left_in_infection = None
                self.virus = None
            else:
                self.hours_left_in_infection -= 1

    def get_infected(self, virus):
        self.virus = virus
        self.disease_stage = DiseaseStage.infected
        self.hours_left_in_infection = virus.infection_duration * 24

    def spread_virus(self, other: 'Person'):
        """Determines whether virus spreads over course of 1 hour of proximity"""
        # check if infection possible
        if self.disease_stage == DiseaseStage.infected and other.disease_stage == DiseaseStage.susceptible:
            # roll the dice
            if random() < self.virus.transmission_probability:
                other.get_infected(self.virus)
