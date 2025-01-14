# Quick Sort Algorithm Implementation in Python

def quick_sort(arr):
    """
    Recursively sorts an array using the Quick Sort algorithm.

    Args:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: A new list that is sorted in ascending order.
    """
    # Base case: If the array has 0 or 1 elements, it is already sorted.
    if len(arr) < 2:
        return arr

    # Choose the pivot element (first element of the array).
    pivot = arr[0]

    # Partition the array into two sublists:
    # 'less' contains elements less than the pivot.
    less = [i for i in arr[1:] if i <= pivot]

    # 'greater' contains elements greater than the pivot.
    greater = [i for i in arr[1:] if i > pivot]

    # Recursively sort the 'less' and 'greater' sublists and combine them with the pivot.
    return quick_sort(less) + [pivot] + quick_sort(greater)


# Test the Quick Sort function with a sample list.
my_list = [4, 894, 9965, 22, 45959, 67543, 32, 4, 6, 7, 7, 234, 5, 5, 5, 5, 9, 9, 9]

# Print the sorted list.
print("Original list:", my_list)
print("Sorted list:", quick_sort(my_list))
