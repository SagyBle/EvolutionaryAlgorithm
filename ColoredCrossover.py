import ManipultateColors
from eckity.genetic_operators.genetic_operator import GeneticOperator
from random import randrange
from ColoredGraph import ColoredGraph


class scheduleCrossover(GeneticOperator):
    def __init__(self, probability=1, arity=2, events=None):
        super().__init__(probability, arity, events)

    def apply(self, individuals: [ColoredGraph]):


        self.applied_individuals = individuals
        return individuals
