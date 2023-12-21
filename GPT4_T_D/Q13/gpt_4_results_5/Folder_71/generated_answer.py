
def find_second_largest_num(num_list):
    subset_list = num_list[26:53]
    if len(subset_list) < 2:
        return None
    else:
        subset_list.sort()
        return subset_list[-2]
