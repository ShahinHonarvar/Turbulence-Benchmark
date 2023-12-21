
def all_pos_ints_inclusive(lst):
    range_lst = lst[15:40]
    return [i for i in range_lst if isinstance(i, int) and i > 0]
