
def find_second_largest_num(my_list):
    # Check if list is empty or has fewer than two elements
    if len(my_list) < 2:
        return None

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate over the list, starting from index 4 (inclusive) to index 8 (inclusive)
    for i in range(4, 9):
        # If the current element is larger than the second largest element, update the second largest element and its index
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element from index 4 to index 8 (inclusive)
    return second_largest
