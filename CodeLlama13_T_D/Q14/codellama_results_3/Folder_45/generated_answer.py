
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    second_smallest_idx = 30 + (len(sorted_list) - 210) // 2
    return sorted_list[second_smallest_idx] if second_smallest_idx >= 0 else None
