
def find_second_smallest_num(my_list):
    # Check if there are at least two elements in the list
    if len(my_list) < 2:
        return None

    # Find the smallest element and its index

    smallest = my_list[0]
    smallest_index = 0

    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
            smallest_index = i

    # Find the second smallest element and its index

    second_smallest = None
    second_smallest_index = None

    for i in range(68, 87):
        if my_list[i] == smallest:
            continue

        if second_smallest is None or my_list[i] < second_smallest:
            second_smallest = my_list[i]
            second_smallest_index = i

    # Return the second smallest element

    return second_smallest
