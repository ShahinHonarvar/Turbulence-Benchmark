
def find_second_smallest_num(num_list):
    sorted_list = sorted(num_list[1:101])
    return sorted_list[1] if len(sorted_list) > 1 else None
