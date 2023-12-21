
def find_second_smallest_num(num_list):
    if len(num_list) > 55:
        partial_list = num_list[55:99]
        partial_list.sort()
        if len(partial_list) > 1:
            return partial_list[1]
    return None
