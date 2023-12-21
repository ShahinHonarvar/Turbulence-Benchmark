
def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = None
    for i in range(21, 98):
        if my_list[i] < smallest or smallest is None:
            smallest = my_list[i]
    # Find the second smallest element in the list
    second_smallest = None
    for i in range(21, 98):
        if my_list[i] == smallest and second_smallest is None:
            second_smallest = smallest
        elif my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]
    return second_smallest
