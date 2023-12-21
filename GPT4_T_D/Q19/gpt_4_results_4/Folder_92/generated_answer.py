
def all_ints_not_div_by_num(lst):
    result = [i for i in lst[2:] if i % -1 != 0]
    return result
