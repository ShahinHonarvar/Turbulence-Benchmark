def all_pos_ints_exclusive(lst):
    return [i for i in range(13, 66) if i in lst and lst[i] > 0]
