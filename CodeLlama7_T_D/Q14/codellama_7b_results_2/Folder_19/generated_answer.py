
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = None
    second_smallest = None

    # Iterate through the list starting from index 4 to index 8, both inclusive
    for i in range(4, 9):
        # If the current element is smaller than the smallest element, update the smallest and second smallest elements accordingly
        if smallest is None or my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

        # If the current element is between the second smallest and smallest elements, update the second smallest element accordingly
        elif second_smallest is None or second_smallest < my_list[i] < smallest:
            second_smallest = my_list[i]

    # Return the second smallest element if it exists, otherwise return 'None'
    return second_smallest if second_smallest is not None else None
