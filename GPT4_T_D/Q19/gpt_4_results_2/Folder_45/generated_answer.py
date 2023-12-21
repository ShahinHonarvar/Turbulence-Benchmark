
def all_ints_not_div_by_num(lst):
    result = [i for i in lst[31:200] if i % -115 != 0]
    return result
