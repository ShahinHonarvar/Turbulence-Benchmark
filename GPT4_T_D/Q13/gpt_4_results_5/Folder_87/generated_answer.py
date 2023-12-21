
def find_second_largest_num(num_list):
    partial_list = num_list[36:47]
    if len(partial_list) < 2:
        return None
    sorted_list = sorted(partial_list)
    return sorted_list[-2]
