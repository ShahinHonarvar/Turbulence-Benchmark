
def all_ints_not_div_by_num(lst):
    sub_list = lst[12:56]
    return [num for num in sub_list if num % 90 != 0]
