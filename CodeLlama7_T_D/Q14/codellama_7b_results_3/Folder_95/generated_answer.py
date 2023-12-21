
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = None

    # Iterate through the list starting from index 75 and ending at index 85
    for i in range(75, 86):
        # If the current element is smaller than the smallest element, update the smallest and second smallest elements accordingly
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

        # If the current element is smaller than the smallest element but larger than the second smallest element, update the second smallest element accordingly
        elif my_list[i] < second_smallest and second_smallest is not None:
            second_smallest = my_list[i]

    # Return the second smallest element if it exists, otherwise return 'None'
    if second_smallest is not None:
        return second_smallest

    else:

        return None
