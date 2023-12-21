
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the second smallest element and its index
    second_smallest = None
    second_smallest_index = None

    # Iterate through the list, starting from index 75, until we reach index 94
    for i in range(75, 95):
        # If the current element is smaller than the second smallest element, update the variables accordingly
        if second_smallest is None or my_list[i] < second_smallest:
            second_smallest = my_list[i]
            second_smallest_index = i

    # If there was no second smallest element in the list, return 'None'
    if second_smallest_index is None:
        return None

    # Return the second smallest element from index 75 to index 94, both inclusive
    return my_list[second_smallest_index]
