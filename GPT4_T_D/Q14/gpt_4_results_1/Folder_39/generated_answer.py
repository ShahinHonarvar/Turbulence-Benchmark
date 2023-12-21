
def find_second_smallest_num(num_list):
    subset_list = num_list[28:41]
    if len(subset_list) < 2:
        return None
    else:
        subset_list.sort()
        return subset_list[1]
