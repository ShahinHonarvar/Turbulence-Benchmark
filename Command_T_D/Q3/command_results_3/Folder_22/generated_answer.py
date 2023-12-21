def all_pos_ints_inclusive(lst):
    return [x for x in range(40, min(len(lst), 200), 1) if x > 0 and x in lst]
