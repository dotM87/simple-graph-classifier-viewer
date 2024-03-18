import tkinter as tk
from graph import Graph
from graph_visualization import visualize_graph

def start_app():
    # Create an empty graph
    graph = Graph()

    def add_node():
        value = entry_value.get()
        if value:
            graph.add_node(value)
            entry_value.delete(0, tk.END)

    def add_edge():
        value1 = entry_edge1.get()
        value2 = entry_edge2.get()
        if value1 and value2:
            graph.add_edge(value1, value2)
            entry_edge1.delete(0, tk.END)
            entry_edge2.delete(0, tk.END)

    def display_graph():
        graph.display()
        visualize_graph(graph)
    
    def new_graph():
        graph.clear()

    # GUI setup
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Simple Graph Classifier & Visualizer")

    label_value = tk.Label(root, text="Node Value:")
    entry_value = tk.Entry(root)
    btn_add_node = tk.Button(root, text="Add Node", command=add_node)

    label_edge1 = tk.Label(root, text="Edge Node 1:")
    entry_edge1 = tk.Entry(root)
    label_edge2 = tk.Label(root, text="Edge Node 2:")
    entry_edge2 = tk.Entry(root)
    btn_add_edge = tk.Button(root, text="Add Edge", command=add_edge)

    btn_display_graph = tk.Button(root, text="Display Graph", command=display_graph)
    btn_clear_display = tk.Button(root, text="New", command=new_graph)

    label_value.pack()
    entry_value.pack()
    btn_add_node.pack()

    label_edge1.pack()
    entry_edge1.pack()
    label_edge2.pack()
    entry_edge2.pack()
    btn_add_edge.pack()

    btn_display_graph.pack()
    btn_clear_display.pack()

    root.mainloop()
