
def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    sorted_list = sorted(num_list[:5])
    return sorted_list[-2] if len(sorted_list) > 1 else None
