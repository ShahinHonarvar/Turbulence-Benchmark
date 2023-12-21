
def find_second_smallest_num(my_list):
    if len(my_list) < 64:
        return None
    second_smallest = my_list[64]
    for i in range(65, len(my_list)):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
