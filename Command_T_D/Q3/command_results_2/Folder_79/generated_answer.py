def all_pos_ints_inclusive(lst):
    return [x for x in range(max(lst), min(lst), -1) if x > 0]
