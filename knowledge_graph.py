import networkx as nx
import matplotlib.pyplot as plt


# Create a knowledge graph
G = nx.Graph()


# -----------------------------
# Add router nodes
# -----------------------------

G.add_node("R1", type="Router")
G.add_node("R2", type="Router")
G.add_node("R3", type="Router")
G.add_node("R4", type="Router")


# -----------------------------
# Add traffic condition nodes
# -----------------------------

G.add_node("Traffic", type="Traffic")
G.add_node("Delay", type="Performance")
G.add_node("Packet Loss", type="Performance")
G.add_node("Jitter", type="Performance")


# -----------------------------
# Add router links
# -----------------------------

G.add_edge("R1", "R2", relation="connected")
G.add_edge("R2", "R3", relation="connected")
G.add_edge("R3", "R4", relation="connected")
G.add_edge("R4", "R1", relation="connected")


# -----------------------------
# Add performance dependencies
# -----------------------------

G.add_edge("Traffic", "Delay", relation="increases")
G.add_edge("Traffic", "Packet Loss", relation="affects")
G.add_edge("Traffic", "Jitter", relation="affects")


# Traffic affects routers
G.add_edge("Traffic", "R1", relation="affects")
G.add_edge("Traffic", "R2", relation="affects")
G.add_edge("Traffic", "R3", relation="affects")
G.add_edge("Traffic", "R4", relation="affects")


# -----------------------------
# Display the graph
# -----------------------------

position = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    position,
    with_labels=True,
    node_size=1800,
    font_size=9
)

plt.title("Network Knowledge Graph")
plt.show()