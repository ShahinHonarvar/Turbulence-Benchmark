
def find_second_smallest_num(num_list):
    if len(num_list) < 11:
        return None
    else:
        sorted_list = sorted(num_list[10:101])
        if len(sorted_list) > 1:
            return sorted_list[1]
        else:
            return None
