def all_ints_not_div_by_num(list):
    list = list[70:98]
    if not list:
        return []
    return [n for n in list if not n%88]
