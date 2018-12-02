# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:33:50 2018

@author: Leila
"""

#%%

#In a graphs module, implement a directed graph data
#structure using classes. Modify the find_path function for so it works
#on instances of your class.

class Node:
    
    def __init__(self,name,edge):
        self.name = name
        self.edge = edge
        
        
class Graph:
    
    def __init__(self,nodeslist):
        self.nodeslist = nodeslist
        
    def return_edges(self,name):
        
        edges = []
        
        for node in self.nodeslist:
            if node.name == name:
                edges += node.edge
        
        return node.edge
        
    def return_node(self,name):
        
        nodes = []
        
        for node in self.nodeslist:
            if node.name == name:
                nodes += node.name
    
        return nodes
        
    def find_path(self,start, end, path=[]):
        
        path = path + self.return_node(start)
    
            
        if self.return_node(start) == self.return_node(end):          
            return path
        
        for conn in self.return_edges(start): 
        # this is to avoid getting stuck in cycles and going back to start            
#            if conn not in path:
            
            new_path = self.find_path(conn, end, path)
              
            if new_path is not None:
                return new_path
                
        return None

        
a = Node("a",["b"])
b = Node("b",["c"])
c = Node("c",[])

graph = Graph([a,b,c])
        

graph.find_path("a","c")