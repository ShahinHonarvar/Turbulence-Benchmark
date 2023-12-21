
def find_second_smallest_num(my_list):
    # Check if list is empty or has less than two elements
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = None

    # Iterate over the elements starting from index 64
    for i in range(64, len(my_list)):
        # If the current element is smaller than the smallest element found so far
        if my_list[i] < smallest:
            # Update the second smallest element with the previous smallest element
            second_smallest = smallest

            # Update the smallest element with the current element
            smallest = my_list[i]

    # If a second smallest element was found, return it
    if second_smallest is not None:
        return second_smallest

    # Otherwise, return 'None'
    else:
        return None
