from random import randrange
import pandas as pd
from eckity.individual import Individual
from eckity.fitness.simple_fitness import SimpleFitness
from Graph import Graph
from Data import Data
from ManipultateColors import init_random_colors

class ColoredGraph(Individual):
    def __init__(self, graph, num_of_vertices, num_of_colors, colors):
        super().__init__(SimpleFitness())
        self.graph = graph
        self.num_of_vertices = num_of_vertices
        self.num_of_colors = num_of_colors
        self.colors = colors

    def get_graph(self):
        return self.graph

    def get_num_of_colors(self):
        return self.num_of_colors

    def get_colors(self):
        return self.colors

    def set_colors(self, colors):
        self.colors = colors
        self.graph.load_vertices_colors(colors)
        self.graph.reset_collisions()


    # override - Individual interface
    def show(self):
        # res = []
        # for lect in self._lectures:
        #     res.append(str(lect))
        # print("\n".join(res), "\nBest Fitness:")
        colors = self.get_colors()
        adj_list = self.graph.print_adjacency_list()
        print(f'colors: {colors}\n{adj_list}\ncollisions: {self.graph.get_collisions()}')




#
# if __name__ == '__main__':
#     NUM_OF_VERTICES = 5
#     NUM_OF_COLORS = 3
#     graph = Graph(NUM_OF_VERTICES)
#     graph.load_adjacency_list(Data.edges_list5)
#     graph.load_vertices_colors(init_random_colors(NUM_OF_VERTICES, NUM_OF_COLORS))
#     graph.print_adjacency_list()
#     cg = ColoredGraph(graph, NUM_OF_VERTICES, NUM_OF_COLORS)
#     print("22")
