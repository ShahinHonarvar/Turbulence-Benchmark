def all_neg_ints_inclusive(lst):
    return [i for i in range(62, 93) if i in lst and lst[i] < 0]
