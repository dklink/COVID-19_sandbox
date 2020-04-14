import matplotlib.pyplot as plt

from Environment import Environment
from Population import Population
from SimpleObjects import DiseaseStage


class SimulationViewer:
    def __init__(self, world: Environment, population: Population):
        self.fig, axes = plt.subplots(2, 1)
        self.ax0, self.ax1 = axes

        self.ax0.set_xlim([world.min_x, world.max_x])
        self.ax0.set_ylim([world.min_y, world.max_y])
        self.ax0.tick_params(labelbottom=False, labelleft=False)

        self._I_line = None

    def update_population_view(self, population: Population, timestep: int):
        disease_stage = [p.disease_stage for p in population.people]
        colors = list(map(disease_stage_to_color, disease_stage))
        self.ax0.clear()
        sc = self.ax0.scatter(x=[p.position.x for p in population.people], y=[p.position.y for p in population.people],
                              c=colors)
        self.ax0.set_title(timestep)
        self.fig.canvas.draw_idle()
        plt.pause(0.0001)

    def update_progress_chart(self, I, IS, ISR, ISRD):
        t = list(range(len(I)))
        '''
        if self._I_line is None:
            self._I_line, = self.ax1.plot(t, I, color=disease_stage_to_color(DiseaseStage.infected))
            self.ax1.set_ylim([0, 100])
        else:
            self._I_line.set_xdata(t)
            self._I_line.set_ydata(I)
            self.ax1.set_xlim([0, t[-1]])'''
        self.ax1.fill_between(t, 0, I, color=disease_stage_to_color(DiseaseStage.infected))
        self.ax1.fill_between(t, I, IS, color=disease_stage_to_color(DiseaseStage.susceptible))
        self.ax1.fill_between(t, IS, ISR, color=disease_stage_to_color(DiseaseStage.recovered))
        self.ax1.fill_between(t, ISR, ISRD, color=disease_stage_to_color(DiseaseStage.deceased))
        plt.pause(.0001)


def disease_stage_to_color(disease_stage):
    if disease_stage == DiseaseStage.infected:
        return 'tab:orange'
    elif disease_stage == DiseaseStage.susceptible:
        return 'b'
    elif disease_stage == DiseaseStage.recovered:
        return 'g'
    elif disease_stage == DiseaseStage.deceased:
        return 'k'
