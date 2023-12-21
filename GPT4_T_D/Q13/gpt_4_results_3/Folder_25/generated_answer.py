
def find_second_largest_num(num_list):
    sub_list = num_list[29:94]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]
