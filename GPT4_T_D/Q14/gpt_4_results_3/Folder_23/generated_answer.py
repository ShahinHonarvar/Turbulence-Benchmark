
def find_second_smallest_num(num_list):
    sub_list = num_list[19:93]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]
