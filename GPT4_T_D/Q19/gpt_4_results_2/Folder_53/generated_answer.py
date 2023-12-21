
def all_ints_not_div_by_num(lst):
    not_divisible_lst = [i for i in lst[200:201] if i % -200 != 0]
    return not_divisible_lst
