# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:45:16 2018

@author: Leila
"""

# -*- coding: utf-8 -*-
#%%

class Node:
    
    def __init__(self,name,edges):
        self.name = name
        self.edges = edges
        
    def add_edges(self,node, weight):
        self.edges.append({"node":node, "weight":weight})      
        
class Graph:
    
    def __init__(self,nodelist):
        self.nodelist = nodelist
        
    def get_edges(self,name):
        
        edges = []
        
        for node in self.nodelist:
            if node.name == name:
                edges += node.edges
        
        return edges
        
    def get_nodes(self,name):
        
        nodes = []
        
        for node in self.nodelist:
            if node.name == name:
                nodes += node.name
    
        return nodes
 
    def find_all_paths(self, start, end, path=[], weight=0):
        
        path = path + [{"node": start, "weight": weight}]
    
        if start == end:
            return [path]
    
##        if not start in graph:
##            return []
#    
        paths = []
        
        for conn in self.get_edges(start):
            if conn not in path:
                newpaths = self.find_all_paths(conn["node"],end,path,conn["weight"])
                
                for newpath in newpaths:
                    paths.append(newpath)
    
        return paths
    
    def cheapest_path(self, start, end):
        all_paths = self.find_all_paths(start, end)
        
        cheapest = None
        
        for path in all_paths:
            cost = 0
            
            for step in path:
                cost += step["weight"]
                
            if cheapest is None or cost < cheapest:
                cheapest = cost
                
        return cheapest
    

a = Node("a",["b"])
b = Node("b",["c"])
c = Node("c",[])

a.add_edges(b,1)
b.add_edges(c,1)

graph = Graph([a,b,c])
        

graph.find_all_paths("a","c")