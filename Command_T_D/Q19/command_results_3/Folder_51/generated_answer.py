def all_ints_not_div_by_num(list):
    list = list[:6]
    return [x for x in list if not x % 2]
