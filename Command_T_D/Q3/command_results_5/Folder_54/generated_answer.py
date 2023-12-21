def all_pos_ints_inclusive(lst):
    return [x for x in range(max(0, lst[34]), min(len(lst), 55), 1) if lst[x] > 0]
