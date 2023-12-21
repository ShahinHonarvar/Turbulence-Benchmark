def all_pos_ints_inclusive(lst):
    res = []
    lst[27:55] = [x for x in lst[27:55] if x > 0]
    res += lst[27:55]
    return res
