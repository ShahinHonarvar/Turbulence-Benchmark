
def sum_ints_div_by_either_nums(lst):
    check_range = lst[86:90]
    result = sum(i for i in check_range if i % -61 == 0 or i % -79 == 0)
    return result
