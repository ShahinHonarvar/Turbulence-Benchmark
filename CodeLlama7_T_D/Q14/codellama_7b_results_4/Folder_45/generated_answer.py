
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    len = len(my_list)

    # Check if the list has at least 2 elements
    if len < 2:
        return None

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = my_list[1]

    # Iterate through the list starting from index 30
    for i in range(30, len):
        # If the current element is smaller than the smallest element, update the smallest and second smallest elements
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

        # If the current element is smaller than the second smallest element, update the second smallest element
        elif my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element from index 30 to index 200, both inclusive
    return second_smallest
