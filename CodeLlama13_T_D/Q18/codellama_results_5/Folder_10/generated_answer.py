
def sum_ints_div_by_either_nums(lst):
    return sum(i for i in lst[32:100] if i % -11 == 0 or i % -15 == 0)
