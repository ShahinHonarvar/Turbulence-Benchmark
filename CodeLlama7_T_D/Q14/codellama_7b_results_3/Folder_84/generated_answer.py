
def find_second_smallest_num(my_list):
    # Check if the input list has at least 41 elements
    if len(my_list) < 41:
        return None

    # Find the smallest element in the range [40, 80]
    smallest = my_list[40]
    for i in range(41, 81):
        if my_list[i] < smallest:
            smallest = my_list[i]

    # Find the second smallest element

    second_smallest = None

    for i in range(40, 80):
        if my_list[i] > smallest and (second_smallest is None or my_list[i] < second_smallest)):
            second_smallest = my_list[i]

    # Return the second smallest element

    return second_smallest
