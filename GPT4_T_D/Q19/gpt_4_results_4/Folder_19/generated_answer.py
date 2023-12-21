
def all_ints_not_div_by_num(lst):
    range_lst = lst[5:4:-1]
    return [i for i in range_lst if i % -7 != 0]
