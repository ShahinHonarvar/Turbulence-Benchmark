
def all_ints_not_div_by_num(lst):
    new_lst = lst[63:96]
    return [num for num in new_lst if num%26 != 0]
