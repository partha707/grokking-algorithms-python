from os import listdir
from os.path import isfile, join
from collections import deque

# Directory Traversal Using Breadth-First Search (BFS)
def print_file_names_bfs(start_dir):
    """
    Prints file names in a directory using Breadth-First Search (BFS).

    Args:
        start_dir (str): The path of the starting directory.
    """
    search_queue = deque()  # Queue for BFS
    search_queue.append(start_dir)

    while search_queue:
        current_dir = search_queue.popleft()

        try:
            # Iterate through the sorted list of items in the directory
            for item in sorted(listdir(current_dir)):
                full_path = join(current_dir, item)

                # If it's a file, print the file name
                if isfile(full_path):
                    print(f"File: {full_path}")
                else:
                    # If it's a directory, add it to the search queue
                    search_queue.append(full_path)
        except PermissionError:
            print(f"Permission denied: {current_dir}")
        except FileNotFoundError:
            print(f"Directory not found: {current_dir}")


# Directory Traversal Using Depth-First Search (DFS)
def print_file_names_dfs(start_dir):
    """
    Prints file names in a directory using Depth-First Search (DFS).

    Args:
        start_dir (str): The path of the starting directory.
    """
    try:
        # Iterate through the sorted list of items in the directory
        for item in sorted(listdir(start_dir)):
            full_path = join(start_dir, item)

            # If it's a file, print the file name
            if isfile(full_path):
                print(f"File: {full_path}")
            else:
                # If it's a directory, recursively call the function
                print_file_names_dfs(full_path)
    except PermissionError:
        print(f"Permission denied: {start_dir}")
    except FileNotFoundError:
        print(f"Directory not found: {start_dir}")


# Test the BFS function
print("\n BFS Directory Traversal:")
print_file_names_bfs("your_directory_path_here")

# Test the DFS function
print("\n DFS Directory Traversal:")
print_file_names_dfs("your_directory_path_here")
