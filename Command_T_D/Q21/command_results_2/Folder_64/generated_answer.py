def all_ints_div_by_num(lst):
    result = [x for x in lst if x % 4 == 0]
    return result if result else []
