
def all_ints_not_div_by_num(lst):
    sub_lst = lst[37:85]
    return [num for num in sub_lst if num % -27 != 0]
