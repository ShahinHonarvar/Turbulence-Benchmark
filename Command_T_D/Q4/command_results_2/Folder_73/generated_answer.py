def all_pos_ints_exclusive(lst):
    return [i for i in range(36, 85) if i in lst and lst[i] > 0]
