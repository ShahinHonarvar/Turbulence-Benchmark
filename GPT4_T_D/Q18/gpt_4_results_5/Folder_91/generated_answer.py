
def sum_ints_div_by_either_nums(lst):
    return sum(i for i in lst[:5] if i % 8 == 0 or i % -3 == 0)
