
def all_ints_not_div_by_num(lst):
    lst = lst[81:200]
    return [i for i in lst if i % 1000 != 0]
