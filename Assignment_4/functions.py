# -*- coding: utf-8 -*-
#%%

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
    
    path = path + [start]
  
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath is not None:
                return newpath
    return None

def find_all_paths(graph, start, end, path=[]):

    path = path + [start]
    
    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []    

    for node in graph[start]:        
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


graph_weighted = {
    "a": [{"node": "b", "weight": 1}, {"node": "c", "weight": 2}],
    "b": [{"node": "d", "weight": 3}],
    "c": [{"node": "d", "weight": 1}],
    "d": [{"node": "e", "weight": 3}],
    "e": [],
    "f": []
}

def find_path_weighted(graph_weighted, start, end, path=[], weight=0):
    
    path = path + [{"node": start, "weight": weight}]
    
    if start == end:
        return path
    if not start in graph:
        return None
    for conn in graph_weighted[start]:
        if conn["node"] not in path:
            newpath = find_path_weighted(graph_weighted, conn["node"], end, path, conn["weight"])
            if newpath is not None:
                return newpath
    return None

def find_all_paths_weighted(graph_weighted, start, end, path=[], weight=0):
    
    path = path + [{"node": start, "weight": weight}]

    if start == end:
        return [path]
    if not start in graph_weighted:
        return []

    paths = []
    
    for conn in graph_weighted[start]:
        if conn not in path:
            newpaths = find_all_paths_weighted(graph_weighted, conn["node"], end, path, conn["weight"])            
            for newpath in newpaths:
                paths.append(newpath)
    return paths
