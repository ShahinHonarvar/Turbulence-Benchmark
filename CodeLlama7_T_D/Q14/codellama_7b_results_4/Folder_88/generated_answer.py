
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize the second smallest element to None
    second_smallest = None

    # Iterate through the list starting from index 6
    for i in range(5, len(my_list)):
        # If the current element is smaller than the second smallest element or if the second smallest element is None, update the second smallest element
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
