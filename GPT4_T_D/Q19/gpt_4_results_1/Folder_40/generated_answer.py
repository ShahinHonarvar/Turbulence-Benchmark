
def all_ints_not_div_by_num(lst):
    lst = lst[2:-1] 
    return [i for i in lst if i % 1 != 0]
