
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the list has at least 25 elements
    if len(my_list) < 25:
        return None

    # Find the second smallest element in the range [25, 59]
    second_smallest = None
    for i in range(25, 60):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
