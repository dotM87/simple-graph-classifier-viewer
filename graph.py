class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent_nodes = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, value1, value2):
        if value1 in self.nodes and value2 in self.nodes:
            node1 = self.nodes[value1]
            node2 = self.nodes[value2]
            if node2 not in node1.adjacent_nodes:
                node1.adjacent_nodes.append(node2)
                node2.adjacent_nodes.append(node1)

    def get_adjacent_nodes(self, value):
        if value in self.nodes:
            return self.nodes[value].adjacent_nodes

    def display(self):
        for node_value, node in self.nodes.items():
            adjacent_values = [adj_node.value for adj_node in node.adjacent_nodes]
            print(f"{node_value}: {', '.join(map(str, adjacent_values))}")
    def clear(self):
        self.nodes = {}