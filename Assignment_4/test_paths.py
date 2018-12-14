# -*- coding: utf-8 -*-
#%%
from functions import find_path
from functions import find_all_paths
from functions import find_path_weighted
from functions import find_all_paths_weighted


graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["d"],
        "d": ["e"],
        "e":[],
        "f":[]
}

graph_weighted = {
    "a": [{"node": "b", "weight": 1}, {"node": "c", "weight": 2}],
    "b": [{"node": "d", "weight": 3}],
    "c": [{"node": "d", "weight": 1}],
    "d": [{"node": "e", "weight": 3}],
    "e": [],
    "f": []
}
    
def test_find_path_from_a_to_d():
    assert find_path(graph, "a", "d") == ['a', 'b', 'd']
    
def test_find_path_no_path():
    assert find_path(graph, "a", "f") == None
    
def test_find_path_start_not_in_nodes():
    assert find_path(graph, "h", "b") == None
    
def test_find_all_paths_from_a_to_d():
    assert find_all_paths(graph, "a", "d") == [['a', 'b', 'd'], ['a', 'c', 'd']]
    
def test_find_all_paths_no_paths():
    assert find_all_paths(graph,"a","f") == []
    
def test_find_path_end_not_in_nodes():
    assert find_all_paths(graph, "b", "h") == []
    
def test_find_path_weighted_from_a_to_e():
    assert find_path_weighted(graph_weighted, "a", "e") == [{'node': 'a', 'weight': 0},
                                                     {'node': 'b', 'weight': 1},
                                                     {'node': 'd', 'weight': 3},
                                                     {'node': 'e', 'weight': 3}]
    
def test_find_path_weighted_end_not_in_graph():
    assert find_path_weighted(graph_weighted, "a", "h") == None

def test_find_path_weighted_no_path():
    assert find_path_weighted(graph_weighted, "a", "f") == None  
    
def find_all_paths_weighted_from_a_to_e():
    assert find_all_paths_weighted(graph_weighted, "a", "e") == [[{'node': 'a', 'weight': 0},
                                                                  {'node': 'b', 'weight': 1},
                                                                  {'node': 'd', 'weight': 3},
                                                                  {'node': 'e', 'weight': 3}],
                                                                 [{'node': 'a', 'weight': 0},
                                                                  {'node': 'c', 'weight': 2},
                                                                  {'node': 'd', 'weight': 1},
                                                                  {'node': 'e', 'weight': 3}]]
        
def find_all_paths_weighted_no_path():
    assert find_all_paths_weighted(graph_weighted, "c", "f") == []
