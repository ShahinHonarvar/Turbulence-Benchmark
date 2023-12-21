def all_pos_ints_inclusive(lst):
    return [x for x in range(min(x for x in lst), max(x for x in lst)+1) if x > 0]
