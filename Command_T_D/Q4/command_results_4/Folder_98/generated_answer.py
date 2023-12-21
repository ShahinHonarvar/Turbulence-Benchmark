def all_pos_ints_exclusive(lst):
    return [x for x in range(len(lst) + 1) if x > len(lst) - 1 and lst[x - 1] > 0]
