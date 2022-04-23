import networkx as nx
import matplotlib.pyplot as plt

from file_to_nx import *
from plotting import *

def closeness_centrality(G):
    """
    Return closeness centrality measure for all nodes in a graph.

    Args:
        G: A NetworkX Graph

    Returns:
        A dictionary with node:closeness_centrality for each node in G.
    """
    # TODO: your implementation here

    return {}

def betweenness_centrality(G):
    """
    Return betweenness centrality measure for all nodes in a graph.

    Args:
        G: A NetworkX Graph

    Returns:
        A dictionary with node:betweenness_centrality for each node in G.
    """
    # TODO: your implementation here

    return {}


if __name__ == "__main__":
    # use create_graph function from file_to_nx file to make a networkx graph from
    # data from here: https://networkrepository.com/network-data.php
    G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')

    val_map_closeness = closeness_centrality(G)
    val_map_betweenness = betweenness_centrality(G)
    # plot_colormap(G, val_map) #TODO: uncomment this and sub out val_map when you finish your implementation
