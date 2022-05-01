"""
Use pre-built NetworkX versions of our functions in order to get a sense of how
to work with the graphs we have created
"""

import networkx as nx
import matplotlib.pyplot as plt

from file_to_nx import *
from plotting import *

G = nx.Graph()
# G.add_edge(1, 2)
# G.add_edge(1, 3)
# G.add_edge(2, 3)
# G.add_edge(3, 5)
# G.add_edge(2, 5)
# G.add_edge(1, 4)
# G.add_edge(4, 5)
# G.add_edge(5, 6)
# G.add_edge(6, 7)
# G.add_edge(6, 9)
# G.add_edge(7, 9)
# G.add_edge(7, 8)
# G.add_edge(8, 9)
# G.add_edge(9, 10)
# G.add_edge(9, 11)
# G.add_edge(10, 11)

# G.add_edge(1, 2)
# G.add_edge(1, 3)
# G.add_edge(1, 4)
# G.add_edge(2, 3)
# G.add_edge(2, 5)
# G.add_edge(3, 5)
# G.add_edge(4, 5)


G.add_edge(1, 2)
G.add_edge(1, 5)
G.add_edge(2, 5)
G.add_edge(2, 3)
G.add_edge(3, 5)
G.add_edge(3, 4)
G.add_edge(4, 5)




degree = nx.degree_centrality(G)

closeness = nx.closeness_centrality(G, u=None, distance=None, wf_improved=True)

betw = nx.betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)

print("\nDegree")
print(degree)
print("Max: ", max(degree, key=degree.get))

print("\nCloseness")
print(closeness)
print("Max: ", max(closeness, key=closeness.get))

print("\nBetweenness")
print(betw)
print("Max: ", max(betw, key=betw.get))

plot_colormap(G, degree)
plot_colormap(G, closeness)
plot_colormap(G, betw)



# G.add_edge(1, 3)
# G.add_edge(1, 2)
# G.add_edge(2, 3)
# G.add_edge(2, 5)
# G.add_edge(3, 5)
# G.add_edge(1, 4)
# G.add_edge(4, 5)
# G.add_edge(5, 6)
# G.add_edge(5, 7)
# G.add_edge(7, 8)
# G.add_edge(7, 10)
# G.add_edge(8, 10)
# G.add_edge(8, 9)
# G.add_edge(9, 10)
# G.add_edge(10, 11)
# G.add_edge(10, 12)
# G.add_edge(10, 13)
# G.add_edge(12, 13)
# G.add_edge(8, 14)
# G.add_edge(13, 14)
