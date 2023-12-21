
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables for second smallest element and its index
    second_smallest = None
    second_smallest_index = -1

    # Iterate over the list starting from index 22 to index 88
    for i in range(22, 90):
        # If the current element is smaller than the second smallest element, update the second smallest element and its index
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
            second_smallest_index = i

    # Return the second smallest element from index 22 to index 88, both inclusive
    return second_smallest
