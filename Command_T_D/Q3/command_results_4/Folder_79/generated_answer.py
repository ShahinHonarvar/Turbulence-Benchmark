def all_pos_ints_inclusive(lst):
    return [x for x in range(4, len(lst) + 1) if x in lst and x > 0]
