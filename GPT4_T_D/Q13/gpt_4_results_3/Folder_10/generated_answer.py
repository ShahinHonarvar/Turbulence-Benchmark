
def find_second_largest_num(num_list):
    if len(num_list) < 26:
        return None
    else:
        sorted_list = sorted(num_list[25:60])
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[-2]
