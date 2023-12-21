def all_pos_ints_exclusive(lst):
    return [x for x in range(15, 100) if x not in lst and x > 0]
