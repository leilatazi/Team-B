#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Investigate the NetworkX library. Create an instance of
a digraph like the one we saw in class.

graph = {
"a": ["b", "c"],
"b": ["d"],
1
"c": ["d"],
"d": ["e"],
"e": [],
"f": []
}

1. Find NetworkX’ functions that do the following:
• see if there’s a path between two nodes
• find the shortest path between two nodes

2. Find a way to draw the graph using networkx and matplotlib libraries.

"""

#%%

#%%

import networkx

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
}

graph = networkx.Graph(graph)
networkx.draw_spring(graph)

def find_path(graph, start, end, path=[]): 
    
    path = path + [start] #create a new list instead of modifying the old one
    
    if start == end:
        return path
    
    if start not in graph:
        return None
    
    for connection in graph[start]:
        
        if connection not in path:
            new_path = find_path(path, connection, end, path)
            
            if new_path is not None:
                return new_path
            
    return None

find_path(graph, "a", "c")