def binary_search(arr, item):
    """
    Perform a binary search to find the position of a given item in a sorted array.

    Binary search works by repeatedly dividing the search space in half. It requires
    the array to be sorted.

    Args:
        arr (list): A sorted list of elements to search.
        item (int): The item to find in the array.

    Returns:
        int: The index of the item if found, otherwise None.
    """
    low = 0                # The starting index of the search space.
    high = len(arr) - 1    # The ending index of the search space.
    step = 1               # To track the number of steps taken.

    while low <= high:
        mid = (low + high) // 2    # Calculate the midpoint of the current search space.
        guess = arr[mid]           # Get the element at the midpoint.

        # Check if the guessed element is the one we're looking for.
        if guess == item:
            return mid

        # If the guess is too high, adjust the high boundary.
        elif guess > item:
            high = mid - 1

        # If the guess is too low, adjust the low boundary.
        else:
            low = mid + 1

        # Print the current step for debugging purposes.
        print(f"--- now step is {step} ---")
        step += 1

    # Return None if the item was not found.
    return None


# Create a list of numbers from 0 to 127.
my_list = [i for i in range(128)]

# Print the list (for debugging purposes).
print(my_list)

# Search for the number 9 in the list and print the result.
print(binary_search(my_list, 9))
