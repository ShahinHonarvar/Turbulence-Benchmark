
def find_second_smallest_num(my_list):
    if len(my_list) < 8:
        return None
    second_smallest = my_list[4]
    for i in range(5, 9):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
