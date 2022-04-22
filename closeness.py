"""
Our implementation for closeness centrality
"""

from tracemalloc import start
import networkx as nx
import matplotlib.pyplot as plt

from file_to_nx import *
from plotting import *

G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')

def closeness_centrality(G):
    # implementing the simplified case from initial research
    #nx.shortest_path(G, source = 2, target = 4))
    num_nodes = G.number_of_nodes()
    val_map = {}
    for start_node in G.nodes():
        l_paths = 0
        for end_node in G.nodes():
            if start_node != end_node:
                path = nx.shortest_path(G, start_node, end_node)
                len_path = len(path) - 1
                l_paths += len_path
        
        val_map[start_node] = (num_nodes - 1) / l_paths
    
    return val_map


val_map = closeness_centrality(G)
plot_colormap(G, nx_val_map)
