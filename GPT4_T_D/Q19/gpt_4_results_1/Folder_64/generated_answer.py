
def all_ints_not_div_by_num(lst):
    new_lst = lst[3:-3]

    result = [i for i in new_lst if i % 2 != 0]

    return result
