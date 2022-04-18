"""
Use pre-built NetworkX versions of our functions in order to get a sense of how
to work with the graphs we have created
"""

import networkx as nx
import matplotlib.pyplot as plt

from file_to_nx import *
from plotting import *

G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')

# nx.draw(G, node_size=10, width=0.5)
# plt.show()

# val_map = nx.degree_centrality(G)

# val_map = nx.closeness_centrality(G, u=None, distance=None, wf_improved=True)

val_map = nx.betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)

plot_colormap(G, val_map)
