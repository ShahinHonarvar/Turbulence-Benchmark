
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the second smallest element in the list
    second_smallest = None
    for i in range(22, 64):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element, or 'None' if it does not exist
    return second_smallest
