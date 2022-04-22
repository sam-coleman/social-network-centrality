"""
Plotting
"""

import networkx as nx
import matplotlib.pyplot as plt

def plot_colormap(G, val_map):
    """
    Plots a matplotlib plot of the graph with each node's color corresponding to
        its centrality value
    Inputs
        G: a networkx graph
        val_map: a dictionary of each node to its centrality value
    """
    values = [val_map.get(node, 0.25) for node in G.nodes()]
    cmap=plt.get_cmap('viridis')
    layout = nx.spring_layout(G, seed = 100)
    nx.draw(
        G,
        pos = layout,
        node_size=15,
        width=0.5,
        cmap=plt.get_cmap('viridis'),
        node_color=values,
        with_labels=False,
        font_color='black'
    )
    vmin = min(val_map.values())
    vmax = max(val_map.values())
    colorscale = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    plt.colorbar(colorscale)
    plt.show()
