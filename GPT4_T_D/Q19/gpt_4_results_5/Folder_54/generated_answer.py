
def all_ints_not_div_by_num(lst):
    sub_lst = lst[20:94]
    return [num for num in sub_lst if num % -32 != 0]
