###
# Packages
###

import networkx as nx
import matplotlib.pyplot as plt
import community
import numpy as np


###
# First Model
###

edges = [
    (0, 6), 
    (1, 6),
    (2, 6),
    (3, 6),
    (4, 6),
    (5, 6),
    (4, 7),
    (7, 8),
    (8, 9),
    (7, 10),
    (10, 11),
    (10, 12),
    (10, 13),
    (10, 14),
]
vertices = [i for i in range(15)]

G=nx.Graph()
G.add_edges_from(edges)
nx.draw(G,with_labels=True)
plt.savefig('smallNetwork.png')
plt.close()

###
# Compute Values
###

degree = nx.degree_centrality(G)
print("Degree")
print("-"*20)
list(map(lambda x:print(str(x)+' : '+str(degree[x])),degree))
print("-"*20)
betweenness = nx.betweenness_centrality(G)
print("Betweenness")
print("-"*20)
list(map(lambda x:print(str(x)+' : '+str(betweenness[x])),betweenness))
print("-"*20)
closeness = nx.closeness_centrality(G)
print("Closeness")
print("-"*20)
list(map(lambda x:print(str(x)+' : '+str(closeness[x])),closeness))
print("-"*20)
katz = nx.katz_centrality_numpy(G)
print("Katz")
print("-"*20)
list(map(lambda x:print(str(x)+' : '+str(katz[x])),katz))
print("-"*20)


###
# Load Twitter 2097571
###

g = nx.read_edgelist("twitter/2097571.edges",create_using=nx.Graph(), nodetype = int)
nx.draw(g, node_size=100)
print("Number of nodes: "+str(len(g.nodes))+" edges: "+str(len(g.edges)))

def delete_unconnected_nodes(G):
    nodes_to_delete = []
    for node in G.nodes:
        if not G.neighbors(node):
            nodes_to_delete.append(node)
    G.remove_nodes_from(nodes_to_delete)
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    G = G.subgraph(Gcc[0])
    return G

g = delete_unconnected_nodes(g)

nx.draw(g)
plt.savefig('twitterPlot.png')
plt.close()

###
#Louvain Community detection
###


partition = community.best_partition(g)
size = float(len(set(partition.values())))
pos = nx.spring_layout(g)
count = 0
for com in set(partition.values()) :
    count = count + 1
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(g, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))
nx.draw_networkx_edges(g, pos, alpha=0.5)
plt.savefig('louvain.png')
plt.close()