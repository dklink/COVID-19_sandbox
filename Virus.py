from random import random

from Person import Person
from SimpleObjects import DiseaseStage


class Virus:
    """represents a virus, parameterizes its behavior"""
    def __init__(self, contagion_radius, transmission_probability, infection_duration, death_rate):
        self.contagion_radius = contagion_radius
        self.transmission_probability = transmission_probability
            # definition: the probability that the virus spreads from a host to a new person,
                # given that the new person is within contagion_radius of the host for one hour
        self.infection_duration = infection_duration
        self.death_rate = death_rate


covid = Virus(contagion_radius=2,  # meters, this is kind of a "seems reasonable" value
              transmission_probability=1,  # ??? this is unknown irl.  But we do have estimates of the daily transmission rate (https://doi.org/10.1016/S1473-3099(20)30144-4), so we can reverse-engineer this.
              infection_duration=5,  # days DOI: 10.1056/NEJMoa2001316
              death_rate=0.0066)  # https://doi.org/10.1016/S1473-3099(20)30243-7
