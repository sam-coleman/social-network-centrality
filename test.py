"""
This file is used to test your implementation by comparing it to the built-in
networx equivalents of the functions.
"""

import networkx as nx
import pytest

from file_to_nx import create_graph
from betweenness import betweenness_centrality
from degree import degree_centrality
from closeness import closeness_centrality

# G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')
G = create_graph('data/fb-pages-food/fb-pages-food.edges', delim = ' ')
# G = create_graph('data/soc-wiki-Vote/soc-wiki-Vote.txt', delim = ' ')


def test_degree():
    impn = degree_centrality(G)
    ref = nx.degree_centrality(G)
    assert len(impn) == len(ref)
    for node in ref:
        assert impn[node] is not None
        assert abs(impn[node] - ref[node]) < 0.001

def test_closeness():
    impn = closeness_centrality(G)
    ref = nx.closeness_centrality(G)
    assert len(impn) == len(ref)
    for node in ref:
        assert impn[node] is not None
        assert abs(impn[node] - ref[node]) < 0.001

def test_betweenness():
    impn = betweenness_centrality(G)
    ref = nx.betweenness_centrality(G)
    assert len(impn) == len(ref)
    for node in ref:
        assert impn[node] is not None
        assert abs(impn[node] - ref[node]) < 0.001
