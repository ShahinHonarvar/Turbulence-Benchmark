
def find_second_smallest_num(my_list):
    if len(my_list) < 48:
        return None
    second_smallest = my_list[30]
    for i in range(31, 49):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
