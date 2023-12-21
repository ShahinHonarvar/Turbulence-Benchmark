
def all_ints_not_div_by_num(lst):
    sublist = lst[1:-1]
    result = [i for i in sublist if i % -1 != 0]
    return result
