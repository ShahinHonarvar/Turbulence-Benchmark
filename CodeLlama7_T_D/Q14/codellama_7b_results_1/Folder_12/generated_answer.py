
def find_second_smallest_num(my_list):
    # Check if there are at least two elements in the list
    if len(my_list) < 2:
        return None

    # Find the second smallest element
    second_smallest = None
    for i in range(31, 73):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
