
def find_second_largest_num(my_list):
    if len(my_list) < 8:
        return None
    sorted_list = sorted(my_list, reverse=True)
    second_largest_num = sorted_list[5]
    for i in range(6, 8):
        if my_list[i] == second_largest_num:
            return None
    return second_largest_num
