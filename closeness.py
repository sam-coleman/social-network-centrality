"""
Our implementation for closeness centrality
"""

import networkx as nx
import matplotlib.pyplot as plt

from file_to_nx import *
from plotting import *

# G = create_graph('data/soc-wiki-Vote/soc-wiki-Vote.txt', delim = ' ')
G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')

def closeness_centrality(G):
    """
    Return closeness centrality measure for all nodes in a graph.

    Args:
        G: A NetworkX Graph

    Returns:
        A dictionary with node:closeness_centrality for each node in G.
    """
    NUM_NODES = G.number_of_nodes()
    val_map = {}
    for start_node in G.nodes():
        l_all_paths = 0 # sum of lengths of shortest path for start_node
        for end_node in G.nodes():
            if start_node != end_node:
                path = nx.shortest_path(G, start_node, end_node) # get shortest path
                len_path = len(path) - 1 # get number of edges in shortest path
                l_all_paths += len_path

        val_map[start_node] = (NUM_NODES - 1) / l_all_paths

    return val_map

if __name__ == "__main__":
    val_map = closeness_centrality(G)
    plot_colormap(G, val_map)
