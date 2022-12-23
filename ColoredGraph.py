from random import randrange
import pandas as pd
from eckity.individual import Individual
from eckity.fitness.simple_fitness import SimpleFitness
import Graph


class ColoredGraph(Individual):
    def __init__(self, graph, number_of_colors):
        super().__init__(SimpleFitness())
        self.graph = graph
        # self.number_of_vertices
        self.number_of_colors = number_of_colors
        self.colors = []

    def init_with_random(self):
        for i in range(self.graph.nun_of_vertices):
            self.colors[i] = randrange(self.number_of_colors)


if __name__ == '__main__':
    number_of_colors = 3
    print(randrange(number_of_colors))
