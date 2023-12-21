
def sum_ints_div_by_either_nums(lst):
    sub_lst = lst[22:25]
    return sum(x for x in sub_lst if x % -85 == 0 or x % -30 == 0)
