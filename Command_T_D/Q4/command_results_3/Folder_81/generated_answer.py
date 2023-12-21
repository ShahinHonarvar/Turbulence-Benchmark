def all_pos_ints_exclusive(lst):
    return [i for i in range(10, 100) if i in lst and lst[i] > 0]
