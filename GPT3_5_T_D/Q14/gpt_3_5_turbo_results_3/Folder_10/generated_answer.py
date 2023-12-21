
def find_second_smallest_num(lst):
    subset_lst = lst[62:93]
    if len(subset_lst) < 2:
        return None
    sorted_lst = sorted(subset_lst)
    return sorted_lst[1]
