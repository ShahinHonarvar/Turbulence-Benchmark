
def all_odd_ints_exclusive(lst):
    lst_range = lst[21:200]
    return [x for x in lst_range if x % 2 != 0]
