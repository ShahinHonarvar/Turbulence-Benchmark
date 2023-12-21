
def find_second_smallest_num(my_list):
    # Find the smallest element
    smallest = None
    for i in range(22, 88 + 1):
        if my_list[i] < smallest or smallest is None:
            smallest = my_list[i]
    # Find the second smallest element
    second_smallest = None
    for i in range(22, 88 + 1):
        if my_list[i] == smallest and second_smallest is None:
            second_smallest = my_list[i]
        elif my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]
    return second_smallest
