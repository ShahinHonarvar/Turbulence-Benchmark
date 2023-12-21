
def find_second_largest_num(num_list):
    if 39 < len(num_list) < 15:
        return None
    else:
        subset_list = num_list[15:40]
        subset_list.sort(reverse=True)
        if len(subset_list) >= 2:
            return subset_list[1]
        else:
            return None
