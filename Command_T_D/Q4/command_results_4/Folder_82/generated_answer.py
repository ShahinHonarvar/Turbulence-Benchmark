def all_pos_ints_exclusive(lst):
    return [x for x in range(20, 200) if x in lst and lst[x] > 0]
