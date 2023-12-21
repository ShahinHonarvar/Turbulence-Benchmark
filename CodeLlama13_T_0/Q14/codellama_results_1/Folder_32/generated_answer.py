
def find_second_smallest_num(my_list):
    if len(my_list) < 35:
        return None
    second_smallest = my_list[32]
    for i in range(33, 36):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
