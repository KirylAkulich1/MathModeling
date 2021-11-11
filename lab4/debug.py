import networkx as nx
from networkx.classes.function import nodes
import numpy as np 
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

def do_iterate(D_output,D,state_0):
    def node_exist(g,state):
        nodes = g.nodes
        for node in nodes:
            if node == state:
                return True
        return False
    def check_if_infinite(g,state,infinite_set):
        nodes = g.nodes
        for node in nodes:
            if nx.has_path(g,node,state):
                for v1,v2 in zip(node,state):
                    if v2 < v1:
                        break
                    infinite_set.add(node)
            
    states_to_check = list()
    state = state_0
    state_graph = nx.DiGraph()
    states_to_check.append(state)
    inifite_set = set()
    while len(states_to_check) !=0:
        check_option = states_to_check.pop()
        for i,row in enumerate(D_output):
            if np.all(check_option >= row):
                new_state = state +  D[i]
                if node_exist(state_graph,new_state):
                    if not state_graph.has_edge(new_state,state):
                        state_graph.add_edge(state,new_state)
                check_if_infinite(state_graph,new_state,inifite_set)
    return state_graph,inifite_set

                    


D_input = np.array([
    [1,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,1,0,0,0],
    [0,0,0,1,1,1]])
D_output = np.array([
    [0,1,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,1,0],
    [1,0,0,0,0,0]])
mu_0 = {}
