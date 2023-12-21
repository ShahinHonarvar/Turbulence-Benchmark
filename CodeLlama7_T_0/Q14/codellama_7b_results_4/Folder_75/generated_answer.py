
def find_second_smallest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize a variable to keep track of the second smallest element
    second_smallest = None

    # Iterate through the list and find the second smallest element
    for i in range(12, 92 + 1):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
