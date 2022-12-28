from eckity.genetic_operators.genetic_operator import GeneticOperator

from ManipultateColors import mutate

# from ColoredGraphEvaluator import ColoredGraphEvaluator
from ColoredGraphCreator import ColoredGraphCreator
from ColoredGraph import ColoredGraph

class ColoredMutate(GeneticOperator):
    def __init__(self, probability=1, arity=1, events=None):
        super().__init__(probability, 1, events)

    def apply(self, individuals):
        for i in range(len(individuals)):
            cg: ColoredGraph = individuals[i]
            cg_colors = cg.get_colors()
            new_colors = mutate(cg_colors, cg.num_of_colors)
            cg.set_colors(new_colors)

        self.applied_individuals = individuals
        return individuals



#
# if __name__ == '__main__':
#     print("compiled")
#     cgc = ColoredGraphCreator()
#     individuals = cgc.create_individuals(10, higher_is_better=False)
#     cg_individual = individuals[0]
#     cm = ColoredMutate()
#     cm.apply(individuals)
#     # cg_individual_is_modified = individulas[0]
#     print("OK finished!")
