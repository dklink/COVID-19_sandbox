from typing import List
from Person import Person
from SimpleObjects import DiseaseStage


class Population:
    """represents a group of people"""
    def __init__(self, people: List[Person]):
        self.people = people

    def behave(self):
        for person in self.people:
            person.behave()

    def spread_disease(self):
        for host in self.people:
            if host.disease_stage == DiseaseStage.infected:
                for other in self.people:
                    if other is not host and host.position.distance_to(other.position) <= host.virus.contagion_radius:
                        host.spread_virus(other)
