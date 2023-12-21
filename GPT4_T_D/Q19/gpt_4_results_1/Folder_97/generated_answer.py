
def all_ints_not_div_by_num(lst):
    sublist = lst[15:48]
    return [i for i in sublist if i%16 != 0]
