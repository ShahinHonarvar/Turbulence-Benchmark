
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    list_len = len(my_list)

    # Check if the list is empty
    if list_len == 0:
        return None

    # Initialize variables for the smallest and second smallest elements
    smallest_element = my_list[75]
    second_smallest_element = None

    # Iterate over the elements in the specified range
    for i in range(75, 89):
        # Check if the current element is smaller than the smallest element
        if my_list[i] < smallest_element:
            # If it is, update the second smallest element and continue
            second_smallest_element = smallest_element
            smallest_element = my_list[i]

    # Check if a second smallest element was found
    if second_smallest_element is not None:
        # Return the second smallest element
        return second_smallest_element

    # If no second smallest element was found, return None
    return None
