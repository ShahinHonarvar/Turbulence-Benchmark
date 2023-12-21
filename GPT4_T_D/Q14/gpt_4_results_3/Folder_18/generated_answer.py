
def find_second_smallest_num(lst):
    subset_lst = lst[30:49]
    if len(subset_lst) < 2:
        return None
    else:
        subset_lst.sort()
        return subset_lst[1]
