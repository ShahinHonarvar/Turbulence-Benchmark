 def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the input list has at least two elements

    if len(my_list) < 2:
        return None

    # Find the second smallest element in the list

    second_smallest = None

    for i in range(661, 925):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element

    return second_smallest
