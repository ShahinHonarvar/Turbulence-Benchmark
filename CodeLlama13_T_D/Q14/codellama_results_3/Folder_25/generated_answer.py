
def find_second_smallest_num(my_list):
    second_smallest = None
    for i in range(37, 76 + 1):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
