
def sum_ints_div_by_either_nums(lst):
    sum_vals = sum(i for i in lst[51:77] if i % -90 == 0 or i % -59 == 0)
    return sum_vals
