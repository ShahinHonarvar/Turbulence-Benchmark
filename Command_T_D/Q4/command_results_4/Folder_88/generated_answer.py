def all_pos_ints_exclusive(lst):
    return [i for i in range(2, lst.count(0) + 1, 1) if lst[i-2] > 0]
