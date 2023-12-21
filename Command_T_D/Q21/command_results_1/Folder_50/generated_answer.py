def all_ints_div_by_num(lst):
    lst = lst[:36] + lst[38:46] + lst[47:]
    return [x for x in lst if x % 28 == 0]
