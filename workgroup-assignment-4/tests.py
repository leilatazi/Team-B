#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create tests for all the graph functions we have seen so
far:
• find_path
• find_all_paths
• find_path (weighted)
• find_all_paths (weighted)
"""
#%%
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
}

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

find_path(graph, "d", "e")

#%%
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
}

def find_all_paths(graph, start, end, path=[], connection=[]): 
    
    path = path + [start] #create a new list instead of modifying the old one
    
    if start == end:
        return [path]
    
    if start not in graph:
        return []
    
    paths = []

    for connection in graph[start]:      
        
        if connection not in path:
            new_paths = find_all_paths(graph, connection, end, path)
            
            for new_path in new_paths:
                paths.append(new_path)
                
    return paths

find_all_paths(graph, "a", "d")

#%%


graph = {
    "a": [{"node": "b", "weight": 1}, {"node": "c", "weight": 2}],
    "b": [{"node": "d", "weight": 3}],
    "c": [{"node": "d", "weight": 4}],
    "d": [{"node": "e", "weight": 5}],
    "e": {},
    "f": {}
}

def find_path_weighted(graph, start, end, path=[], weight=0): 
    
    path = path + [{"node": start, "weight": weight}] 
    
    if start == end:
        return path
    
    if start not in graph:
        return None
    
    for connection in graph[start]:
    
        if connection not in path:
            new_path = find_path_weighted(path,
                                          connection["node"],
                                          end,
                                          path, 
                                          connection["weight"])
        
            if new_path is not None:
                return new_path
            
    return None

find_path_weighted(graph, "a", "c")