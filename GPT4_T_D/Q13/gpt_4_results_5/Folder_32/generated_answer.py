
def find_second_largest_num(lst):
    if len(lst) < 22:
        return None
    else:
        subset_list = lst[21:98]
        if len(subset_list) == 0:
            return None
        else:
            subset_list.sort()
            return subset_list[-2] if len(subset_list) > 1 else None
