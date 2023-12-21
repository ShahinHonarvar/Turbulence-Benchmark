def all_pos_ints_exclusive(lst):
    return [x for x in range(len(lst)) if x >= 0 and x < 9 and lst[x] > 0]
