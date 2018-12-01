#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:05:35 2018

@author: efrancois
"""
#Create tests for all the graph functions we have seen so
#far:
#• find_path
#• find_all_paths
#• find_path (weighted)
#• find_all_paths (weighted)


from Pathfinder import find_path

def test_find_path():
    
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["d"],
        "d": ["e"],
        "e":[],
        "f":[]
}

    start = "g"
    
    end = "d"
    
    
    assert find_path(graph, start, end) == None

    
from Pathfinder import find_all_paths

def test_find_all_paths():
    
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["d"],
        "d": ["e"],
        "e":[],
        "f":[]
}

    start = "a"
    
    end = "e"
    
    path = ["b"]
    
    assert find_all_paths(graph, start, end, path) == [['b', 'a', 'c', 'd', 'e']]
 
    
from Pathfinder import find_path_weighted

def test_find_path_weighted():
    
    graph = {
    "a": [{"node": "b", "weight": 1}, {"node": "c", "weight": 2}],
    "b": [{"node": "d", "weight": 3}],
    "c": [{"node": "d", "weight": 1}],
    "d": [{"node": "e", "weight": 3}],
    "e": [],
    "f": []
}
    
    start = "a"
    
    end = "e"
    
    path = []
    
    weight = 9
    
    assert find_path_weighted(graph, start, end, path, weight) == [{'node': 'a', 'weight': 9},
                             {'node': 'b', 'weight': 1},
                             {'node': 'd', 'weight': 3},
                             {'node': 'e', 'weight': 3}]
    
    
from Pathfinder import find_all_paths_weighted

def test_find_all_paths_weighted():
    
    graph = {
    "a": [{"node": "b", "weight": 1}, {"node": "c", "weight": 2}],
    "b": [{"node": "d", "weight": 3}],
    "c": [{"node": "d", "weight": 1}],
    "d": [{"node": "e", "weight": 3}],
    "e": [],
    "f": []
}
    
    start = "p"
    
    end = "a"
    
    path = ["c"]
    
    weight = 3
    
    assert find_all_paths_weighted(graph, start, end, path, weight) == []
    


    
    
    
    



