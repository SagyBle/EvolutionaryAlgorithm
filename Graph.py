import numpy as np
import random
import time
from queue import Queue

from Vertice import Vertice

# for n = 4, an example for edges list.
edges_list0 = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]

# initial colors array (will be randomly generated)
colors0 = [0, 1, 2, 1, 1]


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

    # colors0 = [0, 1, 2, 1, 0]
    def load_vertices_colors(self, vertices_colors):
        for i in range(len(vertices_colors)):
            self.adjacency_list[i].set_color(vertices_colors[i])

    def inc_collisions(self):
        self.num_of_collisions += 1

    def investigate_graph_collisions(self):
        for vertice in self.adjacency_list:
            for neighbour in vertice.get_neighbours():
                if vertice.get_color() == neighbour.get_color():
                    if vertice.get_is_legal():
                        graph.inc_collisions()
                        vertice.set_is_legal(False)
                    if neighbour.get_is_legal():
                        graph.inc_collisions()
                        vertice.set_is_legal(False)

        print(f'collisions number: {self.num_of_collisions}')

    def print_adjacency_list(self):
        print("graph adjacency list:")
        for vertice in self.adjacency_list:
            vertice_str = f'(v{vertice.get_index()}, c{vertice.get_color()})'
            neighbors_str = ""
            for neighbor in vertice.neighbours:
                neighbors_str += f'(v{neighbor.get_index()}, c{neighbor.get_color()}), '
            if neighbors_str == "":
                neighbors_str = "no neighbours"
            else:
                neighbors_str = neighbors_str[:-2]
            print(f'{vertice_str} -> {neighbors_str}')


if __name__ == '__main__':
    graph = Graph(5)
    graph.load_adjacency_list(edges_list0)
    graph.load_vertices_colors(colors0)
    graph.print_adjacency_list()

    graph.investigate_graph_collisions()
