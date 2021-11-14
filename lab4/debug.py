import networkx as nx
from networkx.classes.function import nodes
import numpy as np 
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

def do_iterate(D_input,D,state_0):
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
                    if v2 <= v1 or v1 ==0:
                        break
                    infinite_set.add(node)

    states_to_check = list()
    node_labels = dict()
    state = state_0
    state_graph = nx.DiGraph()
    state_graph.add_node(state_0)
    labels_count = 0
    node_labels[state] = f'M{labels_count}:{state}'
    states_to_check.append(state)
    inifite_set = set()
    while len(states_to_check) !=0:
        state = states_to_check.pop(0)
        vertex_to_add = []
        for i,row in enumerate(D_input):
            answer = state >= row
            if np.all(state >= row):
                new_state = tuple(state +  D[i])
                if node_exist(state_graph,tuple(new_state)):
                    if not state_graph.has_edge(new_state,state):
                        state_graph.add_edge(tuple(state),tuple(new_state),t =f"t{i+1}")
                        vertex_to_add.append(new_state)
                else:
                    labels_count+=1
                    node_labels[new_state] = f'M{labels_count}:{new_state}'
                    state_graph.add_edge(tuple(state),tuple(new_state),t =f"t{i+1}")
                    states_to_check.append(tuple(new_state))
                    vertex_to_add.append(new_state)
                check_if_infinite(state_graph,tuple(new_state),inifite_set)
    G = nx.relabel_nodes(state_graph,node_labels)
    '''G = nx.relabel_nodes(state_graph,node_labels)
    edge_labels = dict([((n1, n2), d['t'])
                    for n1, n2, d in G.edges(data=True)])
    pos = nx.planar_layout(G)
    nx.draw(G,pos , with_labels=True)
    nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)

    plt.show()
    '''
    return state_graph,G,inifite_set

def isLive(G):
    for node in G.nodes:
        if len(list(G.neighbors(node))) == 0:
            return False
    else:
        return True

def Bounded(G,inifinity_nodes):
    if len(inifinity_nodes)!=0:
        return np.inf
    nodes = G.nodes
    return max([max(node) for node in nodes])
def Conservative(G):
    sums = [sum(node) for node in G.nodes]
    return len(set(sums)) == 1

def Reachibility(G,state_0,transisions):

    for node in G.nodes:
        if len(list(G.neighbors(node))) == 0:
            for path in nx.all_simple_edge_paths(G,state_0,node):
                for edge in path:
                    src = edge[0]
                    dst = edge[1]
                    print(str(src)+ " - "+str(dst)+ " :: "+str(G.get_edge_data(edge[0], edge[1])[edge[2]]))

def ParallelTransavtions(G,D_input):
    for node in G.nodes:
        neighbors = G.neighbors(node)

        if len(list(neighbors)) < 2:
            continue
        for i in range(np.shape(D_input)[0]):
            new_state = np.array(node) - D_input[i]    
            if np.any(new_state<0):
                continue        
            for j in range(i+1,np.shape(D_input)[0]):
                if np.all((new_state - D_input[j])>=0):
                    print(f'Параллельное срабатывание вохможно: Из состояния {node} c помощью переходов t{i+1} t{j+1}')
                    return 
    print('Параллельное срабатывание невозможно')

def if_freechoice_net(D_input):
    for i in range(np.shape(D_input)[1]):
        if sum(D_input[:,i]) !=1:
            for j,v in enumerate(D_input[:,i]):
                if v == 0:
                    continue
                if(sum(D_input[j]))!=1:
                    return False

    return True

         
def can_be_reachable(G,source,target):
    return nx.has_path(G,source,target)

def is_marked_graph(D_input,D_output):
    for i in range(np.shape(D_input)[1]):
        if sum(D_input[:,i]) !=1 or sum(D_output[:,i])!=1:
            return False
    return True

D_input = np.array([
    [0,0,0,1,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0]])
D_output = np.array([
    [1,0,0,0,0],
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,0,0,0,1]])
D =   D_output - D_input
mu_0 = (0,0,1,1,0)

g,G,ininity = do_iterate(D_input,D,mu_0)
print("=======1 сеть=======")
print(f"Является живой: {isLive(g)}")
print(f'Является ограниченной. K={Bounded(g,ininity)}')
print(f'Является консервативной: {Conservative(g)}')
print(f'Является сетью свободного выбора: {if_freechoice_net(D_input)}')
ParallelTransavtions(g,D_input)

edge_labels = dict([((n1, n2), d['t'])
                    for n1, n2, d in G.edges(data=True)])
pos = nx.planar_layout(G)
nx.draw(G,pos , with_labels=True)
nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)

plt.show()

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
D =   D_output - D_input
mu_0 = (1,0,0,0,0,1)
g,G,ininity = do_iterate(D_input,D,mu_0)
print("=======2 сеть=======")
print(f"Является живой: {isLive(g)}")
print(f'Является ограниченной. K={Bounded(g,ininity)}')
print(f'Является консервативной: {Conservative(g)}')
ParallelTransavtions(g,D_input)
print(f'является маркерованным графом {is_marked_graph(D_input,D_output)}')

edge_labels = dict([((n1, n2), d['t'])
                    for n1, n2, d in G.edges(data=True)])
pos = nx.planar_layout(G)
nx.draw(G,pos , with_labels=True)
nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)

plt.show()