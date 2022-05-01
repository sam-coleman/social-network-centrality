"""
Advanced Algorithms Centrality Homework
Olin College of Engineering
Helper file to read list of edges and create NetworkX graph
"""

import networkx as nx

def create_graph(file_path, delim = None):
    """
    Return a NetworkX Graph from edgelist

    Args:
        file_path: A string representing path to txt file/
        delim: A string representing the delimiter between the two nodes

    Returns:
        A NetworkX undirected graph
    """
    return nx.read_edgelist(file_path, delimiter = delim)
