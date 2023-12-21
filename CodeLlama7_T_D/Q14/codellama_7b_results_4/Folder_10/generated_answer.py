
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the smallest element
    smallest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]

    # Find the second smallest element
    second_smallest = None

    for i in range(len(my_list)):
        if my_list[i] == smallest:
            continue

        elif second_smallest is None or my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
