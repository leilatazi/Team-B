#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 18:22:33 2018

@author: Javier
"""

#%%

#%%

"""
Investigate the NetworkX library. Create an instance of
a digraph like the one we saw in class.
"""

import networkx as nx

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
}

graph = nx.Graph(graph)
nx.draw_spring(graph, with_labels=True)

#%%

"""
1. Find NetworkX’ functions that do the following:
"""

""" see if there’s a path between two nodes """
nx.has_path(graph, "a", "d")


"""find the shortest path between two nodes"""

nx.dijkstra_path(graph, "a", "d")

#%%
"""
2. Find a way to draw the graph using networkx and matplotlib libraries.
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4,5])
G.add_edges_from([(1, 2), (2, 1), (2, 3)])

nx.draw(G,with_labels=True, node_size=500)
plt.title("Drawing the graph")
plt.show()


#%%

import networkx as nx

G = nx.Graph()
G.add_edge("Javi","Leila",color='r',weight=10)
G.add_edge("Leila","Edem",color='y',weight=4)
G.add_edge("Hannah","Felix",color='w',weight=6)
G.add_edge("Hannah","Leila",color='g',weight=6)
G.add_edge("Edem","Thibault",color='m',weight=20)
G.add_edge("Felix","Javi",color='b',weight=8)
G.add_edge("Thibault","Hannah",color='k',weight=22)
G.add_edge("Pepe", "Pepe",color='k',weight=0)

pos = nx.circular_layout(G)

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
weights = [G[u][v]['weight'] for u,v in edges]
nx.draw(G, pos, edges=edges,node_color="lightsalmon", edge_color=colors, width=weights, with_labels=True, node_size=2700)