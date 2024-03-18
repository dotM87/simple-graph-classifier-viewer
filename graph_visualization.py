import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.Graph()
    for node_value, node in graph.nodes.items():
        G.add_node(node_value)
        for adj_node in node.adjacent_nodes:
            G.add_edge(node_value, adj_node.value)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    plt.show()
