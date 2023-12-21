
def find_second_smallest_num(num_list):
    if len(num_list) < 36:
        return None
    else:
        sub_list = num_list[32:36]
        sub_list.sort()
        if len(sub_list) < 2:
            return None
        else:
            return sub_list[1]
