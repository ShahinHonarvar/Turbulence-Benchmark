
def find_second_smallest_num(my_list):
    # Check if the list has enough elements
    if len(my_list) - 1 < 37 or len(my_list) - 1 > 76:
        return None

    # Initialize variables for keeping track of the smallest and second smallest elements
    smallest = my_list[37]
    second_smallest = None

    # Iterate through the list from index 37 to 76, inclusive
    for i in range(37, 77):
        # Check if the current element is smaller than the current smallest element
        if my_list[i] < smallest:
            # If it is, update the second smallest element and continue iterating
            second_smallest = smallest
            smallest = my_list[i]

        # Check if the current element is smaller than the current second smallest element
        elif my_list[i] < second_smallest:
            # If it is, update the second smallest element and continue iterating
            second_smallest = my_list[i]

    # Return the second smallest element found in the list from index 37 to 76, inclusive
    return second_smallest
