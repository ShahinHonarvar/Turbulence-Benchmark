
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    second_smallest = sorted_list[15]
    for i in range(16,39):
        if my_list[i] == second_smallest:
            continue
        elif my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
