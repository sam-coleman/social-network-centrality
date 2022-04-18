"""
Our implementation for betweenness centrality
"""

import networkx as nx
import matplotlib.pyplot as plt

from file_to_nx import *
from plotting import *

G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')

def betweenness_centrality(G):
    pass

# val_map = betweenness_centrality(G)
# plot_colormap(G, val_map)
