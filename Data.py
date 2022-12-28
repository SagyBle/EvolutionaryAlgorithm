import random


class Data:

    NUM_OF_VERTICES = 5
    NUM_OF_COLORS = 3

    edges_list0 = [(0, 1), (1, 2), (3, 4), (0, 4)]
    edges_list1 = [(0, 2), (1, 3), (0, 3)]
    edges_list2 = [(0, 2), (0, 3), (0, 4), (2, 4)]
    edges_list3 = [(1, 3), (1, 2), (3, 4), (0, 2)]
    edges_list4 = [(0, 4), (1, 3), (3, 4), (0, 3)]
    edges_lists = [edges_list0, edges_list1, edges_list2, edges_list3, edges_list4]

    def get_edgelist(self):
        return self.edges_lists[random.randrange(0, len(self.edges_lists))]

