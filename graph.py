import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

edges = [
    ("s", "A", "+1"),
    ("A", "s", "-1"),
    ("s", "B", "-1"),
    ("B", "s", "+1"),
    ("A", "B", "+1"),
    ("B", "A", "-1"),
    ("A", "t", "+1"),
    ("t", "A", "-1"),
    ("B", "t", "+1"),
    ("t", "B", "-1"),
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

pos = {
    "s": (0, 1),
    "A": (2, 1),
    "B": (0, 0),
    "t": (2, 0),
}

plt.figure(figsize=(7, 5))

nx.draw_networkx_nodes(G, pos, node_size=1800)
nx.draw_networkx_labels(G, pos, font_size=14, font_weight="bold")

nx.draw_networkx_edges(

    G,
    pos,
    arrows=True,
    arrowstyle="->",
    arrowsize=20,
    connectionstyle="arc3,rad=0.15",
)

edge_labels = nx.get_edge_attributes(G, "weight")


nx.draw_networkx_edge_labels(

    G,
    pos,
    edge_labels=edge_labels,
    font_size=11,
    label_pos=0.35,
)


plt.title("Directed graph with edge weights")
plt.axis("off")
plt.tight_layout()
plt.savefig("dijkstra_graph.png", dpi=300)
plt.show()