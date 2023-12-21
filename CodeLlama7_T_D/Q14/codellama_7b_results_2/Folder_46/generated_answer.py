
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Initialize variables for keeping track of the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = None

    # Iterate through the list starting from index 13 to index 68, both inclusive
    for i in range(13, 69):
        # If the current element is smaller than the smallest element, update the smallest element and its index
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

        # If the current element is smaller than the second smallest element (if it exists), update the second smallest element and its index
        elif second_smallest is not None and my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element from index 13 to index 68, both inclusive
    return second_smallest
