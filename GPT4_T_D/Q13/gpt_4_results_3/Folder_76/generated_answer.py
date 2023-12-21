
def find_second_largest_num(num_list):
    sub_list = num_list[686:988]
    if not sub_list:
        return None
    else:
        return sorted(sub_list)[-2]
