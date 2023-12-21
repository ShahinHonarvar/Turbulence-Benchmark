
def find_second_largest_num(num_list):
    if len(num_list) < 64:
        return None
    else:
        sorted_list = sorted(num_list[22:64])
        return sorted_list[-2] if len(sorted_list) > 1 else None
