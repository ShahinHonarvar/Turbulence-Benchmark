
def find_second_smallest_num(my_list):
    smallest = None
    second_smallest = None
    for i in range(27, 56):
        num = my_list[i]
        if smallest is None:
            smallest = num
        elif second_smallest is None and num != smallest:
            second_smallest = num
    return second_smallest
