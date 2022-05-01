"""
Our implementation for betweenness centrality
"""

import networkx as nx
import matplotlib.pyplot as plt

from file_to_nx import *
from plotting import *

# G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 5)
G.add_edge(2, 5)
G.add_edge(2, 3)
G.add_edge(3, 5)
G.add_edge(3, 4)
G.add_edge(4, 5)


def find_pairs(all_nodes, node):
    pairs = []
    for i in range(len(all_nodes)):
        for j in range(i+1, len(all_nodes)):
            if all_nodes[i] != node and all_nodes[j] != node:
                pairs.append((all_nodes[i], all_nodes[j]))
    return pairs

def betweenness_centrality(G):
    val_map = {}
    all_nodes = list(G.nodes)
    for node in all_nodes:
        sum = 0
        pairs = find_pairs(all_nodes, node)
        for pair in pairs:
            pair_sum = 0
            source, target = pair
            paths = list(nx.all_shortest_paths(G, source, target))
            for path in paths:
                if node in path:
                    pair_sum += 1
            sum += (pair_sum / len(paths))
        val_map[node] = sum / len(pairs)
    return val_map


print(betweenness_centrality(G))
