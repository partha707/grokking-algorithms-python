import math

# Dijkstra's Algorithm to find the shortest path in a weighted graph.

# STEP 1: Create the graph as a dictionary (hash table).
# Each node points to its neighboring nodes and the respective weights of the edges.
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}  # The finish node has no neighbors.
}

# STEP 2: Create a dictionary to track the cost of reaching each node from the start.
# Initially, set the cost of the finish node to infinity (unreachable).
costs = {
    "a": 6,
    "b": 2,
    "fin": math.inf
}

# STEP 3: Create a dictionary to track the parents of each node for path reconstruction.
# This helps us trace the shortest path from the start to the finish.
parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

# STEP 4: Create a set to keep track of processed nodes.
# Once a node has been processed, we won't process it again.
processed = set()


# Function to find the node with the lowest cost that hasn't been processed.
def find_lowest_cost_node(costs):
    """
    Find the node with the lowest cost that hasn't been processed yet.

    Args:
        costs (dict): A dictionary of nodes and their current costs.

    Returns:
        str: The name of the node with the lowest cost, or None if no unprocessed nodes remain.
    """
    lowest_cost = math.inf  # Initialize the lowest cost as infinity.
    lowest_cost_node = None  # Initialize the lowest cost node as None.

    # Iterate through all nodes in the costs dictionary.
    for node in costs:
        cost = costs[node]
        # Check if this node has the lowest cost and hasn't been processed yet.
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


# STEP 5: Dijkstra's main loop.
# Find the shortest path by repeatedly processing the lowest-cost node.
node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    # Iterate through all the neighbors of the current node.
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]  # Calculate the new cost to reach the neighbor.

        # If the new cost is lower than the current cost, update the cost and parent.
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    # Mark the current node as processed.
    processed.add(node)

    # Find the next node to process.
    node = find_lowest_cost_node(costs)


# Print the final costs and parent nodes after running Dijkstra's algorithm.
print("Final costs:", costs)
print("Final parents:", parents)


# Function to reconstruct and print the shortest path from start to finish.
def print_path(parents):
    """
    Reconstruct and print the shortest path from the start node to the finish node.

    Args:
        parents (dict): A dictionary of nodes and their parents in the shortest path tree.
    """
    path = []
    node = "fin"  # Start from the finish node.

    # Work backwards from the finish node to the start node using the parents dictionary.
    while node != "start":
        path.append(node)
        node = parents.get(node)

    path.append("start")  # Add the start node at the end.
    path.reverse()  # Reverse the path to show it from start to finish.

    # Print the reconstructed path.
    print("Path from start to fin:", " -> ".join(path))


# Call the function to print the shortest path.
print_path(parents)
