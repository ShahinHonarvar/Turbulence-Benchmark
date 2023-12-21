
def find_second_smallest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize a variable to store the second smallest element
    second_smallest = None

    # Iterate through the list starting from index 62
    for i in range(62, len(my_list)):
        # Check if the current element is smaller than the second smallest element found so far
        if second_smallest is not None and my_list[i] < second_smallest:
            # If it is smaller, update the second smallest element
            second_smallest = my_list[i]

    # Return the second smallest element found
    return second_smallest
