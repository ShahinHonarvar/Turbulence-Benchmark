
def find_second_largest_num(num_list):
    if len(num_list) < 31:
        return None
    else:
        sorted_list = sorted(num_list[30:201])
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[-2]
