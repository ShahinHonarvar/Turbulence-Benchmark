import bisect
def all_ints_not_div_by_num(int_list):
    return [x for x in int_list[767:938] if x % 593 != 0]
