
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[17]
    second_smallest = my_list[18]

    # Loop through the list from index 17 to index 78, inclusive
    for i in range(17, 79):
        # If the current element is smaller than the smallest element, update the smallest and second smallest elements accordingly
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

        # If the current element is smaller than the second smallest element, update the second smallest element accordingly
        elif my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element from index 17 to index 78, both inclusive
    return second_smallest
