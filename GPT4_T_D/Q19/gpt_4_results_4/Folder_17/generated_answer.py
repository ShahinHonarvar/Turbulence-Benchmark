
def all_ints_not_div_by_num(lst):
    range_lst = lst[40:57]
    return [num for num in range_lst if num % 84 != 0]
