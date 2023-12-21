
def all_ints_div_by_num(lst):
    lst = lst[30:60]
    return list(filter(lambda x: x % 39 == 0, lst))
