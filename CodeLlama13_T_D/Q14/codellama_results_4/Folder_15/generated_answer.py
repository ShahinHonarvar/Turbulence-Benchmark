
def find_second_smallest_num(my_list):
    if len(my_list) < 4:
        return None
    sorted_list = sorted(my_list)
    second_smallest = sorted_list[3]
    for i in range(1, 4):
        if my_list[i] == second_smallest:
            return None
    return second_smallest
