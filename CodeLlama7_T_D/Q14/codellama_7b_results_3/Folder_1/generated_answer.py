
def find_second_smallest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Initialize variables to keep track of the second smallest element and its index
    second_smallest = None
    second_smallest_index = None

    # Iterate over the list starting from index 34
    for i in range(34, len(my_list)):
        # If the current element is smaller than the second smallest element, update the second smallest element and its index
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
            second_smallest_index = i

    # Return the second smallest element from index 34 to index 55, both inclusive
    return second_smallest
