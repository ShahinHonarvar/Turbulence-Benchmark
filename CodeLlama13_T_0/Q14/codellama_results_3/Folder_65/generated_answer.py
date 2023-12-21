
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    second_smallest = sorted_list[56]
    for i in range(57, len(sorted_list)):
        if sorted_list[i] == second_smallest:
            return second_smallest
    return None
