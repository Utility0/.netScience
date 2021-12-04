###
# Packages
###

import networkx as nx
import matplotlib.pyplot as plt
import community
import numpy as np

###
# Load Twitter 2097571
###

g = nx.read_edgelist("twitter/2097571.edges",create_using=nx.Graph(), nodetype = int)
nx.draw(g, node_size=100)
print(f"Number of nodes: {len(g.nodes)} edges: {len(g.edges)}")

###
# Compute Values
###

degree = nx.degree_centrality(g)
betweenness = nx.betweenness_centrality(g)
closeness = nx.closeness_centrality(g)
katz = nx.katz_centrality_numpy(g)

###
#Louvain Community detection
###

#first compute the best partition
partition = community.best_partition(g)
#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(g)
count = 0
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(g, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))
nx.draw_networkx_edges(g, pos, alpha=0.5)
plt.savefig('louvain.png')