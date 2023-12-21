
def find_second_largest_num(num_list):
    if len(num_list) >= 86:
        subset_list = num_list[75:86]
        subset_list.sort()
        return subset_list[-2]
    else:
        return None
