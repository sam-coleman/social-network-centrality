"""
Our implementation for degree centrality
"""

import networkx as nx
import matplotlib.pyplot as plt

from file_to_nx import *
from plotting import *

G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')

def degree_centrality(G):
    """
    Return degree centrality measure for all nodes in a graph.

    Args:
        G: A NetworkX Graph

    Returns:
        A dictionary with node:degree_centrality for each node in G.
    """
    val_map = {}
    NUM_NODES = G.number_of_nodes() - 1.0
    deg_list = G.degree() # list of tuples
    for n in deg_list:
        val_map[n[0]] = n[1] / NUM_NODES
    return val_map

if __name__ == "__main__":
    val_map = degree_centrality(G)
    plot_colormap(G, val_map)
