
def find_second_smallest_num(my_list):
    # Check if the input list is valid
    if not my_list or len(my_list) < 2:
        return None

    # Find the second smallest element in the list
    second_smallest = None
    for i in range(52, 71 + 1):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
