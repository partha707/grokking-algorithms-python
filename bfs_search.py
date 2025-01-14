from collections import deque

# Breadth-First Search (BFS) to find a mango seller in a social network graph.

# Define the graph as an adjacency list.
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def person_is_seller(name):
    """
    Check if a person is a mango seller.

    A mango seller is identified by their name ending with the letter 'm'.

    Args:
        name (str): The name of the person to check.

    Returns:
        bool: True if the person is a mango seller, False otherwise.
    """
    return name[-1] == "m"

def search(name):
    """
    Perform a breadth-first search to find a mango seller in the network.

    The function starts from the given person and explores their connections
    to find someone whose name ends with 'm', indicating they are a mango seller.

    Args:
        name (str): The starting point for the search.

    Returns:
        bool: True if a mango seller is found, False otherwise.
    """
    # Create a queue to manage the search.
    search_queue = deque()
    # Add the connections of the starting person to the queue.
    search_queue += graph[name]
    # Keep track of already searched people to avoid duplicates.
    searched = set()

    while search_queue:
        # Get the next person from the queue.
        person = search_queue.popleft()
        # Check if this person has already been searched.
        if person not in searched:
            # If the person is a mango seller, print the result and return True.
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                # If not, add their connections to the queue for further exploration.
                search_queue += graph[person]
                # Mark the person as searched.
                searched.add(person)

    # If no mango seller is found, print the message and return False.
    print("No mango seller found in network!")
    return False

# Start the search from "you".
search("you")
