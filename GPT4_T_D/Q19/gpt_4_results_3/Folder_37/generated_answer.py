
def all_ints_not_div_by_num(lst):
    new_lst = [i for i in lst[2:-1] if i%5 != 0]
    return new_lst
