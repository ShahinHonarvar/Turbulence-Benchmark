
def find_second_smallest_num(num_list):
    valid_range = num_list[22:89]
    if len(valid_range) < 2:
        return None
    else:
        valid_range.sort()
        return valid_range[1]
