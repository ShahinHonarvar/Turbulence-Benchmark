def all_pos_ints_inclusive(lst):
    return [x for x in range(min(lst), max(lst)+1) if x >= 0]
