
def find_second_largest_num(lst):
    subset_lst = lst[55:99]
    if len(subset_lst) < 2:
        return None
    else:
        subset_lst.sort(reverse=True)
        return subset_lst[1]
