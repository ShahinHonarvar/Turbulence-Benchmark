
def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = None
    for i in range(len(my_list)):
        if smallest is None or my_list[i] < smallest:
            smallest = my_list[i]
    # Find the second smallest element in the list
    second_smallest = None
    for i in range(len(my_list)):
        if my_list[i] > smallest and (second_smallest is None or my_list[i] < second_smallest):
            second_smallest = my_list[i]
    return second_smallest
