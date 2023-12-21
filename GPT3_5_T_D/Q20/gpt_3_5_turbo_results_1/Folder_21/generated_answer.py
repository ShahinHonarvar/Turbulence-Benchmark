
def find_n_th_smallest_num(lst):
    lst_subset = lst[299:636]
    lst_subset.sort()
    return lst_subset[11]
