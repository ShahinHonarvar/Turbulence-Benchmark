
def find_second_smallest_num(my_list):
    if len(my_list) < 86:
        return None
    second_smallest = my_list[82]
    for i in range(83, 87):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
