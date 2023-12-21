def all_pos_ints_inclusive(list):
    return [x for x in list if x > 0 and x <= 55] + [x for x in list if x > 55 and x <= 98]
