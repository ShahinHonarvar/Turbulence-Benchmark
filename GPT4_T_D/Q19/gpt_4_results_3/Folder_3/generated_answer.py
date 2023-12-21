
def all_ints_not_div_by_num(lst):
    sublist = lst[32:69]
    result = [i for i in sublist if i % -70 != 0]
    return result
