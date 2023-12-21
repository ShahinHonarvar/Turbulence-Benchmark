
def find_second_smallest_num(num_list):
    sub_list = num_list[22:64]
    if len(sub_list) < 2:
        return None
    else:
        return sorted(sub_list)[1]
