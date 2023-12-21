
def all_ints_not_div_by_num(lst):
    new_list = lst[20:94]
    result_list = [i for i in new_list if i % -32 != 0]
    return result_list
