from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator

from ColoredGraph import ColoredGraph

from ColoredGraphCreator import ColoredGraphCreator


class ColoredGraphEvaluator(SimpleIndividualEvaluator):
    def __init__(self) -> None:
        super().__init__()

    def _evaluate_individual(self, colored_graph: ColoredGraph):

        collisions = 0
        for vertice in colored_graph.get_graph().get_adjacency_list():
            for neighbour in vertice.get_neighbours():
                if vertice.get_color() == neighbour.get_color():
                    if vertice.get_is_legal():
                        collisions += 1
                        colored_graph.get_graph().inc_collisions()
                        vertice.set_is_legal(False)
                    if neighbour.get_is_legal():
                        collisions += 1
                        colored_graph.get_graph().inc_collisions()
                        neighbour.set_is_legal(False)
        return collisions

# if __name__ == '__main__':
#     print("compiled")
#     cge = ColoredGraphEvaluator()
#     cgc = ColoredGraphCreator()
#     individulas = cgc.create_individuals(10, higher_is_better=False)
#     cg_individual = individulas[0]
#     evaluator = ColoredGraphEvaluator()
#     return_val = evaluator.evaluate_individual(cg_individual)
#     print("OK finished!")

