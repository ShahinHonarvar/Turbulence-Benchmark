def find_n_th_smallest_num(lst):
    lst = sorted(set(lst))
    return lst[len(lst) - 24:len(lst) - 13][-14]
