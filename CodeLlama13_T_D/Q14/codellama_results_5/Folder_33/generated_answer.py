
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    return sorted_list[262:746+1][1] if len(sorted_list[262:746+1]) > 1 else None
