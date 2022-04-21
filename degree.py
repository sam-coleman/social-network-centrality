"""
Our implementation for degree centrality
"""

import networkx as nx
import matplotlib.pyplot as plt

from file_to_nx import *
from plotting import *

G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')

def degree_centrality(G):
    val_map = {}
    num_nodes = G.number_of_nodes()
    deg_list = G.degree() # list of tuples
    for n in deg_list:
        val_map[n[0]] = n[1] / num_nodes
    return val_map


val_map = degree_centrality(G)
plot_colormap(G, val_map)
