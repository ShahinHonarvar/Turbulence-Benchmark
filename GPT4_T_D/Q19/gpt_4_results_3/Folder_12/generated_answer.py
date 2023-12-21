
def all_ints_not_div_by_num(lst):
    relevant_lst = lst[60:93]
    return [i for i in relevant_lst if i % -26 != 0]
