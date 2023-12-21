
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the second smallest element
    second_smallest = None
    second_index = -1

    # Iterate through the list and find the second smallest element
    for i in range(len(my_list)):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]
            second_index = i

    # Return the second smallest element, if it exists
    if second_index >= 8 and second_index <= 9:
        return second_smallest

    # Otherwise, return None
    else:
        return None
