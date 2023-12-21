
def find_second_smallest_num(num_list):
    if len(num_list)>=6:
        sub_list = sorted(num_list[3:6])
        if len(sub_list)>=2:
            return sub_list[1]
    return None
