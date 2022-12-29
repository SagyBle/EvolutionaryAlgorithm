import numpy as np
import random
import time
from queue import Queue
from Vertice import Vertice
from ManipultateColors import mutate, crossover, init_random_colors


class Graph:
    def __init__(self, num_of_vertices: int):
        self.num_of_vertices = num_of_vertices
        self.num_of_collisions = 0

        arr = [0 for i in range(self.num_of_vertices)]
        for i in range(0, self.num_of_vertices):
            arr[i] = Vertice(i, '*')

        self.adjacency_list = arr

    # given edges list (list of tuples of (int:int)),
    def load_adjacency_list(self, edges_list: [(int, int)]):
        for (i, j) in edges_list:
            self.adjacency_list[i].add_neighbour(self.adjacency_list[j])

    def get_adjacency_list(self):
        return self.adjacency_list

    # colors0 = [0, 1, 2, 1, 0]
    def load_vertices_colors(self, vertices_colors):
        for i in range(len(vertices_colors)):
            # set vertice color to new color
            self.adjacency_list[i].set_color(vertices_colors[i])
            # set is legal to true (in the next stage it'll update)
            self.adjacency_list[i].set_is_legal(True)
        self.reset_collisions()

    def inc_collisions(self):
        self.num_of_collisions += 1
    def get_collisions(self):
        return self.num_of_collisions

    def reset_collisions(self):
        self.num_of_collisions = 0

    def evaluate_fitness(self):
        for vertice in self.adjacency_list:

            for neighbour in vertice.get_neighbours():
                if vertice.get_color() == neighbour.get_color():
                    if vertice.get_is_legal():
                        graph.inc_collisions()
                        vertice.set_is_legal(False)
                    if neighbour.get_is_legal():
                        graph.inc_collisions()
                        neighbour.set_is_legal(False)


    def print_adjacency_list(self):
        print("graph adjacency list:")
        for vertice in self.adjacency_list:
            vertice_str = f'(v{vertice.get_index()}, c{vertice.get_color()}, legal:{vertice.get_is_legal()})'
            neighbors_str = ""
            for neighbor in vertice.neighbours:
                neighbors_str += f'(v{neighbor.get_index()}, c{neighbor.get_color()}, legal:{neighbor.get_is_legal()}), '
            if neighbors_str == "":
                neighbors_str = "no neighbours"
            else:
                neighbors_str = neighbors_str[:-2]
            print(f'{vertice_str} -> {neighbors_str}')





if __name__ == '__main__':
    NUM_OF_VERTICES = 5
    NUM_OF_COLORS = 3
    # 1) init graph with number of vertices
    graph = Graph(NUM_OF_VERTICES)

    # *USER* given edge list
    edges_list0 = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]
    # 2)  load adjacency to graph
    graph.load_adjacency_list(edges_list0)

    # given colors array
    colors0 = [0, 1, 2, 1, 1]
    colors1 = [2, 1, 0, 1, 0]

    # 3) color graph vertices
    graph.load_vertices_colors(colors0)
    graph.print_adjacency_list()

    # 4) count collisions by running on adjacency list
    graph.evaluate_fitness()

    # 5) create new individual
    colors0 = init_random_colors(NUM_OF_VERTICES, NUM_OF_COLORS)
    colors1 = [0, 1, 2, 1, 0]  # a mutation in colors0
    colors2 = [0, 1, 0, 1, 0]  # a crossover between 2 old colors array

    # 3) load colors on graph
    # it'll probably create a new graph instant
    graph.load_vertices_colors(colors1)

    # 4) investigate (count) collisions by running on adjacency list
    graph.evaluate_fitness()

    # we can use this functions to modify colors array
    print(colors0)
    mutate(colors0, NUM_OF_COLORS)
    print(colors0)
