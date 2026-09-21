import networkx as nx
import matplotlib.pyplot as plt


# Create an empty network
G = nx.Graph()


# Add routers
G.add_node("R1")
G.add_node("R2")
G.add_node("R3")
G.add_node("R4")


# Add links between routers
G.add_edge("R1", "R2")
G.add_edge("R2", "R3")
G.add_edge("R1", "R4")
G.add_edge("R4", "R3")


# Give positions to the routers
position = {
    "R1": (0, 1),
    "R2": (2, 1),
    "R3": (2, 0),
    "R4": (0, 0)
}


# Draw the network
nx.draw(
    G,
    position,
    with_labels=True,
    node_size=2000,
    node_color="lightblue",
    font_size=12
)


# Show the network
plt.title("Basic Network Topology")
plt.show()