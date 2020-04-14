from typing import List
from Person import Person
from SimpleObjects import DiseaseStage


class Population:
    """represents a group of people"""
    def __init__(self, people: List[Person]):
        self.people = people
        self.size = len(people)

    def behave(self):
        for person in self.people:
            person.behave()

    def spread_disease(self):
        for host in self.people:
            if host.disease_stage == DiseaseStage.infected:
                for other in self.people:
                    if other is not host and host.position.distance_to(other.position) <= host.virus.contagion_radius:
                        host.spread_virus(other)

    def calculate_stats(self):
        susceptible, infected, recovered, deceased = 0, 0, 0, 0
        for person in self.people:
            if person.disease_stage == DiseaseStage.susceptible:
                susceptible += 1
            elif person.disease_stage == DiseaseStage.infected:
                infected += 1
            elif person.disease_stage == DiseaseStage.recovered:
                recovered += 1
            elif person.disease_stage == DiseaseStage.deceased:
                deceased += 1
            else:
                raise RuntimeError("Encountered Unknown Disease Stage")
        return {DiseaseStage.susceptible: susceptible,
                DiseaseStage.infected: infected,
                DiseaseStage.recovered: recovered,
                DiseaseStage.deceased: deceased}
