
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Get the length of the list
    n = len(my_list)
    # Check if the index is within the range of the list
    if 23 < n:
        raise ValueError("Index must be less than the length of the list")
    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = None
    # Iterate through the list from index 23 to index 23, both inclusive
    for i in range(23, n):
        # If the current element is larger than the current second largest element
        if my_list[i] > second_largest:
            # Update the second largest element and its index
            second_largest = my_list[i]
            second_largest_index = i
    # Return the second largest element from index 23 to index 23, both inclusive
    return second_largest
