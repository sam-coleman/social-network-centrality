# betweenness centrality
"""
Our implementation for betweenness centrality
"""

import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

from regex import P

from file_to_nx import *
from plotting import *

G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')


G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 5)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

print(nx.betweenness_centrality(G))
# def betweenness_centrality(G):
#     # val_map = {}
#     # pairs = list(combinations(G.nodes(), 2))
#     # for node in G.nodes():
#     #     num_in_path = 0
#     #     num_paths = 0
#     #     for pair in pairs:
#     #         if node not in pair:
#     #             all_shortest_paths = nx.all_shortest_paths(G, pair[0], pair[1])
#     #             for path in all_shortest_paths:
#     #                 if node in path:
#     #                     num_in_path += 1
#     #                 num_paths += 1
            
#     #     val_map[node] = num_in_path / num_paths
        
#     # return val_map

#     val_map = {}
#     pairs = list(combinations(G.nodes(), 2))
#     all_paths = []
#     flag = 0
#     for start_node in G.nodes():
#         for end_node in G.nodes():
#             shortest = list(nx.all_shortest_paths(G, start_node, end_node))
#             print(shortest)
#             print(all_paths)
#             flag += 1
#             if flag == 10:
#                 return
#             #all_paths.append(list(nx.all_shortest_paths(G, start_node, end_node)))
#     #print(len(all_paths))
#     #return 
#     for node in G.nodes():
#         num_in_path = 0
#         for path in all_paths:
#             print(path)
#             if node in path:
#                 print("in path")
#                 num_in_path += 1
        
#         val_map[node] = num_in_path/len(all_paths)
    
#     print(val_map)
#     return val_map


# betweenness_centrality(G)
# impn = betweenness_centrality(G)
# ref = nx.betweenness_centrality(G)
# print(impn == ref)
# for node in impn:
#     if abs(impn[node] - ref[node]) < 0.001:
#         print(f"{node} is true {impn[node] - ref[node]}")
#     else:
#         print(f"{node} is false, {impn[node] - ref[node]}")







# def betweenness_centrality(G):
#     val_map = {}
#     pairs = list(combinations(G.nodes(), 2))

#     for node in G.nodes():
#         num_in_path = 0
#         num_paths = 0
#         for pair in pairs:
#             if node not in pair:
#                 path = nx.shortest_path(G, pair[0], pair[1]) # get shortest path
#                 if node in path:
#                     num_in_path += 2
#             num_paths += 2
        
#         val_map[node] = num_in_path / num_paths
    
#     return val_map
#     # for start_node in G.nodes():
#     #     num_in = 0
#     #     for end_node in G.nodes():
#     #         if start_node != end_node:
#     #             path = nx.shortest_path(G, start_node, end_node) # get shortest path


# # # val_map = betweenness_centrality(G)
# # # nx_map = nx.betweenness_centrality(G)
# # # print(val_map == nx_map)
# # # plot_colormap(G, val_map)

# impn = betweenness_centrality(G)
# ref = nx.betweenness_centrality(G)
# print(impn == ref)
# for node in impn:
#     if abs(impn[node] - ref[node]) < 0.001:
#         print(f"{node} is true {impn[node] - ref[node]}")
#     else:
#         print(f"{node} is false, {impn[node] - ref[node]}")


# """
# Our implementation for betweenness centrality
# """
# import math
# import networkx as nx
# import matplotlib.pyplot as plt
# from sklearn import neighbors

# from file_to_nx import *
# from plotting import *
# # from collections import queue
# from itertools import combinations

# G = create_graph('data/soc-dolphins/soc-dolphins.txt', delim = ' ')

# # def betweenness_centrality(G):
    
# #     val_map = dict()
# #     nodes = G.nodes()
# #     combos = combinations(nodes, 2)
# #     for node in nodes:
# #         num_paths = 0
# #         num_in_path = 0
# #         for combo in combos:
# #             if node == "11":
# #                 print(combo)
# #             if node not in combo:
# #                 shortest_paths = nx.all_shortest_paths(G, combo[0], combo[1])
# #                 #print(len(list(shortest_paths)))
# #                 #print(shortest_paths)
# #                 # print(list(shortest_paths))
# #                 for shortest_path in shortest_paths:
# #                     #print(shortest_path)
# #                     # if node == "1":
# #                     #     print(shortest_path)
# #                     num_paths += 2
# #                     if node in shortest_path:
# #                         num_in_path += 2
# #         # print(start_node)
# #         if num_paths == 0:
# #             print(f"num_paths is 0, num_in_path: {num_in_path}")
# #         val_map[node] = num_in_path/(num_paths)
# #     return val_map

# print(betweenness_centrality(G))
# # if name == "__main__":
# #     B = betweenness_centrality(G)
# #     v_map = nx.betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)
# #     if B == v_map:
# #         print("True")
# #     else:
# #         print("B: ", B)
# #         print("Valmap: ", v_map)


# # val_map = betweenness_centrality(G)
# # plot_colormap(G, val_map)

