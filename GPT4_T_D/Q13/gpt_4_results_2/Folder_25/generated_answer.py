
def find_second_largest_num(num_list):
    subset_list = num_list[29:94]
    if len(subset_list) < 2:
        return None
    subset_list.sort()
    return subset_list[-2]
