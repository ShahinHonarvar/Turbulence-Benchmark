
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    list_len = len(my_list)

    # Check if the list is empty
    if list_len == 0:
        return None

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[37]
    second_smallest = None

    # Iterate through the list from index 37 to index 51, both inclusive
    for i in range(37, 52):
        # If the current element is smaller than the smallest element, update the smallest and second smallest elements
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

        # If the current element is smaller than the second smallest element, update the second smallest element
        elif my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element from index 37 to index 51, both inclusive
    return second_smallest
