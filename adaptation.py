import networkx as nx


# Create the network
G = nx.Graph()


# Add network links
G.add_edge("R1", "R2")
G.add_edge("R2", "R3")
G.add_edge("R3", "R4")
G.add_edge("R4", "R1")


# Current route
current_route = ["R1", "R2", "R3"]

print("Current route:", current_route)


# The overloaded link
overloaded_link = ("R2", "R3")

print("Overloaded link:", overloaded_link)


# Remove the overloaded link temporarily
G.remove_edge(overloaded_link[0], overloaded_link[1])


# Find an alternative shortest path
alternative_route = nx.shortest_path(
    G,
    source="R1",
    target="R3"
)


# Display the new route
print("Alternative route:", alternative_route)