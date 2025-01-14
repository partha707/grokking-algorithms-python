# Selection Sort Algorithm Implementation in Python

def find_smallest(arr):
    """
    Finds the index of the smallest element in a list.

    Args:
        arr (list): The list to search for the smallest element.

    Returns:
        int: The index of the smallest element.
    """
    smallest = arr[0]  # Assume the first element is the smallest
    smallest_index = 0

    # Iterate through the list to find the actual smallest element
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: A new list that is sorted in ascending order.
    """
    sorted_arr = []  # List to hold the sorted elements
    copied_arr = list(arr)  # Copy the original array to avoid mutating it

    # Repeat the process until all elements are sorted
    while copied_arr:
        # Find the index of the smallest element in the unsorted part
        smallest_index = find_smallest(copied_arr)

        # Remove the smallest element from the unsorted list and add it to the sorted list
        sorted_arr.append(copied_arr.pop(smallest_index))

    return sorted_arr


# Test the Selection Sort function
my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 23, 67, 97, 33, 244, 55, 44, 44]

print("Original list:", my_list)
print("Sorted list:", selection_sort(my_list))
