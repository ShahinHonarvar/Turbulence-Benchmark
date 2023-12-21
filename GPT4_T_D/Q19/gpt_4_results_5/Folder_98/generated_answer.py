
def all_ints_not_div_by_num(lst):
    new_lst = lst[1:5]
    return [i for i in new_lst if i % 13 != 0]
