
def all_ints_not_div_by_num(lst):
    new_list = [i for i in lst[11:100] if i % 100 != 0]
    return new_list
